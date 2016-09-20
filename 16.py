import sys
if __name__ == '__main__':
    f = open('hightemp.txt')
    target = f.read().strip()
    f.close()
    N = int(sys.argv[1])
    target_list = target.split('\n')
    labels = ['aa', 'ab', 'ac', 'ad']
    output = {}
    label_count = 0
    for i in range(len(target_list)):
        label = labels[label_count]
        if i >= N * (label_count + 1):
            label_count += 1
            label = labels[label_count]
        if label not in output:
            output[label] = []
        output[label].append(target_list[i])
    for key, value in output.items():
        f = open('tmp' + key, 'w')
        f.write('\n'.join(value))
        f.close()
