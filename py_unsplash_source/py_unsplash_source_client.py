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

    def _getter(self, getter_type: Type[BaseGetter], *args):
        g = getter_type(*args)
        # Inject default width/height if no overrides provided
        if self.width:
            g.width(self.width)
        if self.height:
            g.height(self.height)
        return g

    def random_getter(self) -> RandomGetter:
        return self._getter(RandomGetter)

    def item_getter(self, image_id: str) -> ItemGetter:
        return self._getter(ItemGetter, image_id)

    def featured_getter(self) -> FeaturedGetter:
        return self._getter(FeaturedGetter)

    def collection_item_getter(self, collection_id: int) -> CollectionItemGetter:
        return self._getter(CollectionItemGetter, collection_id)

    def user_item_getter(self, user_id: str) -> UserItemGetter:
        return self._getter(UserItemGetter, user_id)
