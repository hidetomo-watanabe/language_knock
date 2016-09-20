import my_ngram
if __name__ == '__main__':
    target1 = 'paraparaparadise'
    target2 = 'paragraph'
    X = my_ngram.generateNGram(target1, 2, 'char')
    Y = my_ngram.generateNGram(target2, 2, 'char')
    output_or = list(set(X + Y))
    output_and = []
    for x in X:
        if x in Y:
            output_and.append(x)
    output_not_and = []
    for tmp in output_or:
        if tmp not in output_and:
            output_not_and.append(tmp)
    print('or: %s' % output_or)
    print('and: %s' % output_and)
    print('not and: %s' % output_not_and)
    if 'se' in X:
        print('se in X')
    if 'se' in Y:
        print('se in Y')
