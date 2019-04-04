#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# unsplash_endpoint.py
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


class UnsplashEndpoint:

    def __init__(self,
                 protocol: str = 'https',
                 host: str = 'source.unsplash.com',
                 port: int = None):
        self.protocol = protocol
        self.host = host
        self.port = port

    def __str__(self):
        return '{}://{}{}'.format(
            self.protocol,
            self.host,
            ':{}'.format(self.port) if self.port else ''
        )
