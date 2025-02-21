# Cortical microcircuit model (Potjans & Diesmann, 2014)
[![www.python.org](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org) 
<a href="http://www.nest-simulator.org"> <img src="https://github.com/nest/nest-simulator/blob/master/doc/logos/nest-simulated.png" alt="NEST simulated" width="50"/></a> 
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## Overview

The model of a cortical microcircuit proposed by Potjans and Diesmann (2014) describes the neuronal circuitry under ~1 mm$`^2`$ cortical surface. The network consists of 4 cortical layers (L2/3, L4, L5, L6), each being represented by a randomly connected network of excitatory and inhibitory point neurons. 
The network connectivity is derived from anatomical and electrophysiological data.
Connection probabilities between neurons in the network are highly specific and depend on the cell type (excitatory, inhibitory) and on the locations (cortical layers) of the pre- and postsynaptic neurons.
In contrast to this high specificity in the connectivity, all neurons in the network are identical and share the same dynamics and parameters, irrespective of their type and location.
Similarly, all synapses are described by an identical dynamics, and differ only in the synaptic weight and spike-transmission latencies.
Synaptic weights and spike transmission latencies are randomly drawn from distributions which depend only on the type of the presynaptic neuron (excitatory or inhibitory), but are otherwise identical for all neurons and connections (with one exception).
In addition to inputs from the local network, neurons receive external inputs representing thalamic afferents and cortico-cortical inputs from more distant cortical regions. 

The original purpose of this model was to understand the relationship between the connectivity and the spiking activity within local cortical circuits. Specifically, the model demonstrates that the observed cell-type and layer specificity of in-vivo firing rates is largely explained by the specificity in the number of connections between cortical subpopulations, and doesn't require a specificity in single neuron or synapse dynamics.

|  |  |  |
|--|--|--|
| <img src="figures/potjans_2014_microcircuit.png" width="300"/> | <img src="figures/potjans_2014_raster_plot.png" width="400"/> | <img src="figures/potjans_2014_box_plot.png" width="400"/> |

*Sketch of the cortical microcircuit model (left), spiking activity (middle) and distributions of time averaged single-neuron firing rates across neurons in each subpopulation (right). Adapted from (van Albada et al., 2018)*

In recent years, the model became an established Computational Neuroscience benchmark for various soft- and hardware architectures (van Albada et al., 2018; Jordan et al., 2018; Rhodes et al., 2020; Dasbach et al., 2021; Albers et al., 2022; Kurth et al., 2022; Heittmann et al., 2022; Pronold et al., 2022; Pronold et al., 2022; Golosio et al., 2023; Kauth et al., 2023; Schmidt et al., 2024).

## Model description

A detailed mathematical, implementation agnostic description of the model and its parameters is provided [here](doc/ModelDescription_microcircuit-PD14-model.pdf).

## Model implementations
* [PyNEST](PyNEST/README.md)

## Repository Contents

[TODO]

## References

[Potjans & Diesmann (2014). The cell-type specific cortical microcircuit: relating structure and activity in a full-scale spiking network model. Cerebral Cortex, 24(3), 785-806.](https://doi.org/10.1093/cercor/bhs358)

[van Albada et al. (2018). Performance Comparison of the Digital Neuromorphic Hardware SpiNNaker and the Neural Network Simulation Software NEST for a Full-Scale Cortical Microcircuit Model. Front. Neurosci. 12:291.](https://doi.org/10.3389/fnins.2018.00291)

[Jordan et al. (2018). Extremely scalable spiking neuronal network simulation code: from laptops to exascale computers. Frontiers in Neuroinformatics, 12, 317068.](https://doi.org/10.3389/fninf.2018.00002)

[Rhodes et al. (2020). Real-time cortical simulation on neuromorphic hardware. Philosophical Transactions of the Royal Society A, 378(2164), 20190160.](https://doi.org/10.1098/rsta.2019.0160)

[Dasbach et al. (2021). Dynamical characteristics of recurrent neuronal networks are robust against low synaptic weight resolution. Frontiers in Neuroscience, 15, 757790.](https://doi.org/10.3389/fnins.2021.757790)

[Albers et al. (2022). A modular workflow for performance benchmarking of neuronal network simulations. Frontiers in neuroinformatics, 16, 837549.](https://doi.org/10.3389/fninf.2022.837549)

[Kurth et al. (2022). Sub-realtime simulation of a neuronal network of natural density. Neuromorphic computing and engineering, 2(2), 021001.](https://doi.org/10.1088/2634-4386/ac55fc)

[Golosio et al.  (2023). Runtime Construction of Large-Scale Spiking Neuronal Network Models on GPU Devices. Applied Sciences, 13(17), 9598.](https://doi.org/10.3390/app13179598)

[Heittmann et al. (2022). Simulating the cortical microcircuit significantly faster than real time on the IBM INC-3000 neural supercomputer. Frontiers in Neuroscience, 15, 728460.](https://doi.org/10.3389/fnins.2021.728460)

[Pronold et al. (2022). Routing brain traffic through the von Neumann bottleneck: Parallel sorting and refactoring. Frontiers in Neuroinformatics, 15, 785068.](https://doi.org/10.3389/fninf.2021.785068)

[Pronold et al. (2022). Routing brain traffic through the von Neumann bottleneck: Efficient cache usage in spiking neural network simulation code on general purpose computers. Parallel computing, 113, 102952.](https://doi.org/10.1016/j.parco.2022.102952)

[Kauth et al. (2023). neuroAIx-Framework: design of future neuroscience simulation systems exhibiting execution of the cortical microcircuit model 20× faster than biological real-time. Frontiers in Computational Neuroscience, 17, 1144143.](https://doi.org/10.3389/fncom.2023.1144143)

[Schmidt et al. (2024). Demonstrating the Advantages of Analog Wafer-Scale Neuromorphic Hardware. arXiv:2412.02619.](https://doi.org/10.48550/arXiv.2412.02619)
