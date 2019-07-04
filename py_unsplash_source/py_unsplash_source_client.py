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

from py_unsplash_source.getters import ImageFromCollectionGetter, ImageFromUserGetter, ImageFromFeaturedGetter, RandomImageGetter, ImageGetter
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
        if self.width and self.height:
            g.geometry(self.width, self.height)
        return g

    def random_image(self) -> RandomImageGetter:
        return self._getter(RandomImageGetter)

    def image(self, image_id: str) -> ImageGetter:
        return self._getter(ImageGetter, image_id)

    def image_from_featured(self) -> ImageFromFeaturedGetter:
        return self._getter(ImageFromFeaturedGetter)

    def image_from_collection(self, collection_id: int) -> ImageFromCollectionGetter:
        return self._getter(ImageFromCollectionGetter, collection_id)

    def image_from_user(self, user_id: str) -> ImageFromUserGetter:
        return self._getter(ImageFromUserGetter, user_id)
