import my_mecab
if __name__ == '__main__':
    mapping = my_mecab.generate_mapping('neko.txt.mecab')
    output = []
    for sentence in mapping:
        for morpheme in sentence:
            if morpheme['pos'] == '名詞' and morpheme['pos1'] == 'サ変接続':
                output.append(morpheme['surface'])
    output = list(set(output))
    print(output)
