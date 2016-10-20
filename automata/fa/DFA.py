# -*- coding: utf-8 -*-
class DFA(object):
    """Deterministic Finite Automata"""

    def __init__(self, Q, sigma, delta, q0, F):
        """
        Q is a finite set of states.

        sigma is a finite set of symbols called the alphabet.

        delta is the transition function where delta: Q x sigma → Q

        q0 is the initial state from where any input is processed (q0 ∈ Q).

        F is a set of final state/states of Q (F ⊆ Q).
        """
