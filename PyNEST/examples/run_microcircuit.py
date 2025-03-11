'''
Example illustrating usage of the `microcircuit` python package.
'''

#####################
import time
import nest
import numpy as np

## import model implementation
from microcircuit import network

## import (default) parameters (network, simulation, stimulus)
from microcircuit.network_params import default_net_dict as net_dict
from microcircuit.sim_params import default_sim_dict as sim_dict
from microcircuit.stimulus_params import default_stim_dict as stim_dict

#####################

## set network scale
scaling_factor = 0.1
net_dict["N_scaling"] = scaling_factor
net_dict["K_scaling"] = scaling_factor

## set path for storing spike data and figures
sim_dict['data_path'] = 'data_scale_%.2f/' % scaling_factor
    
def main():

    ## start timer 
    time_start = time.time()

    ## create instance of the network
    net = network.Network(sim_dict, net_dict, stim_dict)
    time_network = time.time()

    ## create all nodes (neurons, devices)
    net.create()
    time_create = time.time()

    ## connect nework
    net.connect()
    time_connect = time.time()

    ## pre-simulation (warm-up phase)
    net.simulate(sim_dict["t_presim"])
    time_presimulate = time.time()

    ## simulation
    net.simulate(sim_dict["t_sim"])
    time_simulate = time.time()

    ## current memory consumption of the python process (in MB)
    import psutil
    mem = psutil.Process().memory_info().rss / (1024 * 1024)
    
    #####################
    ## plot spikes and firing rate distribution
    print()
    print('##########################################')
    print()
    observation_interval = np.array([sim_dict["t_presim"], sim_dict["t_presim"] + sim_dict["t_sim"]])
    net.evaluate(observation_interval , observation_interval )
    print()
    print('Raster plot                  : see %s ' % (sim_dict['data_path'] + 'raster_plot.png') )
    print('Distributions of firing rates: see %s ' % (sim_dict['data_path'] + 'box_plot.png'   ) )
    time_evaluate = time.time()

    #####################
    ## print timers and memory consumption

    print()
    print('##########################################')
    print()
    print('Times of Rank %d:' % nest.Rank())
    print('    Total time:')
    print('    Time to initialize  : %.3fs' % (time_network - time_start))
    print('    Time to create      : %.3fs' % (time_create - time_network))
    print('    Time to connect     : %.3fs' % (time_connect - time_create))
    print('    Time to presimulate : %.3fs' % (time_presimulate - time_connect))
    print('    Time to simulate    : %.3fs' % (time_simulate - time_presimulate))
    print('    Time to evaluate    : %.3fs' % (time_evaluate - time_simulate))
    print()
    print("Memory consumption: %dMB" % mem)
    print()
    print('##########################################')
    print()
    
#####################

if __name__== '__main__':
    main()
