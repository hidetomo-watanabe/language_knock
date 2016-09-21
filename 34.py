import my_mecab
if __name__ == '__main__':
    mapping = my_mecab.generateMapping('neko.txt.mecab')
    output = []
    flag = 0
    tmp = ''
    for sentence in mapping:
        for morpheme in sentence:
            if flag in [0, 2] and morpheme['pos'] == '名詞':
                flag += 1
                tmp += morpheme['surface']
            elif flag == 1 and morpheme['surface'] == 'の':
                flag += 1
                tmp += morpheme['surface']
            else:
                flag = 0
                tmp = ''
            if flag == 3:
                output.append(tmp)
                flag = 0
                tmp = ''
    output = list(set(output))
    print(output)
