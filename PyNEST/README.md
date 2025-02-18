# PyNEST implementation of the cortical microcircuit model 

# Simulation scripts

## Downscaled
See [model.py](model.py) and [parameter_dicts.py](parameter_dicts.py)

## Full-scaled
[INSERT FULL-SCALED MODEL]

# Simulation details

By default, this implementation is based on the [`iaf_psc_exp`](https://nest-simulator.readthedocs.io/en/v3.6/models/iaf_psc_exp.html) neuron and the [`static_synapse`](https://nest-simulator.readthedocs.io/en/v3.6/models/static_synapse.html) synapse models provided in [NEST].

The network is connected according to the [`fixed_total_number`](https://nest-simulator.readthedocs.io/en/v3.6/synapses/connection_management.html#rule-fixed-total-number) connection rule in NEST.

The model implementation runs with [NEST 3.6](https://github.com/nest/nest-simulator.git)

## Architecture dependencies

* The full microcircuit requires approximately 16 GB of RAM.

[TODO table with memory consumption for different scales]

## Software dependencies

* NEST 3
* Python 3
* numpy
* matplotlib - if provided plotting routines ares used

## Simulation parameters
| Name | Value | Description |
|--|--|--|
| $`N_{\mathrm{scaling}}`$ | $`0.1`$| scaling of number of neurons, 1 correspondes to full-scale model |
| $`K_{\mathrm{scaling}}`$ | $`0.1`$| scaling of number of synapses. 1 correspondes to full-scale model |
| $`t_{\mathrm{presim}}`$ | $`500\,\mathrm{ms}`$| duration of pre-simulation phase |
| $`t_{\mathrm{sim}}`$ | $`1000\,\mathrm{ms}`$| duration of simulation phase |

## References

[Potjans & Diesmann (2014), The cell-type specific cortical microcircuit: relating structure and activity in a full-scale spiking network model, Cerebral Cortex 24(3):785–806, https://doi.org/10.1093/cercor/bhs358](https://doi.org/10.1093/cercor/bhs358)

[van Albada, Rowley, Senk, Hopkins, Schmidt, Stokes, Lester, Diesmann, & Furber (2018), Performance comparison of the digital neuromorphic hardware SpiNNaker and the neural network simulation software NEST for a full-scale cortical microcircuit model, Front. Neurosci. 12:291, doi:10.3389/fnins.2018.00291](https://doi.org/10.3389/fnins.2018.00291)
