#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# collection_item_getter.py
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

from py_unsplash_source.getters.random_getter import RandomGetter
from py_unsplash_source.unsplash_server import UnsplashServer
from py_unsplash_source.getters.reload_frequency import ReloadFrequency


class CollectionItemGetter(RandomGetter):
    """Getter that fetches a random item from a specific collection by id (extends RandomGetter)."""

    def __init__(self,
                 collection_id: int,
                 server: UnsplashServer = UnsplashServer(),
                 width: int = None,
                 height: int = None,
                 search: str = None,
                 reload_freq: ReloadFrequency = None,
                 ):
        # TODO: document this
        super(CollectionItemGetter, self).__init__(server, width, height, search, reload_freq)
        self.url_prefix += '/collection/{}'.format(collection_id)
