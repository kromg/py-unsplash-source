#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# test_user_item_getter.py
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

from py_unsplash_source.getters.user_item_getter import UserItemGetter
from py_unsplash_source.getters.random_getter import RandomGetter
from py_unsplash_source.getters.base_getter import BaseGetter, DownloadException
from py_unsplash_source.getters.reload_frequency import ReloadFrequency

import pytest


# ------------------------ without likes --------------------------------------

def test_user_item_getter_with_defaults():
    uig = UserItemGetter('someName')
    assert uig is not None
    assert isinstance(uig, (UserItemGetter, RandomGetter, BaseGetter))


def test_user_item_build_url():
    uig = UserItemGetter('usrName')
    assert uig._build_url() == '/user/usrName'


def test_user_item_build_url_with_geometry():
    uig = UserItemGetter("usrName").width(800).height(600)
    assert uig._build_url() == '/user/usrName/800x600'


def test_user_item_build_url_with_searches():
    uig = UserItemGetter('usrName').search('some, random , string')
    assert uig._build_url() == '/user/usrName?random,some,string'


def test_user_item_build_url_with_reload_freq():
    uig = UserItemGetter('usrName').daily()
    assert uig._build_url() == '/user/usrName/daily'


def test_user_item_build_url_with_all():
    uig = (UserItemGetter('usrName')
           .width(800)
           .height(600)
           .search('random, search,string')
           .weekly()
           )
    assert uig._build_url() == '/user/usrName/800x600/weekly?random,search,string'


@pytest.mark.skip('need to mock a server or to mock requests')
def test_get_raises_on_failure():
    with pytest.raises(DownloadException):
        UserItemGetter('usrName').get()


# ------------------------ with likes --------------------------------------

def test_user_item_getter_likes_with_defaults():
    uig = UserItemGetter('someName').from_likes()
    assert uig is not None
    assert isinstance(uig, (UserItemGetter, RandomGetter, BaseGetter))


def test_user_item_likes_build_url():
    uig = UserItemGetter('usrName').from_likes()
    assert uig._build_url() == '/user/usrName/likes'


def test_user_item_likes_build_url_with_geometry():
    uig = UserItemGetter("usrName").from_likes().width(800).height(600)
    assert uig._build_url() == '/user/usrName/likes/800x600'


def test_user_item_likes_build_url_with_searches():
    uig = UserItemGetter('usrName').from_likes().search('some, random , string')
    assert uig._build_url() == '/user/usrName/likes?random,some,string'


def test_user_item_likes_build_url_with_reload_freq():
    uig = UserItemGetter('usrName').from_likes().daily()
    assert uig._build_url() == '/user/usrName/likes/daily'


def test_user_item_likes_build_url_with_all():
    uig = (UserItemGetter('usrName')
           .from_likes()
           .width(800)
           .height(600)
           .search('random, search,string')
           .weekly()
           )
    assert uig._build_url() == '/user/usrName/likes/800x600/weekly?random,search,string'


@pytest.mark.skip('need to mock a server or to mock requests')
def test_get_raises_on_failure():
    with pytest.raises(DownloadException):
        UserItemGetter('usrName').from_likes().get()
