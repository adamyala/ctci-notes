"""
Write code that takes a block of text and produces "flush left and right justified"
text given a max line width.
For example https://en.wikipedia.org/wiki/Typographic_alignment#Examples
"""


class Line:
    def __init__(self):
        self.words = []
        self.space_mapping = {}
        self.create_space_mapping()

    def number_of_letters(self):
        total = 0
        for word in self.words:
            total += len(word)
        return total

    def number_of_spaces(self):
        total = 0
        for _, value in self.space_mapping.items():
            total += value
        return total

    def length(self):
        number_of_letter = self.number_of_letters()
        number_of_spaces = self.number_of_spaces()
        letters_and_spaces = number_of_letter + number_of_spaces
        return letters_and_spaces

    def create_space_mapping(self):
        for index in range(len(self.words) - 1):
            """
            {
                0: 1,
                1: 2,
            }
            """
            self.space_mapping[index] = 1

    def print_line(self):
        output = ""
        for index, word in enumerate(self.words):
            output += word
            try:
                output += " " * self.space_mapping[index]
            except KeyError:
                pass
        print(output)
        return output


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
width = 30

words = text.split(" ")
lines = []
line = Line()
for word in words:
    if line.length() + len(word) + 1 <= width:
        line.words.append(word)
    else:
        lines.append(line)
        line = Line()
        line.words.append(word)

for line in lines:
    if line.length() == width:
        continue

    line.create_space_mapping()

    needed_spaces = width - line.length()
    while line.length() < width:
        for index, number_of_spaces in line.space_mapping.items():
            line.space_mapping[index] += 1
            if line.length() == width:
                break

for line in lines:
    line.print_line()
