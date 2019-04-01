#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# test_featured_getter.py
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

from py_unsplash_source.getters.featured_getter import FeaturedGetter
from py_unsplash_source.getters.random_getter import RandomGetter
from py_unsplash_source.getters.base_getter import BaseGetter, DownloadException
from py_unsplash_source.getters.reload_frequency import ReloadFrequency
from py_unsplash_source.getters.fetched_image import FetchedImage

import pytest


def test_featured_getter_with_defaults():
    fg = FeaturedGetter()
    assert fg is not None
    assert isinstance(fg, (FeaturedGetter, RandomGetter, BaseGetter))


def test_featured_build_url():
    fg = FeaturedGetter(
    )
    assert fg._build_url() == '/featured'


def test_featured_build_url_with_geometry():
    fg = FeaturedGetter(
        width=800,
        height=600
    )
    assert fg._build_url() == '/featured/800x600'


def test_featured_build_url_with_searches():
    fg = FeaturedGetter(
        search='some, random , string'
    )
    assert fg._build_url() == '/featured?some,random,string'


def test_featured_build_url_with_reload_freq():
    fg = FeaturedGetter(
        reload_freq=ReloadFrequency.DAILY
    )
    assert fg._build_url() == '/featured/daily'


def test_featured_build_url_with_all():
    fg = FeaturedGetter(
        width=800,
        height=600,
        reload_freq=ReloadFrequency.WEEKLY,
        search='random, search,string'
    )
    assert fg._build_url() == '/featured/weekly/800x600?random,search,string'


@pytest.mark.skip('need to mock a server or to mock requests')
def test_get_raises_on_failure(unsplash_server):
    with pytest.raises(DownloadException):
        FeaturedGetter(unsplash_server).get()


def test_fetch_one_random_image():
    image = FeaturedGetter().get()
    assert isinstance(image, FetchedImage)
    # TODO: set geometry and verify that content is in fact an image and has required geometry.
