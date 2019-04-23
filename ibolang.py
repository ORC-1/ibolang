#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import runpy
import code
from core import transpile
            
def commandline():
    """IgboLang, the programming language in Igbo

    usages:
        ibolang                 enter REPL
        ibolang [file.ibl]      execute IgboLang script
    """
    if len(sys.argv) > 2:
        print(commandline.__doc__)
        sys.exit(1)

    elif len(sys.argv) == 2:
        file_path = sys.argv[1]

        if not os.path.exists(file_path):
            print("ibl: file '%s' does not exists" % file_path)
            sys.exit(1)

        sys.path[0] = os.path.dirname(os.path.join(os.getcwd(), file_path))

        with open(file_path) as ibolang:
            python = transpile(src=ibolang)
            code_object = compile(python, file_path, "exec")
            runpy._run_module_code(code_object, mod_name="__main__")

    else:
        sys.ps1 = "ibl>> "
        banner = "IgboLang, the programming language in Igbo (Interactive Interpreter)"
        code.interact(banner=banner, readfunc=transpile)


if __name__=="__main__":
    commandline()
