#!/usr/bin/env python
# encoding: utf8
'''
PyNEST implementation of the cortical microcircuit model of Potjans & Diesmann (2014).

Usage: microcircuit [options] run
       microcircuit [options] config

Options:
    -v, --verbose       increase output
    -h, --help          print this text
'''
import logging
import time

from pprint import pformat
from docopt import docopt       # type: ignore

import nest
import numpy as np

from microcircuit.network import Network
from microcircuit.network_params import default_net_dict as net_dict
from microcircuit.sim_params import default_sim_dict as sim_dict
from microcircuit.stimulus_params import default_stim_dict as stim_dict

log = logging.getLogger()
logging.basicConfig(level=logging.INFO)

def run_example():
    time_start = time.time()

    ###############################################################################
    # Initialize the network with simulation, network and stimulation parameters,
    # then create and connect all nodes, and finally simulate.
    # The times for a presimulation and the main simulation are taken
    # independently. A presimulation is useful because the spike activity typically
    # exhibits a startup transient. In benchmark simulations, this transient should
    # be excluded from a time measurement of the state propagation phase. Besides,
    # statistical measures of the spike activity should only be computed after the
    # transient has passed.

    net = Network(sim_dict, net_dict, stim_dict)
    time_network = time.time()

    net.create()
    time_create = time.time()

    net.connect()
    time_connect = time.time()

    net.simulate(sim_dict["t_presim"])
    time_presimulate = time.time()

    net.simulate(sim_dict["t_sim"])
    time_simulate = time.time()

    ###############################################################################
    # Plot a spike raster of the simulated neurons and a box plot of the firing
    # rates for each population.
    # For visual purposes only, spikes 100 ms before and 100 ms after the thalamic
    # stimulus time are plotted here by default.
    # The computation of spike rates discards the presimulation time to exclude
    # initialization artifacts.

    raster_plot_interval = np.array([stim_dict["th_start"] - 100.0, stim_dict["th_start"] + 100.0])
    firing_rates_interval = np.array([sim_dict["t_presim"], sim_dict["t_presim"] + sim_dict["t_sim"]])
    net.evaluate(raster_plot_interval, firing_rates_interval)
    time_evaluate = time.time()

    ###############################################################################
    # Summarize time measurements. Rank 0 usually takes longest because of the
    # data evaluation and print calls.

    print(
        "\nTimes of Rank {}:\n".format(nest.Rank())
        + "  Total time:          {:.3f} s\n".format(time_evaluate - time_start)
        + "  Time to initialize:  {:.3f} s\n".format(time_network - time_start)
        + "  Time to create:      {:.3f} s\n".format(time_create - time_network)
        + "  Time to connect:     {:.3f} s\n".format(time_connect - time_create)
        + "  Time to presimulate: {:.3f} s\n".format(time_presimulate - time_connect)
        + "  Time to simulate:    {:.3f} s\n".format(time_simulate - time_presimulate)
        + "  Time to evaluate:    {:.3f} s\n".format(time_evaluate - time_simulate)
    )

    
def main():
    'Start main CLI entry point.'
    args = docopt(__doc__)
    if args['--verbose']:
        log.setLevel(logging.DEBUG)
    log.debug(pformat(args))

    log.info("Hello World")

    if args['run']:        
        run_example()
        
    if args['config']:
        from ruamel.yaml import YAML
        import sys
        yaml=YAML()
        yaml.dump({"net_dict": net_dict, "stim_dict": stim_dict, "sim_dict": sim_dict}, sys.stdout)

        
if __name__ == '__main__':
    main()
