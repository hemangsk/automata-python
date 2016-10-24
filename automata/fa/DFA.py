# -*- coding: utf-8 -*-

import itertools

class DFA(object):
    """Deterministic Finite Automata"""

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
            'q0': {'a': 'q0', 'b': 'q1'},
            'q1': {'a': 'q0', 'b': 'q1'},
         },
        initial_state='q0',
        final_states=['q1']
        """

    def is_string_valid(self, string):
        """Return True if string is accepted by DFA, otherwise return False"""

        inputs = list(string)
        current_state = self.initial_state

        for letter in inputs:
            try:

                if letter in self.transitions[current_state]:
                    current_state = self.transitions[current_state][letter]

                else:
                    return False
            except KeyError as e:
                return False

        if current_state in self.final_states:
            return True

        return False

    def minimize(self):

        state_list = []
        state_list.append(list(set(self.states) - set(self.final_states)))
        state_list.append(self.final_states)

        foo_dict = {}

        state_list, foo_dict = self.create_foo_dict(state_list, foo_dict)
        print (foo_dict)
        print (state_list)

        self.create_state_list(state_list, foo_dict)

    def create_state_list(self, state_list, foo_dict):
        temp_list = []
        for x in foo_dict.keys():
            temp_list.append(foo_dict[x])

        temp_list_2 = []
        for x in temp_list:
            if x not in temp_list_2:
                temp_list_2.append(x)

        print(temp_list_2)
        state_list = []

        for x in temp_list_2:
            state_list_element = []
            for k,v in foo_dict.items():
                if v == x:
                    state_list_element.append(k)
            state_list.append(state_list_element)

        print(state_list)

    def create_foo_dict(self, state_list, foo_dict):

        for x in self.states:
            for a in self.alphabet:
                for y in state_list:
                    if self.transitions[x][a] in y:
                        try:
                            foo_dict[x].append(state_list.index(y))
                        except KeyError as e:
                            foo_dict[x] = []
                            foo_dict[x].append(state_list.index(y))

        return state_list, foo_dict

    def __str__(self):
        """"Pretty Print the DFA"""

        output = "\nDeterministic Finite Automata" + \
                 "\nStates " + str(self.states) + \
                 "\nAlphabet " + str(self.alphabet) + \
                 "\nTransitions " + str(self.transitions) + \
                 "\nInital State " + str(self.initial_state) + \
                 "\nFinal States " + str(self.final_states)

        return output




d = DFA(
['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8','q9','q10'],
['a', 'b'],
{

    'q0': {'a': 'q3', 'b': 'q2'},
    'q1': {'a': 'q6', 'b': 'q2'},
    'q2': {'a': 'q8', 'b': 'q5'},
    'q3': {'a': 'q0', 'b': 'q1'},
    'q4': {'a': 'q2', 'b': 'q5'},
    'q5': {'a': 'q4', 'b': 'q3'},
    'q6': {'a': 'q1', 'b': 'q0'},
    'q7': {'a': 'q4', 'b': 'q6'},
    'q8': {'a': 'q2', 'b': 'q7'},
    'q9': {'a': 'q7', 'b': 'q10'},
    'q10': {'a': 'q5', 'b': 'q9'}

 },
'q0',
['q3', 'q4', 'q6','q8']
)

d.minimize()
"""
print(d.is_string_valid('ababba'))
print(d.convert_to_dfa())
print(d)
"""