#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# test_image_from_featured_getter.py
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

from py_unsplash_source.getters.impl.image_from_featured_getter import ImageFromFeaturedGetter
from py_unsplash_source.getters.impl.random_image_getter import RandomImageGetter
from py_unsplash_source.getters.base_getter import BaseGetter, DownloadException
from py_unsplash_source.images.fetched_image import FetchedImage

import pytest


def test_image_from_featured_getter_with_defaults():
    fg = ImageFromFeaturedGetter()
    assert fg is not None
    assert isinstance(fg, (ImageFromFeaturedGetter, RandomImageGetter, BaseGetter))


def test_image_from_featured_build_url():
    fg = ImageFromFeaturedGetter()
    assert fg._build_url() == '/featured'


def test_image_from_featured_build_url_with_geometry():
    fg = ImageFromFeaturedGetter().geometry(800, 600)
    assert fg._build_url() == '/featured/800x600'


def test_image_from_featured_build_url_with_searches():
    fg = ImageFromFeaturedGetter().search('some, random , string')
    assert fg._build_url() == '/featured?random,some,string'


def test_image_from_featured_build_url_with_reload_freq():
    fg = ImageFromFeaturedGetter().daily()
    assert fg._build_url() == '/featured/daily'


def test_image_from_featured_build_url_with_all():
    fg = (ImageFromFeaturedGetter()
          .geometry(800, 600)
          .search('random, search,string')
          .weekly()
          )
    assert fg._build_url() == '/featured/800x600/weekly?random,search,string'


@pytest.mark.skip('need to mock a server or to mock requests')
def test_get_raises_on_failure():
    with pytest.raises(DownloadException):
        ImageFromFeaturedGetter().get()


def test_fetch_one_random_image():
    image = ImageFromFeaturedGetter().get()
    assert isinstance(image, FetchedImage)
    # TODO: set geometry and verify that content is in fact an image and has required geometry.
