# -*- coding: utf-8 -*-

import requests
import json
from urllib import unquote_plus


class TrendsBusca(object):
    '''
        >>> tb = TrendsBusca('gnt')
        >>> tb.url
        'http://www.google.com/trends/fetchComponent?hl=pt-BR&q=gnt' ...
        >>> tb.json
        {u'sig' ...
    '''

    URL = ('http://www.google.com/trends/fetchComponent?hl=pt-BR&q=%(q)s'
           '&content=1&cid=TOP_QUERIES_0_0&export=3')

    def __init__(self, query):
        import ipdb
        ipdb.set_trace()
        self._url = TrendsBusca.URL % {'q': unquote_plus(query)}
        self._response = requests.get(self._url)

    @property
    def json(self):
        if self._response.ok:
            json_slice = slice(62, -2)
            json_string = self._response.content[json_slice]
            return json.loads(json_string)
        else:
            return None

    @property
    def url(self):
        return self._url
