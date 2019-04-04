#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# image_getter.py
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


import re

from py_unsplash_source.getters.base_getter import BaseGetter

_SEARCH_SEPARATOR = re.compile(r'\s*,\s*')


class ImageGetter(BaseGetter):
    """Class to fetch a single item by id."""

    def __init__(self, item_id):
        # TODO: document this
        super(ImageGetter, self).__init__()
        self._url_prefix = '/{}'.format(item_id)

    def _build_url(self):
        url = self._url_prefix

        if self._width and self._height:
            url += '/{}x{}'.format(self._width, self._height)

        return url
