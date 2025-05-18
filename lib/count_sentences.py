#!/usr/bin/env python3
class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # this goes through the setter for validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        import re

        # Split on '.', '?', or '!' using regex
        # The `+` ensures we treat multiple punctuations like '!!' as one separator
        sentence_list = re.split(r'[.!?]+', self.value)
        
        # Remove empty strings or strings that only contain whitespace
        non_empty = [s for s in sentence_list if s.strip()]

        return len(non_empty)

