if __name__ == '__main__':
    target1 = 'パトカー'
    target2 = 'タクシー'
    if len(target1) != len(target2):
        raise Exception('Invalid Input')
    length = len(target1)
    output = ''
    for i in range(length):
        output += target1[i]
        output += target2[i]
    print(output)
