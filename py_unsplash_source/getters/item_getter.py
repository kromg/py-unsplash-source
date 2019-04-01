#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# item_getter.py
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

from abc import ABC
from py_unsplash_source.getters.base_getter import BaseGetter
from py_unsplash_source.unsplash_server import UnsplashServer
from py_unsplash_source.getters.reload_frequency import ReloadFrequency

import re

_SEARCH_SEPARATOR = re.compile(r'\s*,\s*')


class ItemGetter(BaseGetter, ABC):
    """Class to fetch a single item by id."""

    def __init__(self,
                 item_id: str,
                 server: UnsplashServer = UnsplashServer(),
                 width: int = None,
                 height: int = None,
                 ):
        # TODO: document this
        super(ItemGetter, self).__init__(server, width, height)
        self.url_prefix = '/{}'.format(item_id)

    def _build_url(self):
        url = self.url_prefix

        if self.width and self.height:
            url += '/{}x{}'.format(self.width, self.height)

        return url
