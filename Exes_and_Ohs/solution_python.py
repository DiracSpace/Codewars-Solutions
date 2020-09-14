#!/usr/bin/env python
import re
def xo(s):
    if (len(re.findall('x', s, re.IGNORECASE)) == len(re.findall('o', s, re.IGNORECASE))):
        return True
    else:
        return False
