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
from py_unsplash_source.getters import ImageFromCollectionGetter, ImageFromFeaturedGetter, ImageGetter, RandomImageGetter, ImageFromUserGetter


defaults = {'width': 800, 'height': 600}


def test_client():
    c = PyUnsplashSourceClient()
    assert isinstance(c, PyUnsplashSourceClient)


def test_client_with_defaults():
    c = PyUnsplashSourceClient(**defaults)
    assert isinstance(c, PyUnsplashSourceClient)
    assert c.width == 800
    assert c.height == 600


def test_client_can_create_image_from_collection_getter():
    c = PyUnsplashSourceClient(**defaults)
    g = c.image_from_collection(123)
    assert isinstance(g, ImageFromCollectionGetter)
    assert g._width == 800
    assert g._height == 600


def test_client_can_create_featured_getter():
    c = PyUnsplashSourceClient(**defaults)
    g = c.image_from_featured()
    assert isinstance(g, ImageFromFeaturedGetter)
    assert g._width == 800
    assert g._height == 600


def test_client_can_create_image_getter():
    c = PyUnsplashSourceClient(**defaults)
    g = c.image('abc')
    assert isinstance(g, ImageGetter)
    assert g._width == 800
    assert g._height == 600


def test_client_can_create_random_getter():
    c = PyUnsplashSourceClient(**defaults)
    g = c.random_image()
    assert isinstance(g, RandomImageGetter)
    assert g._width == 800
    assert g._height == 600


def test_client_can_create_image_from_user_getter():
    c = PyUnsplashSourceClient(**defaults)
    g = c.image_from_user('usrName')
    assert isinstance(g, ImageFromUserGetter)
    assert g._width == 800
    assert g._height == 600
