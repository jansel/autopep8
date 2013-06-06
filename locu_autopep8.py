#!/usr/bin/env python
import re
import sys
import tokenize

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import autopep8


def fix_l99901(source):
    """
    Replace "x" strings with 'x' strings
    Replace '''y''' strings with "\""y"\""
    """
    lines = StringIO(source).readlines()
    for i, line in enumerate(lines):
        try:
            g = tokenize.generate_tokens(StringIO(line).readline)
            for toknum, val, _, _, _ in g:
                if toknum == tokenize.STRING:
                    newval = None

                    m = re.match(r'^"([^"\'\\]*)"$', val)
                    if m:
                        newval = u"'{0}'".format(m.group(1))

                    m = re.match(r"^'''([^\"'\\]*)'''$", val)
                    if m:
                        newval = u'"""{0}"""'.format(m.group(1))

                    if (newval and
                            line.replace(val, newval, 1) == line.replace(val, newval, 2)):
                        lines[i] = line.replace(val, newval, 1)

        except tokenize.TokenError:
            pass
    return ''.join(lines)


def fix_l99902(source):
    """
    Force utf-8 encoding
    """
    lines = StringIO(source).readlines()
    if len(lines) > 2:
        if ('coding' not in lines[0].lower() and
                'coding' not in lines[1].lower()):
            pos = 1 if lines[0][:2] == "#!" else 0
            lines.insert(pos, '# coding: utf-8')
    return ''.join(lines)

autopep8.fix_l99901 = fix_l99901
autopep8.fix_l99902 = fix_l99902
autopep8.DEFAULT_INDENT_SIZE = 2

if __name__ == '__main__':
    sys.exit(autopep8.main())
