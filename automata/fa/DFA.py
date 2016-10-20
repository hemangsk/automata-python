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
        for
