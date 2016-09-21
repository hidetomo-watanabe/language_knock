import my_mecab
if __name__ == '__main__':
    output = my_mecab.generateMapping('neko.txt.mecab')
    print(output[:5])
