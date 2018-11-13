# -*- coding: utf-8 -*-
#
# This file is part of INSPIRE.
# Copyright (C) 2014-2018 CERN.
#
# INSPIRE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# INSPIRE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with INSPIRE. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""INSPIRE module that adds more fun to the platform."""

from __future__ import absolute_import, division, print_function

import pytest
import random

from faker import Faker
from faker.providers import BaseProvider

from inspire_schemas.api import validate as schema_validate

fake = Faker()

USED_RECIDS = {}
MAX_ES_INT = 2147483647
MAX_RANDOMIZE_TRIES = 100


def get_next_free_recid():
    next_recid_candidate = random.randint(1, MAX_ES_INT)
    cur_try = 0
    while next_recid_candidate in USED_RECIDS and cur_try < MAX_RANDOMIZE_TRIES:
        next_recid_candidate = random.randint(1, MAX_ES_INT)
        cur_try += 1

    if cur_try >= MAX_RANDOMIZE_TRIES:
        raise Exception(
            "Unable to find a non-used record id, tried %d times." % cur_try
        )

    reserve_recid(next_recid_candidate)
    return next_recid_candidate


def reserve_recid(recid):
    USED_RECIDS[recid] = True


def cleanup():
    global USED_RECIDS
    USED_RECIDS = {}


class RecordProvider(BaseProvider):
    def control_number(self):
        return get_next_free_recid()

    def record(self, data=None, with_control_number=False):
        record = {
            "$schema": "http://localhost:5000/schemas/records/hep.json",
            "titles": [{"title": fake.sentence()}],
            "document_type": ["article"],
            "_collections": ["Literature"],
        }
        if with_control_number:
            record["control_number"] = self.control_number()
        if data:
            record.update(data)
        schema_validate(record)
        return record
