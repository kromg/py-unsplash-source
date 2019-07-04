#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# test_random_image_getter.py
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
from py_unsplash_source.getters.impl.random_image_getter import RandomImageGetter
from py_unsplash_source.images.fetched_image import FetchedImage


def test_random_image_getter_with_defaults():
    rg = RandomImageGetter()
    assert rg is not None
    assert isinstance(rg, (RandomImageGetter, BaseGetter))


def test_random_build_url():
    rg = RandomImageGetter(
    )
    assert rg._build_url() == ''


def test_random_build_url_with_geometry():
    rg = RandomImageGetter().geometry(800, 600)
    assert rg._build_url() == '/800x600'


def test_random_build_url_with_searches():
    rg = RandomImageGetter().search('some, random , string')
    assert rg._build_url() == '?random,some,string'
    rg = RandomImageGetter().search('some, random , string', 'another, search, terms, collection', 'random, some, else')
    assert rg._build_url() == '?another,collection,else,random,search,some,string,terms'


def test_random_build_url_with_reload_freq():
    rg = RandomImageGetter().daily()
    assert rg._build_url() == '/daily'

    rg = RandomImageGetter().weekly()
    assert rg._build_url() == '/weekly'


def test_random_build_url_with_all():
    rg = (RandomImageGetter()
          .geometry(800, 600)
          .search('random, search,string')
          .weekly())
    assert rg._build_url() == '/800x600/weekly?random,search,string'


@pytest.mark.skip('need to mock a server or to mock requests')
def test_get_raises_on_failure():
    with pytest.raises(DownloadException):
        RandomImageGetter().get()


def test_fetch_one_random_image():
    image = RandomImageGetter().get()
    assert isinstance(image, FetchedImage)
    # TODO: set geometry and verify that content is in fact an image and has required geometry.
