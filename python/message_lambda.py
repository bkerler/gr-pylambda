#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 Jacob Gilbert.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr
import pmt

class message_lambda(gr.basic_block):
    """
    docstring for block message_lambda
    """
    def __init__(self, fn):
        gr.basic_block.__init__(self,
            name="message_lambda",
            in_sig=[],out_sig=[])
        self.set_fn(fn)
        self.message_port_register_in(pmt.intern("msg"))
        self.message_port_register_out(pmt.intern("msg"))
        self.set_msg_handler(pmt.intern("msg"), self.handle_msg)

    def handle_msg(self, msg):
        try:
            msg = self.fn(msg)
            self.message_port_pub(pmt.intern("msg"), msg)
        except:
            pass

    def set_fn(self,fn):
        self.fn = fn
