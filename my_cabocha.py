import CaboCha


def generate_cabocha(path):
    with open(path, 'r') as f:
        text = f.read()
    c = CaboCha.Parser()
    output = c.parse(text).toString(CaboCha.FORMAT_LATTICE)
    return output


if __name__ == '__main__':
    output = generate_cabocha('neko.txt')
    with open('neko.txt.cabocha', 'w') as f:
        f.write(output)
