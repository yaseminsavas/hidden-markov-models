

class HMM:
    def __init__(self, p0, emission, transition, states, observations):

        self.p0 = p0
        self.transition = transition
        self.emission = emission
        self.states = states
        self.observations = observations

    def viterbi(self):

        viterbi_result = [{}]
        for st in self.states:
            viterbi_result[0][st] = {"probability": self.p0["probability"][st] * self.emission[st][self.observations['0']], "prev": None}

        for observation in range(len(self.observations)):
            viterbi_result.append({})

        print(viterbi_result)


    def viterbi_algorithm(self):

        for t in range(1, len(observations)):
            V.append({})
            for st in states:
                max_tr_prob = V[t - 1][states[0]]["prob"] * trans_p[states[0]][st]
                prev_st_selected = states[0]
                for prev_st in states[1:]:
                    tr_prob = V[t - 1][prev_st]["prob"] * trans_p[prev_st][st]
                    if tr_prob > max_tr_prob:
                        max_tr_prob = tr_prob
                        prev_st_selected = prev_st

                max_prob = max_tr_prob * emit_p[st][observations[t]]
                V[t][st] = {"prob": max_prob, "prev": prev_st_selected}

        for line in dptable(V):
            print(line)

        opt = []
        max_prob = 0.0
        best_st = None

        for st, data in V[-1].items():
            if data["prob"] > max_prob:
                max_prob = data["prob"]
                best_st = st
        opt.append(best_st)
        previous = best_st

        for t in range(len(V) - 2, -1, -1):
            opt.insert(0, V[t + 1][previous]["prev"])
            previous = V[t + 1][previous]["prev"]

        print("The steps of states are " + " ".join(opt) + " with highest probability of %s" % max_prob)


def dptable(V):
    yield " ".join(("%12d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)