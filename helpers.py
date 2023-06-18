# -*- coding: utf8 -*-
# This file is part of farcaster-bot.
#
# Copyright (C) 2023 Daniel Lombraña González.
#
# farcaster-bot is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# farcaster-bot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with farcaster-bot.  If not, see <http://www.gnu.org/licenses/>.
import requests


def check_empty(value):
    return value is None or value == ""


def download_file(url):
    local_filename = "/tmp/" + url.split("/")[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename
