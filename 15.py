import sys
if __name__ == '__main__':
    f = open('hightemp.txt')
    target = f.read().strip()
    f.close()
    N = int(sys.argv[1])
    re_target_list = list(reversed(target.split('\n')))
    tmp = []
    for i in range(len(re_target_list)):
        if i >= N:
            break
        tmp.append(re_target_list[i])
    output = '\n'.join(list(reversed(tmp)))
    print(output.strip())
