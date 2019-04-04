#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# test_collection_item_getter.py
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

from py_unsplash_source.getters.impl.collection_item_getter import CollectionItemGetter
from py_unsplash_source.getters.impl.random_getter import RandomGetter
from py_unsplash_source.getters.base_getter import BaseGetter, DownloadException

import pytest


def test_collection_item_getter_with_defaults():
    cig = CollectionItemGetter(123)
    assert cig is not None
    assert isinstance(cig, (CollectionItemGetter, RandomGetter, BaseGetter))


def test_collection_item_build_url():
    cig = CollectionItemGetter(123)
    assert cig._build_url() == '/collection/123'


def test_collection_item_build_url_with_geometry():
    cig = CollectionItemGetter(123).width(800).height(600)
    assert cig._build_url() == '/collection/123/800x600'


def test_collection_item_build_url_with_searches():
    cig = CollectionItemGetter(123).search('some, random , string')
    assert cig._build_url() == '/collection/123?random,some,string'


def test_collection_item_build_url_with_reload_freq():
    cig = CollectionItemGetter(123).daily()
    assert cig._build_url() == '/collection/123/daily'


def test_collection_item_build_url_with_all():
    cig = (CollectionItemGetter(123)
           .width(800)
           .height(600)
           .search('random, search,string')
           .weekly()
           )
    assert cig._build_url() == '/collection/123/800x600/weekly?random,search,string'


@pytest.mark.skip('need to mock a server or to mock requests')
def test_get_raises_on_failure():
    with pytest.raises(DownloadException):
        CollectionItemGetter(123).get()
