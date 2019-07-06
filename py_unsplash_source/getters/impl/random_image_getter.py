#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# random_image_getter.py
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
from py_unsplash_source.getters.reload_frequency import ReloadFrequency

_SEARCH_SEPARATOR = re.compile(r'\s*,\s*')


class RandomImageGetter(BaseGetter):
    """Base class for fetching random items. More specialized classes can extend this class for specific cases."""

    def __init__(self):
        # TODO: document this
        super(RandomImageGetter, self).__init__()
        self._search_params = set()
        self._reload_freq = None

    def _build_url(self):
        url = self._url_prefix

        if self._width and self._height:
            url += '/{}x{}'.format(self._width, self._height)

        if self._reload_freq and '/likes' not in url:
            url += '/{}'.format(self._reload_freq.value)

        if self._search_params and '/likes' not in url:
            url += '?{}'.format(','.join(sorted(self._search_params)))

        return url

    def search(self, *search_params_list: str):
        for search_params in search_params_list:
            self._search_params = self._search_params.union(self._search_params, set(_SEARCH_SEPARATOR.split(search_params)))
        return self

    def daily(self):
        self._reload_freq = ReloadFrequency.DAILY
        return self

    def weekly(self):
        self._reload_freq = ReloadFrequency.WEEKLY
        return self
