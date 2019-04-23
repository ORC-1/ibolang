# -*- coding: utf-8 -*-

import tokenize
import readline
import io

from ig_tran import trans as translations

def translate_code(readline):
    for type, name, start, end, line in tokenize.generate_tokens(readline):
        if type == tokenize.NAME and name in translations:
            yield tokenize.NAME, translations[name], start, end, line
        else:
            yield type, name, start, end, line

def transpile(prompt=None, src=None):
    if src is None:
        src = io.StringIO(input(prompt))

    return tokenize.untokenize(list(translate_code(src.readline)))