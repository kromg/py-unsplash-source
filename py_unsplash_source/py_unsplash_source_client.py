#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# py_unsplash_source_client.py
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

from typing import Type

from py_unsplash_source.getters import CollectionItemGetter, UserItemGetter, FeaturedGetter, RandomGetter, ItemGetter
from py_unsplash_source.getters.base_getter import BaseGetter


class PyUnsplashSourceClient:

    def __init__(self,
                 width: int = None,
                 height: int = None):
        self.width = width
        self.height = height

    def _getter(self, getter_type: Type[BaseGetter], **kwargs):
        g = getter_type()
        # Inject default width/height if no overrides provided
        if self.width:
            g.width(self.width)
        if self.height:
            g.height(self.height)
        return g

    def random_getter(self) -> RandomGetter:
        return self._getter(RandomGetter)

    def item_getter(self, **kwargs):
        return self._getter(ItemGetter, **kwargs)

    def featured_getter(self, **kwargs):
        return self._getter(FeaturedGetter, **kwargs)

    def collection_item_getter(self, **kwargs):
        return self._getter(CollectionItemGetter, **kwargs)

    def user_item_getter(self, **kwargs):
        return self._getter(UserItemGetter, **kwargs)
