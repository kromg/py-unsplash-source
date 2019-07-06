#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vim: se et ts=4 syn=python:

#
# get_random_image.py
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

from py_unsplash_source.getters import RandomImageGetter

# Search for an image
ig = (RandomImageGetter()
      .geometry(1920, 1080)             # Optional
      .search('python, programing')     # Optional
      )

image = ig.get()
image.save_as('image.jpg')

# Get the daily image
ig = (RandomImageGetter()
      .geometry(1920, 1080)             # Optional
      .search('programming')
      .daily()
      )

image = ig.get()
image.save_as('daily.jpg')

# Get the weekly image
ig = (RandomImageGetter()
      .geometry(1920, 1080)             # Optional
      .search('programming')
      .weekly()
      )

image = ig.get()
image.save_as('weekly.jpg')
