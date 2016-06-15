import logging
from collections import namedtuple
from crypt import crypt

import requests

_VERSION_ = "0.0.5"
_LOGGER = logging.getLogger(__name__)


class CineMaterial(object):
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        self._url_skel = "https://api.cinematerial.com/1/request.json?imdb_id={imdb_id}&api_key={public_key}&secret=" \
                         "{secret}&width={width}"

    def search(self, imdb_id, width=300):
        url = self._url_skel.format(imdb_id=imdb_id, width=width, public_key=self.public_key,
                                    secret=self._generate_hash(imdb_id))
        _LOGGER.debug("Requesting URL: {}".format(url))
        return self._request(url)

    # noinspection PyMethodMayBeStatic
    def _request(self, url):
        response = requests.get(url)
        if response.status_code != requests.codes.ok:
            return None

        json = response.json()
        _LOGGER.debug("Response: {}".format(json))
        if "errors" in json:
            return None

        return CineMaterialSearchResult(**json)

    def _generate_hash(self, imdb_id):
        return crypt(imdb_id + self.private_key)


CineMaterialSearchResult = namedtuple("CineMaterialSearchResult",
                                      ["imdb", "year", "title", "page", "posters"])
