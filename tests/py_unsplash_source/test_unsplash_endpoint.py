#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# test_unsplash_endpoint
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

from py_unsplash_source.unsplash_endpoint import UnsplashEndpoint


def test_default_endpoint():
    s = UnsplashEndpoint()
    assert s.protocol == 'https'
    assert s.host == 'source.unsplash.com'
    assert s.port is None

    assert str(s) == 'https://source.unsplash.com'


def test_custom_endpoint():
    s = UnsplashEndpoint(protocol='http', host='test', port=80)

    assert s.protocol == 'http'
    assert s.host == 'test'
    assert s.port == 80

    assert str(s) == 'http://test:80'
