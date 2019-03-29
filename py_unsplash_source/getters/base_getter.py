#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# BaseGetter
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

from abc import ABC, abstractmethod


class BaseGetter(ABC):
    """Base class from which all getters must be derived. It handles the basic information to fetch an image."""

    def __init__(self,
                 protocol='https',
                 host='source.unsplash.com',
                 port=443,
                 width=None,
                 height=None):
        # TODO: document this
        self.protocol = protocol
        self.host = host
        self.port = port

        self.width = width
        self.height = height

    @abstractmethod
    def _build_url(self):
        """This method must be implemented by each derived getter and it must return the url to be fetched
         as a string"""
        # TODO: enhance docstring with params and returns
        pass

    def get(self):
        """Fetch an image per configuration of this getter. Returns a FetchedImage instance"""
        # TODO: enhance docstring with params and returns
        pass
