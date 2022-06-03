import sys
import numpy as np
import pandas as pd


def get_arguments():
    args = sys.argv
    return args


def initialize_parameters():
    p0 = np.array([0.95, 0.05])

    emission = np.array([[0.95, 0.05],
                        [0.2, 0.8]])

    transition = np.array([[0.95, 0.2],
                          [0.05, 0.8]])

    states = {'0':'0','1':'1'}
    observations = {'0':'0', '1':'1'}

    p0 = pd.DataFrame(p0, index=["0", "1"], columns=["probability"])
    emission = pd.DataFrame(emission, index=["0", "1"], columns=["0", "1"])
    transition = pd.DataFrame(transition, index=["0", "1"], columns=["0", "1"])

    return p0, emission, transition, states, observations