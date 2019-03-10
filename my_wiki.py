def generate_basic_info(target):
    output = {}
    flag = 0
    for line in target.split('\n'):
        if '{{基礎情報' in line:
            flag = 1
        if line == '}}':
            flag = 0
        if flag == 0:
            continue
        if line[0] != '|':
            continue
        tmp = line[1:].split('=')
        output[tmp[0].strip()] = '='.join(tmp[1:]).strip()
    return output


if __name__ == '__main__':
    pass
