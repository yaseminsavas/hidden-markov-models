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

        # Multiplication of prior probabilities & emission matrix (initial forward values)
        forward_values = np.zeros(shape=(y.shape[0], A.shape[0]))
        forward_values[0, :] = B[:, y[0]] * Pi

        # Going through y values to update the probabilities
        initial_values = forward_values[0, :]
        for index, i in enumerate(y):
            if index > 0:
                initial_values = [np.sum(initial_values * A[:, j]) for j in range(0, A.shape[0])] * B[:, i]
                forward_values[np.where(y == i)] = initial_values
            else:
                continue

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

        probs[:, 0] = Pi * B[:, y[0]]

        counter = 0
        for i in range(1, len(y)):

            probs_1 = probs[:, i - 1] * A.T
            probs_2 = B[np.newaxis, :, y[i]].T
            probs_fin = probs_1 * probs_2
            probs[:, i] = np.max(probs_fin, 1)
            counter += 1
            seq[len(seq)-1] = np.argmax(probs[:, len(y) - 1])

        print("Iteration number: ", counter)
        return seq, probs

    # PART III
    # I didn't implemented the Baum-Welch part
    def BaumWelch(self, observations, Pi, A, B, k):
        pass