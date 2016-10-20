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
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states
