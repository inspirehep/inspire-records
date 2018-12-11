..
    This file is part of INSPIRE.
    Copyright (C) 2014-2018 CERN.

    INSPIRE is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    INSPIRE is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with INSPIRE. If not, see <http://www.gnu.org/licenses/>.

    In applying this license, CERN does not waive the privileges and immunities
    granted to it by virtue of its status as an Intergovernmental Organization
    or submit itself to any jurisdiction.


=================
 inspire-records
=================

.. image:: https://travis-ci.org/inspirehep/inspire-records.svg?branch=master
    :target: https://travis-ci.org/inspirehep/inspire-records

.. image:: https://coveralls.io/repos/github/inspirehep/inspire-records/badge.svg?branch=master
    :target: https://coveralls.io/github/inspirehep/inspire-records?branch=master


About
=====

INSPIRE module that adds more fun to the platform.

Style Guide
===========

* ``Napoleon`` https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html for docstrings
* ``Black`` https://github.com/ambv/black


Install ``Black`` pre-commit:
-----------------------------

.. code-block:: console

    $ pre-commit install


Tests
=====

.. code-block:: console

    $ docker-compose -f docker-compose.test.yml build 
    $ docker-compose -f docker-compose.test.yml run --rm tests py.test tests/unit
    $ docker-compose -f docker-compose.test.yml run --rm tests py.test tests/integration

Run a specific test
-------------------

.. code-block:: console

    $ docker-compose -f docker-compose.test.yml exec tests pytest tests/integration/api/test_api_base.py --pdb -s