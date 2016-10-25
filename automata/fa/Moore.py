# -*- coding: utf-8 -*-


class Moore(object):
    """Moore Machine : Finite Automata with Output"""

    def __init__(self, states, input_alphabet, output_alphabet, transitions, initial_state, output_table ):
        """
        states: Finite set of states
        input_alphabet: Alphabet of letters for forming input string
        output_alphabet: Alphabet of letters for forming output characters
        transitions: Transition Table
        output_table: Output Table to show what character from output_alphabet is printed when a state from 'states'
        is reached
        """

        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transitions = transitions
        self.output_table = output_table
        self.initial_state = initial_state

    def get_output_from_string(self, string):
        """Return Moore Machine's output when a given string is given as input"""
        temp_list = list(string)
        output = ''
        current_state = self.initial_state
        output += self.output_table[current_state]
        for x in temp_list:
            current_state = self.transitions[current_state][x]
            output += self.output_table[current_state]

        return output

    def __str__(self):
        """"Pretty Print the Moore Machine"""

        output = "\nMoore Machine" + \
                 "\nStates " + str(self.states) + \
                 "\nInput Alphabet " + str(self.input_alphabet) + \
                 "\nOutput Alphabet " + str(self.output_alphabet) + \
                 "\nTransitions " + str(self.transitions) + \
                 "\nInitial State" + str(self.initial_state) + \
                 "\nOutput Table " + str(self.output_table)

        return output

"""
moore = Moore(['q0', 'q1', 'q2', 'q3'],
              ['a' , 'b'],
              ['0', '1'],
              {
                  'q0' : {
                      'a' : 'q1',
                      'b' : 'q3',

                  },
                  'q1': {
                      'a': 'q3',
                      'b': 'q1',

                  },
                  'q2': {
                      'a': 'q0',
                      'b': 'q3',

                  },
                  'q3': {
                      'a': 'q3',
                      'b': 'q2',

                  }


              },

              'q0',
              {
                  'q0' : '1',
                  'q1' : '0',
                  'q2' : '0',
                  'q3' : '1'
              }


              )
print(moore)
print(moore.get_output_from_string('abbba'))
"""