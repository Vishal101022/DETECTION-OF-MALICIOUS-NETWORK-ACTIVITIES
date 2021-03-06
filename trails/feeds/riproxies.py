#!/usr/bin/env python


from core.common import retrieve_content

__url__ = "https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/ri_web_proxies_30d.ipset"
__check__ = "ri_web_proxies_30d"
__info__ = "proxy (suspicious)"
__reference__ = "rosinstrument.com"

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
