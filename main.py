from src.utils import get_arguments, initialize_parameters
from src.hmm import *


def main():
    args = get_arguments()
    mode = args[1]

    # WARNING: Play with this file to convert the initial parameters
    p0, emission, transition, states, observations = initialize_parameters()
    """print("Inital parameters:")
    print(" ")
    print("Initial state distribution:")
    print(p0)
    print(" ")
    print("Emission distribution:")
    print(emission)
    print(" ")
    print("Transition distribution:")
    print(transition)
    print(" ")"""

    if mode == '-obsv_prob':
        print("Calculating probability")
        #forward()
    elif mode == '-viterbi':
        print("Calculating Viterbi")
        hmm_object = HMM(p0, emission, transition, states, observations)
        hmm_object.viterbi()
    elif mode == '-learn':
        print("Training HMM")
        #learn()
    else:
        raise "Provide a valid argument! (-obsv_prob, -viterbi or -learn"


if __name__ == '__main__':
    main()
