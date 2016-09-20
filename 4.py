if __name__ == '__main__':
    target = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. \
New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    nums = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    output = {}
    for i in range(len(target.split(' '))):
        word = target.split(' ')[i]
        if i + 1 in nums:
            output[i + 1] = word[:1]
        else:
            output[i + 1] = word[:2]
    print(output)
