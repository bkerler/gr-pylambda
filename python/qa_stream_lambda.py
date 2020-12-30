#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 Jacob Gilbert.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

from gnuradio import gr, gr_unittest
from stream_lambda import stream_lambda

class qa_stream_lambda(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_instance(self):
        # FIXME: Test will fail until you pass sensible arguments to the constructor
        instance = stream_lambda(lambda x, y: (x[0]**2)*0.1)

    def test_001_descriptive_test_name(self):
        # set up fg
        self.tb.run()
        # check data


if __name__ == '__main__':
    gr_unittest.run(qa_stream_lambda)
