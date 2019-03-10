import my_mecab
if __name__ == '__main__':
    mapping = my_mecab.generate_mapping('neko.txt.mecab')
    words = []
    flag = 0
    tmp = ''
    for sentence in mapping:
        for morpheme in sentence:
            if morpheme['pos'] == '名詞':
                flag += 1
                tmp += morpheme['surface']
            else:
                flag = 0
                tmp = ''
            if flag == 2:
                words.append(tmp)
                flag = 0
                tmp = ''
    tmp = 0
    output = []
    for word in list(set(words)):
        if len(word) > tmp:
            tmp = len(word)
            output = []
        if len(word) == tmp:
            output.append(word)
    print(output)
