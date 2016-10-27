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
        """Return Mealy Machine's output when a given string is given as input"""

        temp_list = list(string)
        current_state = self.initial_state
        output = ''
        for x in temp_list:
            output+= self.transitions[current_state][x][1]
            current_state = self.transitions[current_state][x][0]

        return output

    def convert_to_moore(self):
        moore_transitions = {}
        temp_list = []
        moore_output_table = {}
        moore_initial_state = self.initial_state
        for x in self.transitions.keys():
            for a in self.input_alphabet:
                temp_list.append(self.transitions[x][a])

        temp_list_2 = []
        for x in temp_list:
            for y in temp_list:
                if x[0] == y[0] and x[1] != y[1]:
                    if x not in temp_list_2 and y not in temp_list_2:
                        temp_list_2.append(x)
                        temp_list_2.append(y)

        temp_list_3 = []
        for x in temp_list_2:
            if x[0] not in temp_list_3:
                temp_list_3.append(x[0])

        if self.initial_state in temp_list_3:
            moore_initial_state = self.initial_state + self.output_alphabet[0]

        for x in temp_list_2:
            for a in self.input_alphabet:
                if self.transitions[x[0]][a][0] in temp_list_3:
                    next_state = self.transitions[x[0]][a][0]
                    output = self.transitions[x[0]][a][1]

                    next_state = next_state + output
                    try:
                        moore_transitions[x[0] + x[1]][a] = next_state
                    except KeyError as e:
                        moore_transitions[x[0] + x[1]] = {}
                        moore_transitions[x[0] + x[1]][a] = next_state

                    if next_state not in moore_output_table.keys():
                        moore_output_table[next_state] = output

                else:
                    try:
                        moore_transitions[x[0] + x[1]][a] = self.transitions[x[0]][a][0]
                    except KeyError as e:
                        moore_transitions[x[0] + x[1]] = {}
                        moore_transitions[x[0] + x[1]][a] = self.transitions[x[0]][a][0]

                    if moore_transitions[x[0] + x[1]][a] not in moore_output_table.keys():
                        moore_output_table[moore_transitions[x[0] + x[1]][a]] = self.transitions[x[0]][a][1]

        for x in self.transitions.keys():
            if x not in moore_transitions.keys() and x not in temp_list_3:
                for a in self.input_alphabet:
                    if self.transitions[x][a][0] in temp_list_3:
                        next_state = self.transitions[x][a][0]
                        output = self.transitions[x][a][1]

                        next_state = next_state + output
                        try:
                            moore_transitions[x][a] = next_state
                        except KeyError as e:
                            moore_transitions[x] = {}
                            moore_transitions[x][a] = next_state

                        if next_state not in moore_output_table.keys():
                            moore_output_table[next_state] = output

                    else:
                        try:
                            moore_transitions[x][a] = self.transitions[x][a][0]
                        except KeyError as e:
                            moore_transitions[x] = {}
                            moore_transitions[x][a] = self.transitions[x][a][0]

                        if self.transitions[x][a][0] not in moore_output_table.keys():
                            moore_output_table[self.transitions[x][a][0]] = self.transitions[x][a][1]

        moore_states = []
        for s in moore_transitions.keys():
            if s not in moore_states:
                moore_states.append(s)

        from automata.fa.Moore import Moore

        moore_from_mealy = Moore(
            moore_states,
            self.input_alphabet,
            self.output_alphabet,
            moore_transitions,
            moore_output_table,
            moore_initial_state
        )

        print(moore_from_mealy)


    def __str__(self):
        output = "\nMealy Machine" + \
                 "\nStates " + str(self.states) + \
                 "\nTransitions " + str(self.transitions) + \
                 "\nInital State " + str(self.initial_state) + \
                 "\nInital Alphabet " + str(self.input_alphabet) + \
                 "\nOutput Alphabet" + str(self.output_alphabet)

        return output




"""
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

mealy_3 = Mealy(['q0', 'q1', 'q2', 'q3'],
                ['0', '1'],
                ['0', '1'],
                {
                    'q0' : {
                        '0' : ('q3', '0'),
                        '1' : ('q1', '1')
                    },
                    'q1': {
                        '0': ('q0', '1'),
                        '1': ('q3', '0')
                    },
                    'q2': {
                        '0': ('q2', '1'),
                        '1': ('q2', '0')
                    },
                    'q3': {
                        '0': ('q1', '0'),
                        '1': ('q0', '1')
                    }

                },
                'q0'

                )
#print(mealy_2)
#print(mealy_2.get_output_from_string('0111'))
print(mealy_3.convert_to_moore())
"""