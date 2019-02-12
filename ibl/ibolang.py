#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import tokenize
import ig_tran
import runpy
from core import translate_code

translations = ig_tran.trans
            
def commandline():
    """IgboLang, the programming language in Igbo

    usage: ibolang file.ibl
    """
    if len(sys.argv) != 2:
        print(commandline.__doc__)
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print("ibl: file '%s' does not exists" % file_path)
        sys.exit(1)

    #sys.meta_path = [ImportHook()]

    sys.path[0] = os.path.dirname(os.path.join(os.getcwd(), file_path))

    source = tokenize.untokenize(
            list(translate_code(open(file_path).readline, translations)))

    #translate_module(__builtins__)

    code = compile(source, file_path, "exec")

    runpy._run_module_code(code, mod_name="__main__")

if __name__=="__main__":
    commandline()