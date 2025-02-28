'''
testsuit for correct simulation
'''

#####################
import nest
import pytest
import numpy as np

## import model implementation
from microcircuit import network

## import (default) parameters (network, simulation, stimulus)
from microcircuit.network_params import default_net_dict as net_dict
from microcircuit.sim_params import default_sim_dict as sim_dict
from microcircuit.stimulus_params import default_stim_dict as stim_dict

#####################

# set scaling factor of simulation
scaling_factor = 0.1
sim_dict['N_scaling'] = scaling_factor
sim_dict['K_scaling'] = scaling_factor

def test_simulation():
    
    ## set simulation time
    sim_dict['t_sim'] = 100.0 

    def run_simulation():
        ## create instance of the network
        net = network.Network(sim_dict, net_dict, stim_dict)

        ## create all nodes (neurons, devices)
        net.create()

        ## connect nework
        net.connect()

        ## simulation
        net.simulate(sim_dict["t_sim"])

        return not None

    try:
        result = run_simulation()

    except Exception as e:
        pytest.fail(f'Simulation raised an exception: {e}')

    assert result is not None

    print('======================================')
    print('')
    print('Test passed')
    print('')
    print('microcircuit.simulate() runs correctly')
    print('')
    print('======================================')

if __name__ == '__main__':
    test_simulation()

