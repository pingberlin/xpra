# This file is part of Xpra.
# Copyright (C) 2021-2023 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

import os
import sys
from typing import Any

from xpra.util import parse_simple_dict
from xpra.os_util import WIN32
from xpra.scripts.config import InitException
from xpra.log import Logger

log = Logger("auth")


def get_auth_module(auth_str, cwd=os.getcwd(), **auth_options) -> tuple[str,Any,type,dict]:
    log("get_auth_module(%s, {..})", auth_str)
    #separate options from the auth module name
    #either with ":" or "," as separator
    scpos = auth_str.find(":")
    cpos = auth_str.find(",")
    if cpos<0 or scpos<cpos:
        parts = auth_str.split(":", 1)
    else:
        parts = auth_str.split(",", 1)
    auth = parts[0]
    if len(parts)>1:
        auth_options.update(parse_simple_dict(parts[1]))
    auth_options["exec_cwd"] = cwd
    try:
        if auth=="sys":
            #resolve virtual "sys" auth:
            if WIN32:
                auth_modname = "win32_auth"
            else:
                auth_modname = "pam_auth"
            log("will try to use sys auth module '%s' for %s", auth, sys.platform)
        else:
            auth_modname = auth.replace("-", "_")+"_auth"
        auth_mod_name = "xpra.server.auth."+auth_modname
        log("auth module name for '%s': '%s'", auth, auth_mod_name)
        auth_module = __import__(auth_mod_name, {}, {}, ["Authenticator"])
    except ImportError as e:
        log("cannot load %s auth for %r", auth, auth_str, exc_info=True)
        raise InitException(f"cannot load authentication module '{auth}' for {auth_str!r}: {e}") from None
    log("auth module for '%s': %s", auth, auth_module)
    try:
        auth_class = auth_module.Authenticator
        auth_class.auth_name = auth.lower()
        return auth, auth_module, auth_class, auth_options
    except Exception as e:
        log("cannot access authenticator class", exc_info=True)
        raise InitException(f"authentication setup error in {auth_module}: {e}") from None

