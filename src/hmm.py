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
    def forward(self,y, A, B, Pi):

        store_forward = np.zeros(shape=(y.shape[0], A.shape[0]))

        # initial calculation
        c1 = Pi.T * B[:, y[0]]
        store_forward[0, :] = c1

        cp = 0
        for i in y[1:]:
            ctemp = [sum(c1 * A[:, j]) for j in range(A.shape[0])]
            c2 = ctemp * B[:, i]  # calculates the other columns recursively
            c1 = c2
            store_forward[np.where(y == i), :] = c1
            cp = sum(c1)

        return cp

    # PART II
    def viterbi(self, y, A, B, Pi):

        '''
        y is the observation state sequence -> comes from the testdata.txt file.
        A is the transition matrix within states
        B is the emission matrix between observations & states
        Pi is the initial state probabilities
        '''

        T1 = np.zeros(shape=(A.shape[0], len(y)))
        x = np.zeros(len(y), 'B')

        T1[:, 0] = Pi * B[:, y[0]]

        counter = 0
        for i in range(1, len(y)):
            T1[:, i] = np.max(T1[:, i - 1] * A.T * B[np.newaxis, :, y[i]].T, 1)
            counter += 1

        x[-1] = np.argmax(T1[:, len(y) - 1])

        print("Iteration number: ", counter)

        return x, T1

    # PART III
    def BaumWelch(self):
        pass
