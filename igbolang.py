#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Igbo keyword dictionaries

This is the MIT license:
http://www.opensource.org/licenses/mit-license.php

Copyright (c) 2019~ Roland|Chima and contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to
deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""


# Universal keywords repository
#: always run annotator before access worddict
worddict = {}
#: Traditional Igbo keywords repository
igbodict = {}


class IgboPlugin(object):
    """
    basic plugin class
    """
    pass


def revert_dict(lang_dict):
    """make a reverse dictionary from the input dictionary

    >>> revert_dict({'a':'1', 'b':'2'})
    {'1': 'a', '2': 'b'}
    """
    rev_dict = {}
    dict_keys = lang_dict.keys()
    dict_keys.reverse()
    #map(rev_dict.update, map(lambda i: {lang_dict[i]:i}, dict_keys))
    for i in dict_keys:
        rev_dict.update({lang_dict[i]:i})
    return rev_dict
