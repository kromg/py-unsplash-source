#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# test_image_getter.py
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
from py_unsplash_source.getters.impl.image_getter import ImageGetter
from py_unsplash_source.images.fetched_image import FetchedImage


def test_image_getter_with_defaults():
    ig = ImageGetter('abc')
    assert ig is not None
    assert isinstance(ig, (ImageGetter, BaseGetter))


def test_image_getter_build_url():
    ig = ImageGetter('abc')
    assert ig._build_url() == '/abc'


def test_image_getter_build_url_with_geometry():
    ig = ImageGetter('abc').geometry(800, 600)
    assert ig._build_url() == '/abc/800x600'


@pytest.mark.skip('need to mock a server or to mock requests')
def test_get_raises_on_failure(unsplash_server):
    with pytest.raises(DownloadException):
        ImageGetter(unsplash_server).get()


def test_fetch_one_image():
    image = ImageGetter('WLUHO9A_xik').get()
    assert isinstance(image, FetchedImage)
    # TODO: set geometry and verify that content is in fact an image and has required geometry.
