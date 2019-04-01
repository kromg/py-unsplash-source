#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# prototype.py
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

from py_unsplash_source import PyUnsplashSourceClient

su = PyUnsplashSourceClient(width=800, height=600)

# Random √
image = (su.random_getter()
         .width(1920)
         .height(1080)
         .daily()
         .search('nature,landscape')).get()

image.save_as('/tmp/random.jpg')

# Random from a specific user √
image = (su.user_item_getter('gangdise')
         .from_likes()
         .width(1920)
         .height(1080)).get()

image.save_as('/tmp/user.jpg')

# Random from a collection √
image = (su.collection_item_getter(145698)
         .width(1920)
         .height(1080)).get()

image.save_as('/tmp/collection.jpg')

# # Random from featured collection √
image = (su.featured_getter()
         .width(1920)
         .height(1080)
         .search('nature,landscape', 'sunset')).get()

image.save_as('/tmp/featured.jpg')

# Speficic image √
image = (su.item_getter("WLUHO9A_xik")
         .width(1920)
         .height(1080)).get()

image.save_as('/tmp/item.jpg')

