#!/usr/bin/env python

from core.common import retrieve_content

__url__ = "https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/proxylists_1d.ipset"
__check__ = "proxylists_1d"
__info__ = "proxy (suspicious)"
__reference__ = "proxylists.net"

def fetch():
    retval = {}
    content = retrieve_content(__url__)

    if __check__ in content:
        for line in content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#') or '.' not in line:
                continue
            retval[line] = (__info__, __reference__)

    return retval
