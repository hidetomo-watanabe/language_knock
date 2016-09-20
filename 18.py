if __name__ == '__main__':
    f = open('hightemp.txt')
    target = f.read().strip()
    f.close()
    target_list = []
    for line in target.split('\n'):
        values = line.split('\t')
        target_list.append((values[0], values[1], float(values[2]), values[3]))
    output = []
    for tmp in sorted(target_list, key=lambda x: x[2]):
        output.append('\t'.join(map(str, tmp)))
    print('\n'.join(output))
