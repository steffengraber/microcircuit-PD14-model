
# PyNEST implementation of the cortical microcircuit model of Potjans & Diesmann (2014)


Installation
------------

It is recommended to install the package into an environment. For example
using Python `venv` could be done as follows:

```bash
python -m venv venv
source venv/bin/activate
pip install -U pip
pip install .
```

Development and Testing
-----------------------

To install in development mode use

```bash
pip install -e .[dev]
```

in the cloned repository instead of the last line in the normal installation
procedure.

To run the test suite type

```bash
pytest microcircuit-PD14-model
```


License
-------

This project is licensed under GNU General Public License v2.0 or later.
See LICENSE for details.

```
SPDX-License-Identifier: GPL-2.0-or-later
SPDX-Copyright: 2025, Forschungszentrum Jülich GmbH, Jülich, Germany
SPDX-Author: Bender Bending Rodríguez <t.tetzlaff@fz-juelich.de, j.senk@fz-juelich.de>
```
