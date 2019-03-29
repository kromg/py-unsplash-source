#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# BaseGetter
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


class FeaturedGetter(RandomGetter):
    """Getter that fetches a random item from a featured collection (extends RandomGetter)."""

    def __init__(self,
                 server: UnsplashServer = UnsplashServer(),
                 width: int = None,
                 height: int = None,
                 search: str = None,
                 update_freq=None,
                 ):
        # TODO: document this
        super(FeaturedGetter, self).__init__(server, width, height, search, update_freq)

    def _build_request(self):
        return None

