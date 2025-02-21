# PyNEST implementation of the cortical microcircuit model 

## Installation

[TODO: revise]

- cloning the project
  ```bash
  git clone git@github.com:INM-6/microcircuit-PD14-model.git
  ```
- the PyNEST implementation is contained in the PyNEST folder:
  ```bash
  cd PyNEST
  ```

- we recommend installing the python package inside a specific python environment
  +  create a python environment
  ```bash
  python -m venv venv
  ```
  + activate the python environment
  ```
  source venv/bin/activate
  ```
- install the python package
  ```bash
  pip install -U pip
  pip install .
  ```

## Usage

You can now import the python package `microcircuit` in your python applications

```python
import microcircuit
```
See also [example](examples/run_microcircuit.py).
  
## Software requirements

- NEST 3.x (tested on NEST 3.8; see [NEST installation](https://nest-simulator.readthedocs.io/en/stable/installation))
- Python 3.x (tested on Python 3.10)
- NumPy
- SciPy
- Matplotlib (optional)

## Hardware requirements

[TODO: check and revise numbers]

| Scale         | RAM   |
|---------------|-------|
| 0.1 (default) | 567MB |
| 1             | 16GB  |

## Implementation details

[TODO: revise]

By default, this implementation is based on the [`iaf_psc_exp`](https://nest-simulator.readthedocs.io/en/v3.6/models/iaf_psc_exp.html) neuron and the [`static_synapse`](https://nest-simulator.readthedocs.io/en/v3.6/models/static_synapse.html) synapse models provided in [NEST].

The network is connected according to the [`fixed_total_number`](https://nest-simulator.readthedocs.io/en/v3.6/synapses/connection_management.html#rule-fixed-total-number) connection rule in NEST.

The model implementation runs with [NEST 3.6](https://github.com/nest/nest-simulator.git)

### Simulation parameters

[TODO: revise table with default parameters (see sim_params.py); add simulation time resolution, number of threads, seed,...]

| Name | Value | Description |
|--|--|--|
| $`N_{\mathrm{scaling}}`$ | $`0.1`$| scaling of number of neurons, 1 correspondes to full-scale model |
| $`K_{\mathrm{scaling}}`$ | $`0.1`$| scaling of number of synapses. 1 correspondes to full-scale model |
| $`t_{\mathrm{presim}}`$ | $`500\,\mathrm{ms}`$| duration of pre-simulation phase |
| $`t_{\mathrm{sim}}`$ | $`1000\,\mathrm{ms}`$| duration of simulation phase |

## Benchmarking strategies

[TODO]

## Testing

[TODO]

## References

[TODO: NEST refs]

License
-------

This project is licensed under GNU General Public License v2.0 or later.
See LICENSE for details.

```
SPDX-License-Identifier: GPL-2.0-or-later
SPDX-Copyright: 2025, Forschungszentrum Jülich GmbH, Jülich, Germany
SPDX-Author: Bender Bending Rodríguez <t.tetzlaff@fz-juelich.de, j.senk@fz-juelich.de>
```
