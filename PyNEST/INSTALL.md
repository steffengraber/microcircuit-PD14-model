
# PyNEST implementation of the cortical microcircuit model of Potjans & Diesmann (2014)

[TODO: NEST requirement, link to NEST installation page: https://nest-simulator.readthedocs.io/en/stable/installation/index.html]

- cloning the project
  ```bash
  git clone git@github.com:INM-6/microcircuit-PD14-model.git
  ```
- the PyNEST implementation is contained in the PyNEST folder:
  ```bash
  cd PyNEST
  ```

- option 1: using the python package
  +  create a python environment
  ```bash
  python -m venv venv
  ```
  + activate the python environment
  ```
  source venv/bin/activate
  ```
  + install the python package
  ```bash
  pip install -U pip
  pip install .
  ```
  + you can now import the python package `microcircuit` in your python applications (irrespective of your current working folder)
  ```python
  import microcircuit
  ```

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
pytest microcircuit
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
