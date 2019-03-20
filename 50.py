import re
if __name__ == '__main__':
    with open('./nlp.txt', 'r') as f:
        text = f.read()
    result = re.sub(r'(\.|;|:|\?|\!)( )([A-Z])', r'\1\2\n\3', text)
    print(result)
