if __name__ == '__main__':
    f = open('col1.txt')
    col1 = f.read().strip()
    f.close()
    f = open('col2.txt')
    col2 = f.read().strip()
    f.close()
    col1_list = col1.split('\n')
    col2_list = col2.split('\n')
    if len(col1_list) != len(col2_list):
        raise Exception('Invalid input')
    output = ''
    for i in range(len(col1_list)):
        output += col1_list[i] + '\t' + col2_list[i] + '\n'
    print(output.strip())
