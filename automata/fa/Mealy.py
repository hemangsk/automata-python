# -*- coding: utf-8 -*-


class Mealy(object):
    """Mealy Machine : Finite Automata with Output """

    def __init__(self, states, input_alphabet, output_alphabet, transitions, initial_state):
        """
        6 tuple (Q, ∑, O, δ, X, q0) where −

        states is a finite set of states.

        alphabet is a finite set of symbols called the input alphabet.

        output_alphabet is a finite set of symbols called the output alphabet.

        transitions is the resultant data dictionary of input and output transition functions

        initial_state is the initial state from where any input is processed (q0 ∈ Q).
        """
        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transitions = transitions
        self.initial_state = initial_state

    def get_output_from_string(self, string):

        temp_list = list(string)
        current_state = self.initial_state
        output = ''
        for x in temp_list:
            output+= self.transitions[current_state][x][1]
            current_state = self.transitions[current_state][x][0]

        return output

    def __str__(self):
        output = "\nMealy Machine" + \
                 "\nStates " + str(self.states) + \
                 "\nTransitions " + str(self.transitions) + \
                 "\nInital State " + str(self.initial_state) + \
                 "\nInital Alphabet " + str(self.input_alphabet) + \
                 "\nOutput Alphabet" + str(self.output_alphabet)

        return output


"""
d = DFA(

)

d.minimize()
print(d.is_string_valid('ababba'))
print(d.convert_to_dfa())
print(d)


mealy = Mealy(
    ['a', 'b', 'c', 'd'],
    ['0', '1'],
    ['0', '1'],
    {
        'a' : {
            '0' : ('d', '1'),
            '1' : ('b', '0')
        },

        'b' : {
            '0' : ('a', '1'),
            '1' : ('d', '1')
        },

        'c' :{
            '0' : ('c', '0'),
            '1' : ('c', '0')
        },
        'd':{
            '0' : ('b', '0'),
            '1' : ('a', '1')
        }
    },
    'a'
)


mealy_2 = Mealy(['q0'],
                ['0', '1'],
                ['0', '1'],
                {
                    'q0' : {
                        '1' : ('q0', '0'),
                        '0' : ('q0', '1')
                    }
                },
                'q0'
                )
print(mealy_2)
print(mealy_2.get_output_from_string('0111'))
"""