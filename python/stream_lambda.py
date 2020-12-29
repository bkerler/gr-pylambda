#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2015,2020 Tim O'Shea, Jacob Gilbert
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr
import pmt

class stream_lambda(gr.sync_block):
    """
    docstring for block stream_lambda
    """
    def __init__(self, fn, insig=[numpy.complex64], outsig=[numpy.complex64]):
        gr.sync_block.__init__(self,
            name="stream_lambda",
            in_sig=insig, out_sig=outsig)
        self.set_fn(fn)
        self.lvars = {}

    # signature should be:
    #     (output_stream_items) = lambda input_items, output_stream_index: ....
    def set_fn(self,fn):
        self.fn = fn

    def work(self, input_items, output_items):
        n_out = 0;
        for i in range(0,len(output_items)):
            o = self.fn(input_items, i)
            output_items[i][0:len(o)] = o[:]
            if(n_out == 0 or n_out == len(o)):
                n_out = len(o)
            else:
                raise Exception("Streams must produce same lengths for now with the current stream lambda block interface!")
        return n_out

