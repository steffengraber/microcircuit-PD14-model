# Cortical microcircuit model (Potjans & Diesmann, 2012)
[![www.python.org](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org) <a href="http://www.nest-simulator.org"> <img src="https://github.com/nest/nest-simulator/blob/master/doc/logos/nest-simulated.png" alt="NEST simulated" width="50"/></a> [![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Overview

The model of a cortical microcircuit proposed by Potjans and Diesmann (2014) describes the neuronal circuitry under ~1 mm$`^2`$ cortical surface. The network consists of 4 cortical layers (L2/3, L4, L5, L6), each being represented by a randomly connected network of excitatory and inhibitory point neurons. 
The network connectivity is derived from anatomical and electrophysiological data.
Connection probabilities between neurons in the network are highly specific and depend on the cell type (excitatory, inhibitory) and on the locations (cortical layers) of the pre- and postsynaptic neurons.
In contrast to this high specificity in the connectivity, all neurons in the network are identical and share the same dynamics and parameters, irrespective of their type and location.
Similarly, all synapses are described by an identical dynamics, and differ only in the synaptic weight and spike-transmission latencies.
Synaptic weights and spike transmission latencies are randomly drawn from distributions which depend only on the type of the presynaptic neuron (excitatory or inhibitory), but are otherwise identical for all neurons and connections (with one exception).
In addition to inputs from the local network, neurons receive external inputs representing thalamic afferents and cortico-cortical inputs from more distant cortical regions. The original purpose of this model was to understand the relationship between the connectivity and the activity within the local cortical network. Spefically, the model demonstrates that the observed cell-type and layer specificity of in-vivo firing rates is largely explained by the specificity in the number of connections between subpopulations, rather than by differences in single neuron or synapse dynamics.

|  |  |  |
|--|--|--|
| <img src="figures/potjans_2014_microcircuit.png" width="400"/> | <img src="figures/potjans_2014_raster_plot.png" width="400"/> | <img src="figures/potjans_2014_box_plot.png" width="400"/> |

*Network sketch (left), spiking activity (middle), and distributions of time averaged single neuron firing rates (right) of the cortical microcircuit model. Adapted from (van Albada et al., 2018)*


## Model description
See [`doc/ModelDescription_CorticalMicrocircuit_PotjansDiesmann.pdf`](doc/ModelDescription_CorticalMicrocircuit_PotjansDiesmann.pdf)

## Available implementations
* PyNEST ([README](PyNEST/README.md), [code](PyNEST/model.py))

## References

[Potjans & Diesmann (2014). The cell-type specific cortical microcircuit: relating structure and activity in a full-scale spiking network model. Cerebral Cortex, 24(3), 785-806.](https://doi.org/10.1093/cercor/bhs358)

[van Albada et al. (2018). Performance Comparison of the Digital Neuromorphic Hardware SpiNNaker and the Neural Network Simulation Software NEST for a Full-Scale Cortical Microcircuit Model. Front. Neurosci. 12:291.](https://doi.org/10.3389/fnins.2018.00291)
