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

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from helpers import check_empty, download_file


class SpreadsheetClient:
    def __init__(self, JSON_KEYFILE_NAME, SPREADSHEET_URL):
        scope = ["https://spreadsheets.google.com/feeds"]
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(
            JSON_KEYFILE_NAME, scope
        )

        self.gc = gspread.authorize(credentials)
        self.data = self.gc.open_by_url(SPREADSHEET_URL)

        self.worksheets = self.data.worksheets()
        self.dashboard = self.worksheets.pop(0)
        self.project_names = [p.title for p in self.worksheets]
        self.last_project = self.dashboard.acell("A1").value
        self.current_project_idx = 0
        self.current_project_idx = self.project_names.index(self.last_project) + 1

        if self.current_project_idx >= len(self.project_names):
            self.current_project_idx = 0

    def get_cast(self):
        self.candidate = "%s" % self.project_names[self.current_project_idx]
        p = self.data.worksheet(self.candidate)
        tmp = p.find("last")
        row = tmp.row + 1
        cast_msg = p.cell(row, 1).value
        if check_empty(cast_msg):
            row = 1
        if row == 1:
            cast_msg = p.cell(row, 1).value

        cast_media = p.cell(row, 3).value
        local_filename = None
        if not check_empty(cast_media):
            local_filename = download_file(cast_media)

        p.update_cell(tmp.row, 2, "")
        p.update_cell(row, 2, "last")

        # Rotate sheets
        self.dashboard.update_acell("A1", p.title)
        return (cast_msg, local_filename)
