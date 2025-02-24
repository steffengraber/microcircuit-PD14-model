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
- NumPy
- SciPy
- Matplotlib (optional)

## Hardware requirements

[TODO: check and revise numbers]

| `N_scaling`=`K_scaling`   | RAM    |
|---------------------------|--------|
| 0.1 (default)             |  484MB |
| 0.5                       | 4382MB |
| 1                         | 16GB ?  |

## Implementation details

[TODO: revise]

This implementation uses the [`iaf_psc_exp`](https://nest-simulator.readthedocs.io/en/v3.6/models/iaf_psc_exp.html) neuron and the [`static_synapse`](https://nest-simulator.readthedocs.io/en/v3.6/models/static_synapse.html) synapse models provided in [NEST]. The network is connected according to the [`fixed_total_number`](https://nest-simulator.readthedocs.io/en/v3.6/synapses/connection_management.html#rule-fixed-total-number) connection rule in NEST. The neuron dynamics is propagated in time using exact integration ([Rotter & Diesmann (1999)]) with a simulation step size `sim_resolution`.

The PyNEST implementation runs with [NEST 3.6](https://github.com/nest/nest-simulator.git)

### Simulation parameters

[TODO: revise/check table; use default parameters (see sim_params.py)]

| Name | Value | Description |
|--|--|--|
| `sim_resolution` | $`0.1\,\text{ms}`$ | simulation time resolution (duration of one simulation step) |
| `tics_per_step` | $`???`$ | number of tics per simulation step `sim_resolution` (time resolution) |
| `t_presim` | $`500\,\text{ms}`$| duration of pre-simulation phase |
| `t_sim` | $`1000\,\text{ms}`$| duration of simulation phase |
| `local_num_threads` | $`4`$ | local number of threads per MPI process |
| `rec_V_int` | $`1\,\text{ms}`$ | recording interval of the membrane potential |
| `rng_seed` | $`55`$ | Seed for NEST |

## Benchmarking strategies

[TODO]

## Testing

[TODO]

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
