# PyNEST implementation of the cortical microcircuit model 

## Installation

[TODO: revise]

The PyNEST implementation of the model is contained in `microcircuit-PD14-model/PyNEST`:
  ```bash
  cd PyNEST
  ```

We recommend installing the python package inside a python environment:
- Create a python environment
  ```bash
  python -m venv venv
  ```
- Activate the python environment:
  ```
  source venv/bin/activate
  ```

The `microcircuit` python package can be installed using:
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

- docopt-ng, matplotlib, numpy, psutil, ruamel.yaml (handled by python package dependencies)

## Hardware requirements

[TODO: check and revise numbers]

| `N_scaling`=`K_scaling`   | Memory    |
|---------------------------|--------|
| 0.1 (default)             |  484 MB |
| 0.2                       | 1116 MB |
| 0.5                       | 4382 MB |
| 1                         |   16 GB? |

## Implementation details

This implementation uses the [`iaf_psc_exp`](https://nest-simulator.readthedocs.io/en/stable/models/iaf_psc_exp.html) neuron and the [`static_synapse`](https://nest-simulator.readthedocs.io/en/stable/models/static_synapse.html) synapse models provided in [NEST]. 
The network is connected according to the [`fixed_total_number`](https://nest-simulator.readthedocs.io/en/stable/synapses/connectivity_concepts.html#random-fixed-total-number) connection rule in NEST. 
The neuron dynamics is integrated in a time-driven manner using exact integration with a simulation step size `sim_resolution` ([Rotter & Diesmann (1999)]).

The PyNEST implementation runs with [NEST 3.6](https://github.com/nest/nest-simulator.git)

### Simulation parameters (defaults)

| Name             | Value            | Description                                                  |
|------------------|------------------|--------------------------------------------------------------|
| `sim_resolution` | 0.1 ms           | simulation time resolution (duration of one simulation step) |
| `t_presim`       | 500 ms           | duration of pre-simulation phase (warm-up)                   |
| `t_sim`          | 1000 ms          | duration of simulation phase                                 |
| `rec_dev`        | `spike_recorder` | recording device                                             |

## References

[Rotter & Diesmann (1999)]: #Rotter99_381
<a name="Rotter99_381"></a>
* [Rotter & Diesmann (1999). Exact digital simulation of time-invariant linear systems with applications to neuronal modeling. Biological Cybernetics 81(5-6):381-402. doi:10.1007/s004220050570](https://doi.org/10.1007/s004220050570)

[NEST]: #NEST
<a name="NEST"></a>
* [Villamar et al. (2023). NEST 3.6 (3.6). Zenodo. doi:10.5281/zenodo.8344932](https://doi.org/10.5281/zenodo.8344932)

License
-------

This project is licensed under GNU General Public License v2.0 or later.
See LICENSE for details.

```
SPDX-License-Identifier: GPL-2.0-or-later
SPDX-Copyright: 2025, Forschungszentrum Jülich GmbH, Jülich, Germany
SPDX-Author: Bender Bending Rodríguez <t.tetzlaff@fz-juelich.de, j.senk@fz-juelich.de>
```
