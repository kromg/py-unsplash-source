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

su = PyUnsplashSourceClient()

# Random √
image = su.random_getter(
    width=123,  # optional
    height=234,  # optional
    update="UpdateFrequency",  # Optional - From enum: UpdateFrequency
    search="search,terms"  # Optional - append search terms
).get()

image.save_as('/tmp/random.jpg')

# Random from a specific user √
image = su.user_item_getter(
    user="name",
    width=123,  # optional
    height=234,  # optional
    from_likes=True,  # Default: false - get from user likes
    update="UpdateFrequency",  # Optional - From enum: UpdateFrequency
    search="search,terms"  # Optional - append search terms
).get()

image.save_as('/tmp/user.jpg')

# Random from a collection √
image = su.collection_item_getter(
    id=145698,
    width=123,  # optional
    height=234,  # optional
    update="UpdateFrequency",  # Optional - From enum: UpdateFrequency
    search="search,terms"  # Optional - append search terms
).get()

image.save_as('/tmp/collection.jpg')

# Random from featured collection √
image = su.featured_getter(
    width=123,  # optional
    height=234,  # optional
    update="UpdateFrequency",  # Optional - From enum: UpdateFrequency
    search="search,terms"  # Optional - append search terms
).get()

image.save_as('/tmp/featured.jpg')

# Speficic image √
image = su.item_getter(
    id="WLUHO9A_xik",
    width=123,  # optional
    height=234,  # optional
).get()

image.save_as('/tmp/item.jpg')


# Notes:
#   - each *_getter will produce a "getter" object, capable of downloading one image each tmie get() is called
#   - each call to get() will return an "image" object, capable of saving data to some file (and maybe capable of
#       manipulating exif data or something of this sort?)
#   - hierarchy:
#       BaseGetter (width, height)
#           |- RandomGetter (search & Frequency)
#           |   |- FeaturedGetter
#           |   |- CollectionGetter
#           |- SingleItemGetter
# 