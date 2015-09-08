#!/usr/bin/env python
# -*- coding: utf-8; -*-

""""""

__author__ = "Yuhuan Jiang"
__email__ = "jyuhuan@gmail.com"
__version__ = "1.0"

def grouped(str, group_length):
    for i in xrange(0, len(str), group_length):
        yield str[i:i + group_length]
