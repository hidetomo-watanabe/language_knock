import sys
if __name__ == '__main__':
    x = sys.argv[1]
    y = sys.argv[2]
    z = sys.argv[3]
    output = '%s時の%sは%s' % (x, y, z)
    print(output)
