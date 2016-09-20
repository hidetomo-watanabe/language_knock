# coding: UTF-8
import sys


def generateNGram(target, n, mode):
    output = []
    if mode == 'word':
        words = target.split(' ')
        for i in range(len(words)):
            output.append(' '.join(words[i:i+n]))
    elif mode == 'char':
        chars = target.replace(' ', '')
        for i in range(len(chars)):
            output.append(''.join(chars[i:i+n]))
    return list(set(output))

if __name__ == '__main__':
    pass
