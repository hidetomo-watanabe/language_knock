import sys


def cipher(target):
    output = ''
    for char in target:
        if char.islower():
            output += str(219 - ord(char))
        else:
            output += char
    return output


def decipher(target):
    output = ''
    tmp = ''
    for char in target:
        if char.isupper():
            output += char
        else:
            tmp += char
        if len(tmp) == 3:
            output += chr(219 - int(tmp))
            tmp = ''
    return output

if __name__ == '__main__':
    target = sys.argv[1]
    print(cipher(target))
    print(decipher(cipher(target)))
