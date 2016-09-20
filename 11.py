if __name__ == '__main__':
    f = open('hightemp.txt')
    target = f.read().strip()
    f.close()
    print(target.replace('\t', ' '))
