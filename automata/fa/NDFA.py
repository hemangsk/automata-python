# -*- coding: utf-8 -*-
from automata.data_structures.Stack import Stack
from automata.fa.DFA import DFA


class NDFA(object):
    """Non Deterministic Finite Automata"""

    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        """
        Q is a finite set of states.

        sigma is a finite set of symbols called the alphabet.

        delta is the list of transitions based on transition relation.

        q0 is the initial state from where any input is processed (q0 ∈ Q).

        F is a set of final state/states of Q (F ⊆ Q).
        """

        self.states = states                        #list
        self.alphabet = alphabet                    #list
        self.transitions = transitions              #dict
        self.initial_state = initial_state          #char
        self.final_states = final_states            #list

        """
        states=['q0', 'q1'],
        alphabets=['a', 'b'],
        transitions={
            'q0': {'a': ['q0', 'q1'], 'b': ['q1']},
            'q1': {'a': ['q0'], 'b': ['q1', 'q0']},
         },
        initial_state='q0',
        final_states=['q1']
        """

    def is_string_valid(self, string):
        """Return True if string is accepted by NDFA, otherwise return False"""

        inputs = list(string)
        current_state = self.initial_state

        for letter in inputs:

            try:

                if isinstance(current_state, list):
                    temp_cur_state = []
                    for state in current_state:
                        if letter in self.transitions[state]:
                            temp_cur_state.push(self.transitions[state][letter])
                    current_state = temp_cur_state

                elif isinstance(current_state, str):
                    if letter in self.transitions[current_state]:
                        current_state = self.transitions[current_state][letter]

                else:
                    return False

            except KeyError as e:
                return False

        if isinstance(current_state, str):
            if current_state in self.final_states:
                return True

        elif isinstance(current_state, list):
            if not set(current_state).isdisjoint(self.final_states):
                return True

        return False

    def convert_to_dfa(self):
        """"Returns equivalent DFA of the given NDFA"""

        temp_init_state_list = [self.initial_state]

        foo_dict = {str(temp_init_state_list): self.transitions[self.initial_state]}

        s = Stack()
        q = Stack()

        for x in self.alphabet:
            s.push(foo_dict[str(temp_init_state_list)][x])

        while not s.isEmpty():

            current_states = s.pop()
            q.push(current_states)

            if current_states != foo_dict.keys():
                foo_dict[str(current_states)] = {}

            for a in self.alphabet:

                temp_list = []

                for c in current_states:

                    try:
                        for t in self.transitions[c][a]:
                            if t not in temp_list:
                                temp_list.append(t)

                    except KeyError as e:
                        pass

                foo_dict[str(current_states)][a] = (temp_list)

                if temp_list not in q and temp_list not in s and temp_list is not []:
                    s.push(temp_list)

        dfa_initial_state = 'Q0'

        i = 0
        map_states ={}
        for a in foo_dict.keys():
            map_states[a] = 'Q' + str(i)
            i+=1

        dfa_transitions = {}
        dfa_finial_states = []
        dfa_states = []

        for a in foo_dict.keys():
            dfa_transitions[map_states[a]] = {}
            for b in self.alphabet:

                if  set(foo_dict[a][b]).isdisjoint(self.final_states):
                    if (a) not in dfa_finial_states:
                        dfa_finial_states.append(map_states[a])

                dfa_transitions[map_states[a]][b] = map_states[str(foo_dict[a][b])]

                if map_states[a] not in dfa_states:
                    dfa_states.append(map_states[a])

                if (map_states[str(foo_dict[a][b])]) not in dfa_states:
                    dfa_states.append(map_states[str(foo_dict[a][b])])

        # Here we go
        d = DFA(dfa_states, self.alphabet, dfa_transitions, dfa_initial_state, dfa_finial_states)
        print(d)
        return d

    def __str__(self):
        """"Pretty Print the NDFA"""

        output = "\nNon-Deterministic Finite Automata" + \
                 "\nStates " + str(self.states) + \
                 "\nAlphabet " + str(self.alphabet) + \
                 "\nTransitions " + str(self.transitions) + \
                 "\nInital State " + str(self.initial_state) + \
                 "\nFinal States " + str(self.final_states)

        return output



d = NDFA(
['q0', 'q1'],
['a', 'b'],
{
    'q0': {'a': ['q0', 'q1'], 'b': ['q1']},
    'q1': {'a': ['q0'], 'b': ['q1']}
 },
 'q0',
['q1']
)



"""
print (d.convert_to_dfa())
print(d.is_string_valid('a'))
print(d)
"""