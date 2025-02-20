# PyNEST implementation of the cortical microcircuit model 

## Implementation details

[TODO: revise]

By default, this implementation is based on the [`iaf_psc_exp`](https://nest-simulator.readthedocs.io/en/v3.6/models/iaf_psc_exp.html) neuron and the [`static_synapse`](https://nest-simulator.readthedocs.io/en/v3.6/models/static_synapse.html) synapse models provided in [NEST].

The network is connected according to the [`fixed_total_number`](https://nest-simulator.readthedocs.io/en/v3.6/synapses/connection_management.html#rule-fixed-total-number) connection rule in NEST.

The model implementation runs with [NEST 3.6](https://github.com/nest/nest-simulator.git)

## Simulation parameters

[TODO: revise table; add simulation time resolution, number of threads, seed,...]

| Name | Value | Description |
|--|--|--|
| $`N_{\mathrm{scaling}}`$ | $`0.1`$| scaling of number of neurons, 1 correspondes to full-scale model |
| $`K_{\mathrm{scaling}}`$ | $`0.1`$| scaling of number of synapses. 1 correspondes to full-scale model |
| $`t_{\mathrm{presim}}`$ | $`500\,\mathrm{ms}`$| duration of pre-simulation phase |
| $`t_{\mathrm{sim}}`$ | $`1000\,\mathrm{ms}`$| duration of simulation phase |

## Installation

See [INSTALL.md](INSTALL.md).

## Software dependencies

[TODO: revise]

* NEST 3
* Python 3
* numpy
* matplotlib - if provided plotting routines ares used

## Hardware requirements

[TODO table with memory consumption for different scales]

* The full microcircuit requires approximately 16 GB of RAM.

## Usage

[TODO: revise]

See [example](examples/run_microcircuit.py).

## References

[TODO: NEST refs]

