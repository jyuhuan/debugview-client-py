#!/usr/bin/env python
# -*- coding: utf-8; -*-

""""""

from me.yuhuan.debugview.server import TaskCode
from me.yuhuan.util.net.TcpMessenger import TcpMessenger
from me.yuhuan.util.StringUtils import *

__author__ = "Yuhuan Jiang"
__email__ = "jyuhuan@gmail.com"
__version__ = "1.0"


segment_size = 1024

def renderHtml(class_name, html_str):

    messenger = TcpMessenger("127.0.0.1", 1234)
    messenger.send_int(TaskCode.RenderHtml)
    messenger.send_string(class_name)

    segments = list(grouped(html_str, segment_size))

    messenger.send_int(len(segments))
    for segment in segments:
        messenger.send_string(segment)

