from src.utils import get_arguments, initialize_parameters
from src.hmm import *


def main():
    args = get_arguments()
    mode = args[1]

    # WARNING: Play with this file to convert the initial parameters
    Pi, A,B, states, state_dict, observations, observation_dict = initialize_parameters()
    print("Inital parameters:")
    print(" ")
    print("Initial probabilities:")
    print(Pi)
    print(" ")
    print("Emission distribution:")
    print(B)
    print(" ")
    print("Transition distribution:")
    print(A)
    print(" ")

    # Data gathering for PART II - Viterbi Algorithm
    sequences = []
    with open("data/testdata.txt") as file:
        lines = file.readlines()
        for line in lines:
            line_v2 = line.split(" \n")[0]
            sequences.append(line_v2)

    array_sequences = []
    for sequence in sequences:
        arr_subseq = []
        element = sequence.split(" ")
        for el in element:
            if el == '0' or el == '1':
                arr_subseq.append(int(el))
        array_sequences.append(arr_subseq)

    hmm_object = HMM(Pi, A, B, states, state_dict, observations, observation_dict)

    if mode == '-obsv_prob':

        print("Calculating probability of a given sequence")
        print(" ")
        hmm_object.forward(np.array(array_sequences[0]), A, B, Pi)

    elif mode == '-viterbi':

        print("Calculating the most possible state sequence using the Viterbi Algorithm...")
        print("Observed sequence: ", np.array(array_sequences[0]))

        likely_seq, likely_prob = hmm_object.viterbi(np.array(array_sequences[0]), A, B, Pi)

        print("The most likely sequence: ")
        print(likely_seq)
        print(" ")
        print("Its' probabilities: ")
        print(likely_prob)
        print(" ")

    elif mode == '-learn':
        print("Training HMM")
        #learn()
    else:
        raise "Provide a valid argument! (-obsv_prob, -viterbi or -learn"


if __name__ == '__main__':
    main()
