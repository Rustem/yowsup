import os
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

def getFromEnviron():
    url = None
    for key in ('http_proxy', 'https_proxy'):
        url = os.environ.get(key)
        if url: break
    if not url:
        return None
    return urlparse(url)
    