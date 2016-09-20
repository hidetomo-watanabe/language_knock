if __name__ == '__main__':
    target = 'パタトクカシーー'
    output = ''
    for i in range(len(target)):
        if i % 2 == 0:
            output += target[i]
    print(output)
