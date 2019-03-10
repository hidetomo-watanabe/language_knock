import my_mecab
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
if __name__ == '__main__':
    mapping = my_mecab.generateMapping('neko.txt.mecab')
    words = []
    for sentence in mapping:
        for morpheme in sentence:
            words.append(morpheme['surface'])
    values = []
    for value in list(set(words)):
        values.append((value, words.count(value)))
    count = 0
    x_data = []
    y_data = []
    for tmp in reversed(sorted(values, key=lambda x: x[1])):
        count += 1
        x_data.append(count)
        y_data.append(tmp[1])
        if count >= 10:
            break
    fig = plt.figure()
    ax = fig.add_subplot(111)
    H = ax.bar(x_data, y_data)
    plt.savefig('37_histogram.png')
