#!/usr/bin/env python



from core.common import retrieve_content

__url__ = "https://raw.githubusercontent.com/firehol/blocklist-ipsets/master/bitcoin_nodes_1d.ipset"
__check__ = "bitcoin_nodes_1d"
__info__ = "bad reputation (bitcoin node)"
__reference__ = "bitnodes.io"

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
