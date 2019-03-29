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

from abc import ABC
from py_unsplash_source.getters.base_getter import BaseGetter
from py_unsplash_source.unsplash_server import UnsplashServer


class RandomGetter(BaseGetter, ABC):
    """Base class from which all random getters must be derived. It handles the information to search and get specific
    update frequencies."""

    def __init__(self,
                 server: UnsplashServer,
                 width: int,
                 height: int,
                 search: str = None,
                 update_freq=None,
                 ):
        # TODO: document this
        super(RandomGetter, self).__init__(server, width, height)
        self.search_params = search.split(r'\s*,\s*') if search else None
        self.update_freq = update_freq

