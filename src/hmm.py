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


# TODO: PRINT THE NUMBER OF ITERATIONS NEEDED

    def viterbi(self, y, A, B, Pi):

        # y is the observation state sequence -> comes from the testdata.txt file.
        # A is the transition matrix within states
        # B is the emission matrix between observations & states
        # Pi is the initial state probabilities

        T1 = np.empty(shape=(A.shape[0], len(y)))
        T1[:, 0] = Pi * B[:, y[0]]

        for i in range(1, len(y)):
            T1[:, i] = np.max(T1[:, i - 1] * A.T * B[np.newaxis, :, y[i]].T, 1)

        x = np.empty(len(y), 'B')
        x[-1] = np.argmax(T1[:, len(y) - 1])

        return x, T1

    def forward(self,y, A, B, Pi):

        return 0
