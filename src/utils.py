import sys
import numpy as np
import pandas as pd


def get_arguments():
    args = sys.argv
    return args


def initialize_parameters():

    # initial state probabilities
    Pi = np.array([0.95, 0.05]) # columns 0 - 1

    # emission matrix
    B = np.array([[0.05, 0.95],  # columns: loss - ok, rows: 0 - 1
                        [0.8, 0.2]])

    # state transition matrix
    A = np.array([[0.95, 0.05],  # columns: 0 - 1, rows: 0 - 1
                          [0.1, 0.9]])

    #states
    states = np.array([0, 1])
    state_dict = {0: 'not-jammed', 1: "jammed"}

    #observations (visible)
    observations = np.array([0,1])
    observation_dict = {0: 'ok', 1: "loss"}

    return Pi, A, B, states, state_dict, observations, observation_dict
