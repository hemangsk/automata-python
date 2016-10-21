# -*- coding: utf-8 -*-
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
     d
        for letter in inputs:
            try:

                if(letter in self.transitions[current_state]):
                    current_state = self.transitions[current_state][letter]

                else:
                    return False
            except KeyError as e:
                return False


        if(current_state in self.final_states):
            return True

        return False


d = DFA(
['q0', 'q1'],
['a', 'b'],
{
    'q0': {'a': 'q0', 'b': 'q1'},
    'q1': {'a': 'q0', 'b': 'q1'},
 },
'q0',
['q1']
)

print(d.is_string_valid('ab'))
