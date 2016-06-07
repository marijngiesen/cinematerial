from collections import namedtuple
from crypt import crypt

import requests

_VERSION_ = "0.0.1"


class CineMaterial(object):
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        self._url_skel = "https://api.cinematerial.com/1/request.json?imdb_id={imdb_id}&api_key={public_key}&secret=" \
                         "{secret}&width={width}"

    def search(self, imdb_id, width=300):
        return self._request(self._url_skel.format(imdb_id=imdb_id, width=width, public_key=self.public_key,
                                                   secret=self._generate_hash(imdb_id)))

    # noinspection PyMethodMayBeStatic
    def _request(self, url):
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            return CineMaterialSearchResult(**response.json())
        else:
            return None

    def _generate_hash(self, imdb_id):
        return crypt(imdb_id + self.private_key)


CineMaterialSearchResult = namedtuple("CineMaterialSearchResult", ["imdb", "year", "title", "page", "posters"])
