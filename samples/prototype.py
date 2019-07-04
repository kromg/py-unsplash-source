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
image = (su.random_image()
         .geometry(1920, 1080)
         .daily()
         .search('nature,landscape')).get()

image.save_as('/tmp/random.jpg')

# Random from a specific user √
image = (su.image_from_user('gangdise')
         .from_likes()
         .geometry(1920, 1080)).get()

image.save_as('/tmp/user.jpg')

# Random from a collection √
image = (su.image_from_collection(145698)
         .geometry(1920, 1080)).get()

image.save_as('/tmp/collection.jpg')

# # Random from featured collection √
image = (su.image_from_featured()
         .geometry(1920, 1080)
         .search('nature,landscape', 'sunset')).get()

image.save_as('/tmp/featured.jpg')

# Speficic image √
image = (su.image("WLUHO9A_xik")
         .geometry(1920, 1080)).get()

image.save_as('/tmp/item.jpg')

