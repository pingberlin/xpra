#!/usr/bin/env python
# This file is part of Xpra.
# Copyright (C) 2018-2019 Antoine Martin <antoine@xpra.org>
# Xpra is released under the terms of the GNU GPL v2, or, at your option, any
# later version. See the file COPYING for details.

import unittest
import binascii

from xpra.util import AdHocStruct
from unit.server.mixins.servermixintest_util import ServerMixinTest


class WebcamMixinTest(ServerMixinTest):

    def test_webcam(self):
        from xpra.server.mixins.webcam_server import WebcamServer
        from xpra.server.source.webcam_mixin import WebcamMixin
        opts = AdHocStruct()
        opts.webcam = "yes"
        self._test_mixin_class(WebcamServer, opts, {}, WebcamMixin)
        self.debug_all()
        if self.mixin.get_info(self.protocol).get("webcam", {}).get("virtual-video-devices", 0)>0:
            self.handle_packet(("webcam-start", 0, 640, 480))
            png_hex_data = "89504e470d0a1a0a0000000d4948445200000280000001e00802000000bab34bb3000005f34944415478daedd53101000008c330c0bfe7e1029e44429f769202006e8d040060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00080010380010380010300060c00060c0018300018300060c00060c00080010380010380010300060c00060c0018300018300060c00060c00080010380010380010300060c00060c0018300018300060c00060c00080010380010380010300060c00060c0018300018300060c00060c00080010380010380010300060c00060c0018300018300060c00060c00080010380010380010300060c00060c0018300018300060c00060c00080010380010380010300060c00060c0018300018300060c00060c00080010380010380010300060c00060c0018300018300060c00060c00080010380010380010300060c00060c0018300018300060c00060c00080010380010300060c00060c00060c0018300018300060c00060c00080010380010300060c00060c00060c0018300018300060c00060c00080010380010300060c00060c00060c0018300018300060c00060c00080010380010300060c00060c00060c0018300018300060c00060c00080010380010300060c00060c00060c0018300018300060c00060c00080010380010300060c00060c00060c0018300018300060c00060c00080010380010300060c00060c00060c0018300018300060c00060c00080010380010300060c00060c00060c0018300018300060c00060c00080010380010300060c00060c00060c0018300018300060c00060c00080010380010300060c00060c00062c010018300018300060c00060c00080010380010300060c00060c0018300018300018300060c00060c00080010380010300060c00060c0018300018300018300060c00060c00080010380010300060c00060c0018300018300018300060c00060c00080010380010300060c00060c0018300018300018300060c00060c00080010380010300060c00060c0018300018300018300060c00060c00080010380010300060c00060c0018300018300018300060c00060c00080010380010300060c00060c0018300018300018300060c00060c00080010380010300060c00060c0018300018300018300060c00060c00080010380010300060c00060c0018300018300018300060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00060c00080010380010300060c00060c0018300018300060c00060c00080010380010380010300060c00060c0018300018300060c00060c00080010380010380010300060c00060c0018300018300060c00060c00080010380010380010300060c00060c0018300018300060c00060c00080010380010380010300060c00060c0018300018300060c00060c00080010380010380010300060c00060c0018300018300060c00060c000800103c0bf05fda806bd1bd7b4640000000049454e44ae426082"
            png_data = binascii.unhexlify(png_hex_data)
            self.handle_packet(("webcam-frame", 0, 0, "png", 640, 480, png_data))
            self.handle_packet(("webcam-stop", 0, "end"))

def main():
    unittest.main()


if __name__ == '__main__':
    main()
