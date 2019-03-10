import my_mecab
if __name__ == '__main__':
    mapping = my_mecab.generate_mapping('neko.txt.mecab')
    words = []
    for sentence in mapping:
        for morpheme in sentence:
            words.append(morpheme['surface'])
    values = []
    for value in list(set(words)):
        values.append((value, words.count(value)))
    count = 0
    for tmp in reversed(sorted(values, key=lambda x: x[1])):
        count += 1
        print('%s: %s' % (tmp[0], tmp[1]))
        if count >= 20:
            break
