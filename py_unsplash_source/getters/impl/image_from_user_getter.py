#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# image_from_user_getter.py
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

from py_unsplash_source.getters.impl.random_image_getter import RandomImageGetter


class ImageFromUserGetter(RandomImageGetter):
    """Getter that fetches a random item from a specific user's collection (extends RandomGetter)."""

    def __init__(self, user: str):
        # TODO: document this
        super(ImageFromUserGetter, self).__init__()
        self._url_prefix += '/user/{}'.format(user)

    def from_likes(self):
        self._url_prefix += '/likes'
        return self
