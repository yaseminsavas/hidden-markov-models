from src.utils import get_arguments


def main():
    args = get_arguments()
    mode = args[1]

    if mode == '-obsv_prob':
        print("Calculating probability")
        #calculate_probability()
    elif mode == '-viterbi':
        print("Calculating Viterbi")
        #viterbi()
    elif mode == '-learn':
        print("Training HMM")
        #training()
    else:
        raise("Provide a valid argument! (-obsv_prob, -viterbi or -learn")


if __name__ == '__main__':
    main()
