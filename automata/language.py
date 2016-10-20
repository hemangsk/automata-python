class Language(object):
    """Basic operations that can be performed on a language"""

    def __init__(self, language, alphabets, rules):
        """Constructor to create language and its alphabet set"""
        if(type(language) == "list"):
            self.language = language

            if(type(alphabets) == "list"):
                self.alphabets = alphabets
            else:
                self.alphabets = []

            if(type(rules) == "list"):
                self.rules = rules
            else:
                self.rules = []

    def define(self, strings):
        """Add words to the language"""

    def define_alphabets(self, element):
        """"Add elements to the set of alphabets of the language"""

        if(type(element) == "list"):
                self.alphabet = element

        else:
            self.alphabet.push(element)

    def define_rules(self, rule ):
        """Add rule string to python list of rules"""
        self.rule.push(rule)

    def show(self):
        """Getter for language"""
        output = "----------------\n"
        output += "Language is " + self.language + "\n\n"
        output += "Alphabet for it is " + self.alphabets + "\n\n"
        output += "Rules for this language are " + self.rules + "\n"
        output += "\n----------------"
        return output

    def show_alphabet(self):
        """Getter for alphabets"""
        return self.alphabets
