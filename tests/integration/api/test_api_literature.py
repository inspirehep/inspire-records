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

from inspire_records.api import LiteratureRecord

from helpers.factories.models.invenio_records import RecordMetadataFactory


def test_base_get_record(base_app, db):
    record = RecordMetadataFactory()

    expected_record = LiteratureRecord.get_record(record.id)

    assert expected_record == record.json


def test_base_get_records(base_app, db):
    records = RecordMetadataFactory.create_batch(20)
    record_uuids = [record.id for record in records]

    expected_records = LiteratureRecord.get_records(record_uuids)

    for record in records:
        assert record.json in expected_records
