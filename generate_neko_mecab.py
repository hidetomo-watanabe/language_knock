import MeCab
if __name__ == '__main__':
    f = open('neko.txt')
    target = f.read()
    f.close()
    mecab = MeCab.Tagger()
    output = mecab.parse(target)
    f = open('neko.txt.mecab', 'w')
    f.write(output)
    f.close()
