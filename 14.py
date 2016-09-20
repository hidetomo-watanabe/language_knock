import sys
if __name__ == '__main__':
    f = open('hightemp.txt')
    target = f.read().strip()
    f.close()
    N = int(sys.argv[1])
    target_list = target.split('\n')
    output = ''
    for i in range(len(target_list)):
        if i >= N:
            break
        output += target_list[i] + '\n'
    print(output.strip())
