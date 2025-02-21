# This file is part of Xpra.
# Copyright (C) 2012-2023 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

from xpra.x11.gtk_x11.prop import prop_set, prop_get, prop_del
from xpra.gtk_common.gtk_util import get_default_root_window

def root_xid() -> int:
    root = get_default_root_window()
    if not root:
        return 0
    return root.get_xid()

def save_uuid(uuid):
    prop_set(root_xid(), "XPRA_SERVER_UUID", "latin1", uuid)

def get_uuid():
    return prop_get(root_xid(), "XPRA_SERVER_UUID", "latin1", ignore_errors=True)

def del_uuid():
    prop_del(root_xid(), "XPRA_SERVER_UUID")


def save_mode(mode):
    prop_set(root_xid(), "XPRA_SERVER_MODE", "latin1", mode)

def get_mode():
    return prop_get(root_xid(), "XPRA_SERVER_MODE", "latin1", ignore_errors=True)

def del_mode():
    prop_del(root_xid(), "XPRA_SERVER_MODE")
