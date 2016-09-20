if __name__ == '__main__':
    f = open('hightemp.txt')
    target = f.read().strip()
    f.close()
    col1 = col2 = ''
    for line in target.split('\n'):
        col1 += line.split('\t')[0] + '\n'
        col2 += line.split('\t')[1] + '\n'
    f = open('col1.txt', 'w')
    f.write(col1.strip())
    f.close()
    f = open('col2.txt', 'w')
    f.write(col2.strip())
    f.close()
