# This file is part of Xpra.
# Copyright (C) 2013-2020 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

from xpra.server.auth.sys_auth_base import SysAuthenticator
from xpra.util import typedict


class Authenticator(SysAuthenticator):

    def __repr__(self):
        return "allow"

    def get_password(self) -> str:
        return ""

    def authenticate(self, _caps : typedict) -> bool:
        return True
