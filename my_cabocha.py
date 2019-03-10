import CaboCha


def generate_cabocha(path):
    with open(path, 'r') as f:
        text = f.read()
    c = CaboCha.Parser()
    output = c.parse(text).toString(CaboCha.FORMAT_LATTICE)
    return output


class Morph(object):
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def display(self):
        print(
            f'surface: {self.surface}\t' +
            f'base: {self.base}\t' +
            f'pos: {self.pos}\t' +
            f'pos1: {self.pos1}')


if __name__ == '__main__':
    output = generate_cabocha('neko.txt')
    with open('neko.txt.cabocha', 'w') as f:
        f.write(output)
