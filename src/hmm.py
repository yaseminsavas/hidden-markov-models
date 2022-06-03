class HMM:
    def __init__(self, p0, emission, transition, states, observations):

        self.p0 = p0
        self.transition = transition
        self.emission = emission
        self.states = states
        self.observations = observations

    def viterbi(self):

        # initially
        viterbi_result = [{}]
        for st in self.states:
            viterbi_result[0][st] = {"probability": self.p0["probability"][st] * self.emission[st][self.observations[st]], "previous": None}

        print(viterbi_result)

        for observation in range(len(self.observations)):
            viterbi_result.append({})

            for index, state in enumerate(self.states):

                max_tr_prob = viterbi_result[index][state]["probability"] * \
                              self.transition[self.states[index]][self.states[index]]
                prev_st_selected = self.states[index]

                for prev_st in self.states[1:]:

                    tr_prob = viterbi_result[index][prev_st]["probability"] * self.transition[prev_st][self.states[index]]
                    if tr_prob > max_tr_prob:
                        max_tr_prob = tr_prob
                        prev_st_selected = prev_st

                max_prob = max_tr_prob * self.emission[state][self.observations[state]]
                viterbi_result[index] = {"probability": max_prob, "previous": prev_st_selected}
                print(viterbi_result)

                opt = []
                max_prob = 0.0
                best_st = None

                for st, data in viterbi_result[-1].items():
                    if data["probability"] > max_prob:
                        max_prob = data["probability"]
                        best_st = st
                opt.append(best_st)
                previous = best_st

                for t in range(len(viterbi_result) - 2, -1, -1):
                    opt.insert(0, viterbi_result[t + 1][previous]["previous"])
                    previous = viterbi_result[t + 1][previous]["previous"]

                print("The steps of states are " + " ".join(opt) + " with highest probability of %s" % max_prob)