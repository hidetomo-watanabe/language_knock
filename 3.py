if __name__ == '__main__':
    target = 'Now I need a drink, \
alcoholic of course, \
after the heavy lectures involving quantum mechanics.'
    output = []
    for word in target.split(' '):
        output.append(len(word.replace(',', '')))
    print(output)
