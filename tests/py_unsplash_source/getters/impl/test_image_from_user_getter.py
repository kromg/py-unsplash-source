#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# test_image_from_user_getter.py
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

from py_unsplash_source.getters.impl.image_from_user_getter import ImageFromUserGetter
from py_unsplash_source.getters.impl.random_image_getter import RandomImageGetter
from py_unsplash_source.getters.base_getter import BaseGetter, DownloadException

import pytest


# ------------------------ without likes --------------------------------------

def test_image_from_user_getter_with_defaults():
    uig = ImageFromUserGetter('someName')
    assert uig is not None
    assert isinstance(uig, (ImageFromUserGetter, RandomImageGetter, BaseGetter))


def test_image_from_user_build_url():
    uig = ImageFromUserGetter('usrName')
    assert uig._build_url() == '/user/usrName'


def test_image_from_user_build_url_with_geometry():
    uig = ImageFromUserGetter("usrName").geometry(800, 600)
    assert uig._build_url() == '/user/usrName/800x600'


def test_image_from_user_build_url_with_searches():
    uig = ImageFromUserGetter('usrName').search('some, random , string')
    assert uig._build_url() == '/user/usrName?random,some,string'


def test_image_from_user_build_url_with_reload_freq():
    uig = ImageFromUserGetter('usrName').daily()
    assert uig._build_url() == '/user/usrName/daily'


def test_image_from_user_build_url_with_all():
    uig = (ImageFromUserGetter('usrName')
           .geometry(800, 600)
           .search('random, search,string')
           .weekly()
           )
    assert uig._build_url() == '/user/usrName/800x600/weekly?random,search,string'


@pytest.mark.skip('need to mock a server or to mock requests')
def test_get_raises_on_failure():
    with pytest.raises(DownloadException):
        ImageFromUserGetter('usrName').get()


# ------------------------ with likes --------------------------------------

def test_image_from_user_getter_likes_with_defaults():
    uig = ImageFromUserGetter('someName').from_likes()
    assert uig is not None
    assert isinstance(uig, (ImageFromUserGetter, RandomImageGetter, BaseGetter))


def test_image_from_user_likes_build_url():
    uig = ImageFromUserGetter('usrName').from_likes()
    assert uig._build_url() == '/user/usrName/likes'


def test_image_from_user_likes_build_url_with_geometry():
    uig = ImageFromUserGetter("usrName").from_likes().geometry(800, 600)
    assert uig._build_url() == '/user/usrName/likes/800x600'


def test_image_from_user_likes_build_url_with_searches():
    uig = (ImageFromUserGetter('usrName')
           .from_likes()
           .search('some, random , string'))        # Ignored
    assert uig._build_url() == '/user/usrName/likes'


def test_image_from_user_likes_build_url_with_reload_freq():
    uig = (ImageFromUserGetter('usrName')
           .from_likes()
           .daily())        # Ignored
    assert uig._build_url() == '/user/usrName/likes'


def test_image_from_user_likes_build_url_with_all():
    uig = (ImageFromUserGetter('usrName')
           .from_likes()
           .geometry(800, 600)
           .search('random, search,string')     # Ignored
           .weekly()                            # Ignored
           )
    assert uig._build_url() == '/user/usrName/likes/800x600'


@pytest.mark.skip('need to mock a server or to mock requests')
def test_get_raises_on_failure():
    with pytest.raises(DownloadException):
        ImageFromUserGetter('usrName').from_likes().get()
