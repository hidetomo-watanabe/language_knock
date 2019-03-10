import MeCab


def generate_mecab(target):
    f = open(target)
    target = f.read()
    f.close()
    mecab = MeCab.Tagger()
    output = mecab.parse(target)
    return output


def generate_mapping(target):
    f = open(target)
    target = f.readlines()
    f.close()
    output = []
    sentence = []
    for line in target:
        if line.strip() == 'EOS':
            continue
        tmp = line.split('\t')
        surface = tmp[0]
        tmp2 = tmp[1].split(',')
        pos = tmp2[0]
        pos1 = tmp2[1]
        base = tmp2[6]
        sentence.append({
            'surface': surface,
            'base': base,
            'pos': pos,
            'pos1': pos1,
        })
        if surface == '。':
            output.append(sentence)
            sentence = []
    return output


if __name__ == '__main__':
    output = generate_mecab('neko.txt')
    f = open('neko.txt.mecab', 'w')
    f.write(output)
    f.close()
