import my_mecab
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
if __name__ == '__main__':
    mapping = my_mecab.generateMapping('neko.txt.mecab')
    words = []
    for sentence in mapping:
        for morpheme in sentence:
            words.append(morpheme['surface'])
    counts = []
    for value in list(set(words)):
        counts.append(words.count(value))
    values = []
    for value in list(set(counts)):
        values.append((value, counts.count(value)))
    x_data = []
    y_data = []
    for tmp in values:
        x_data.append(tmp[0])
        y_data.append(tmp[1])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    H = ax.bar(x_data, y_data)
    plt.savefig('38_histogram.png')
