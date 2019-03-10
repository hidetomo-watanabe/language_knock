import my_mecab
if __name__ == '__main__':
    output = my_mecab.generate_mapping('neko.txt.mecab')
    print(output[:5])
