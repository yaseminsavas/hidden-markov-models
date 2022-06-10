import numpy as np


class HMM:
    def __init__(self, Pi, A, B, states, state_dict, observations, observation_dict):

        self.Pi = Pi
        self.A = A
        self.B = B
        self.states = states
        self.state_dict = state_dict
        self.observations = observations
        self.observation_dict = observation_dict

    # PART I
    def forward(self, y, A, B, Pi):

        forward_values = np.zeros(shape=(y.shape[0], A.shape[0]))

        # Multiplication of prior probabilities & emission matrix (initial forward values)
        for i in range(forward_values.shape[1]):
            forward_values[0, :] = B[i, y[0]] * Pi

        # Going through y values to update the probabilities
        initial_values = forward_values[0, :]
        for index, i in enumerate(y):
            if index > 0:
                initial_values = [np.sum(initial_values * A[:, j]) for j in range(0, A.shape[0])] * B[:, i]
            else:
                continue

            pos = np.where(y == i)
            forward_values[pos] = initial_values

        return np.sum(initial_values)

    # PART II
    def viterbi(self, y, A, B, Pi):

        '''
        y is the observation state sequence -> comes from the testdata.txt file.
        A is the transition matrix within states
        B is the emission matrix between observations & states
        Pi is the initial state probabilities
        '''

        probs = np.zeros(shape=(A.shape[0], len(y)))
        seq = np.zeros(shape=(len(y), 1))
        counter = 0

        for i in range(0, len(seq)-1):

            probs[:, 0] = Pi * B[:, y[0]]
            probs_1 = A * probs[:, i]
            probs_2 = B[:, y[i]]
            probs_fin = probs_2 * probs_1
            probs[:, i+1] = np.max(probs_fin, axis=1)
            seq[len(seq)-1] = np.where(np.max(probs[:, len(y) - 1]) > 0, 1, 0)
            counter += 1

        print("Iteration number: ", counter)

        return seq, probs


    # PART III
    # I didn't implemented the Baum-Welch part
    def BaumWelch(self, observations, Pi, A, B, k):
        pass