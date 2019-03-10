import my_mecab
if __name__ == '__main__':
    mapping = my_mecab.generate_mapping('neko.txt.mecab')
    output = []
    for sentence in mapping:
        for morpheme in sentence:
            if morpheme['pos'] == '動詞':
                output.append(morpheme['base'])
    output = list(set(output))
    print(output)
