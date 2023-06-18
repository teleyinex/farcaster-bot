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

import os
from base64 import b64decode
import json
from dotenv import load_dotenv
from spreadsheet import SpreadsheetClient
from farcaster import Warpcast

load_dotenv()
GOOGLE_AUTH = b64decode(os.environ["GOOGLE_AUTH"].encode("ascii")).decode("ascii")
GOOGLE_AUTH = json.loads(GOOGLE_AUTH)
URL = os.environ["URL"]
FARCASTER_MNEMONIC = os.environ["FARCASTER_MNEMONIC"]

s_client = SpreadsheetClient(GOOGLE_AUTH, URL)

cast_msg, local_filename = s_client.get_cast()

client = Warpcast(mnemonic=FARCASTER_MNEMONIC)

client.post_cast(text=cast_msg)
