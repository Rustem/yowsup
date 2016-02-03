#!/usr/bin/env python

from .warequest import WARequest

class WADummyRequest(WARequest):

    def __init__(self):
        super(WADummyRequest, self).__init__()
        self.url = "v.whatsapp.net"

def test():
    req = WADummyRequest()
    return req.send()

if __name__ == '__main__':
    print test()