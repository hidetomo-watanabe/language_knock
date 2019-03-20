import sys
if __name__ == '__main__':
    text = sys.stdin.read()
    result = text.strip().replace(' ', '\n')
    print(result)
