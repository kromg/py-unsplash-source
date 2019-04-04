#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# test_item_getter.py
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

import pytest
from py_unsplash_source.getters.base_getter import BaseGetter, DownloadException
from py_unsplash_source.getters.impl.item_getter import ItemGetter
from py_unsplash_source.images.fetched_image import FetchedImage


def test_item_getter_with_defaults():
    ig = ItemGetter('abc')
    assert ig is not None
    assert isinstance(ig, (ItemGetter, BaseGetter))


def test_item_getter_build_url():
    ig = ItemGetter('abc')
    assert ig._build_url() == '/abc'


def test_item_getter_build_url_with_geometry():
    ig = ItemGetter('abc').width(800).height(600)
    assert ig._build_url() == '/abc/800x600'

    # No single-dimension geometry
    ig = ItemGetter('abc').width(800)
    assert ig._build_url() == '/abc'
    ig = ItemGetter('abc').height(600)
    assert ig._build_url() == '/abc'


@pytest.mark.skip('need to mock a server or to mock requests')
def test_get_raises_on_failure(unsplash_server):
    with pytest.raises(DownloadException):
        ItemGetter(unsplash_server).get()


def test_fetch_one_image():
    image = ItemGetter('WLUHO9A_xik').get()
    assert isinstance(image, FetchedImage)
    # TODO: set geometry and verify that content is in fact an image and has required geometry.
