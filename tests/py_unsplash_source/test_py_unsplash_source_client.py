#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# test_py_unsplash_source_client.py
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

from py_unsplash_source.py_unsplash_source_client import PyUnsplashSourceClient
from py_unsplash_source.getters import CollectionItemGetter, FeaturedGetter, ItemGetter, RandomGetter, UserItemGetter


defaults = {'width': 800, 'height': 600}


def test_client():
    c = PyUnsplashSourceClient()
    assert isinstance(c, PyUnsplashSourceClient)


def test_client_with_defaults():
    c = PyUnsplashSourceClient(**defaults)
    assert isinstance(c, PyUnsplashSourceClient)
    assert c.width == 800
    assert c.height == 600


def test_client_can_create_collection_item_getter():
    c = PyUnsplashSourceClient(**defaults)
    g = c.collection_item_getter(123)
    assert isinstance(g, CollectionItemGetter)
    assert g._width == 800
    assert g._height == 600


def test_client_can_create_featured_getter():
    c = PyUnsplashSourceClient(**defaults)
    g = c.featured_getter()
    assert isinstance(g, FeaturedGetter)
    assert g._width == 800
    assert g._height == 600


def test_client_can_create_item_getter():
    c = PyUnsplashSourceClient(**defaults)
    g = c.item_getter('abc')
    assert isinstance(g, ItemGetter)
    assert g._width == 800
    assert g._height == 600


def test_client_can_create_random_getter():
    c = PyUnsplashSourceClient(**defaults)
    g = c.random_getter()
    assert isinstance(g, RandomGetter)
    assert g._width == 800
    assert g._height == 600


def test_client_can_create_user_item_getter():
    c = PyUnsplashSourceClient(**defaults)
    g = c.user_item_getter('usrName')
    assert isinstance(g, UserItemGetter)
    assert g._width == 800
    assert g._height == 600
