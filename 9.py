import random
if __name__ == '__main__':
    target = 'I couldn\'t believe that \
I could actually understand what I was reading \
: the phenomenal power of the human mind .'
    output = ''
    for word in target.split(' '):
        if len(word) <= 4:
            output += word + ' '
            continue
        output += word[0] + \
            ''.join(random.sample(word[1:-1], len(word[1:-1]))) + \
            word[-1] + ' '
    print(output.strip())
