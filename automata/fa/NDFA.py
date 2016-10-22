# -*- coding: utf-8 -*-
from automata.data_structures.Stack import Stack


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
                    print("Third Else : return")
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

        foo_dict = {}
        foo_dict[self.initial_state] = self.transitions[self.initial_state]
        #print (foo_dict)

        s = Stack()
        q = Stack()

        for x in self.alphabet:
            s.push(foo_dict[self.initial_state][x])

        #print(s)

        while(not s.isEmpty()):
           # print ("Iteration")
            current_states = s.pop()
            q.push(current_states)

            #print(q)
            #print(current_states)
            for a in self.alphabet:
                #print("a = " + str(a))
                print(s)
                temp_list = []

             #   print("temp_list = " + str(temp_list))
                for c in current_states:
                #    print("c = " + str(c))

                    for t in self.transitions[c][a]:
                        if t not in temp_list:
                            temp_list.append(t)
               #     print("temp_list.append  = " + str(temp_list))

             #   print("Temp " + str(temp_list))
              #  print("Stack" + str(s))

                if (temp_list not in q and temp_list not in s):
                   # print(s)
                    s.push(temp_list)

             #   if temp_list not in s and temp_list is not None and temp_list is not []:
                   # print("Inside if" + str(s))
                    #s.push(temp_list)

        print ("Current States "  + str(current_states))

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
    'q1': {'a': ['q0'], 'b': ['q1']},
 },
 'q0',
['q1']
)

print (d.convert_to_dfa())

s = Stack()


"""
print(d.is_string_valid('a'))
print(d)
"""