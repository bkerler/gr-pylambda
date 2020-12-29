#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2015,2020 Tim O'Shea, Jacob Gilbert.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr
import pmt



class pdu_lambda(gr.basic_block):
    """
    docstring for block pdu_lambda
    """

    def __init__(self, fn, metadict, key=pmt.PMT_NIL):
        gr.basic_block.__init__(self,
            name="pdu_lambda",
            in_sig=[],out_sig=[])
        self.set_fn(fn)
        self.set_key(key)
        self.metadict_mode = metadict
        self.message_port_register_in(pmt.intern("pdu"))
        self.message_port_register_out(pmt.intern("pdu"))
        self.set_msg_handler(pmt.intern("pdu"), self.handle_msg)   

    def handle_msg(self, pdu):
        if self.metadict_mode:
            meta = pmt.car(pdu)
            try:
                val = pmt.to_python(pmt.dict_ref(meta, self.key, pmt.PMT_NIL))
                if val:
                    val = self.fn(val)
                meta = pmt.dict_add(meta, self.key, pmt.to_pmt(val))
            except: # hide errors to make troubleshooting impossible
                pass
            self.message_port_pub(pmt.intern("pdu"), 
                pmt.cons(meta, pmt.cdr(pdu)));

        else: # PDU Vector mode
            vec = pmt.to_python(pmt.cdr(pdu))
            vec = self.fn(vec)
            self.message_port_pub(pmt.intern("pdu"), 
                pmt.cons(pmt.car(pdu), pmt.to_pmt(vec)));

    def set_fn(self,fn):
        self.fn = fn

    def set_key(self,key):
        self.key = key
