import my_mecab
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
if __name__ == '__main__':
    mapping = my_mecab.generate_mapping('neko.txt.mecab')
    words = []
    for sentence in mapping:
        for morpheme in sentence:
            words.append(morpheme['surface'])
    values = []
    for value in list(set(words)):
        values.append((value, words.count(value)))
    x_data = []
    y_data = []
    count = 0
    for tmp in reversed(sorted(values, key=lambda x: x[1])):
        count += 1
        x_data.append(count)
        y_data.append(float(tmp[1]/len(words))*100)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xscale('log')
    ax.set_yscale('log')
    H = ax.bar(x_data, y_data)
    plt.savefig('39_histogram.png')
