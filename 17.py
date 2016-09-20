if __name__ == '__main__':
    f = open('hightemp.txt')
    target = f.read().strip()
    f.close()
    col1 = []
    for line in target.split('\n'):
        col1.append(line.split('\t')[0])
    print('\n'.join(list(set(col1))).strip())
