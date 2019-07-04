#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# base_getter.py
# Copyright (C) 2019 Giacomo Montagner <kromg.kromg@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from abc import ABC, abstractmethod

import requests

from py_unsplash_source.images.fetched_image import FetchedImage
from py_unsplash_source.unsplash_endpoint import UnsplashEndpoint


class DownloadException(Exception):
    """Raised when download fails."""


class BaseGetter(ABC):
    """Base class from which all getters must be derived. It handles the basic information to fetch an image."""

    def __init__(self):
        # TODO: document this
        self._endpoint = UnsplashEndpoint()

        self._width = None
        self._height = None

        self._url_prefix = ''

    @abstractmethod
    def _build_url(self):
        """This method must be implemented by each derived getter and it must return the URL string to be
        used to fetch an item."""
        # TODO: enhance docstring with params and returns

    def get(self):
        """Fetch an image per configuration of this getter. Returns a FetchedImage instance"""
        # TODO: enhance docstring with params and returns
        url = '{}{}'.format(self._endpoint, self._build_url())
        response = requests.get(url)
        if response.status_code is not 200:
            raise DownloadException('Fetch: {} - returned: {}'.format(
                url,
                response.status_code
            ))
        return FetchedImage(response.content)

    def endpoint(self, endpoint: UnsplashEndpoint):
        self._endpoint = endpoint
        return self

    def geometry(self, width: int, height: int):
        self._width = width
        self._height = height
        return self
