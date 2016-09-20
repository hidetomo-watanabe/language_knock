if __name__ == '__main__':
    f = open('hightemp.txt')
    target = f.read().strip()
    f.close()
    col1 = []
    for line in target.split('\n'):
        col1.append(line.split('\t')[0])
    values = []
    for value in list(set(col1)):
        values.append((value, col1.count(value)))
    for tmp in reversed(sorted(values, key=lambda x: x[1])):
        print('%s: %s' % (tmp[0], tmp[1]))
