import sys
import nltk
if __name__ == '__main__':
    text = sys.stdin.read()
    ps = nltk.stem.porter.PorterStemmer()
    results = []
    for line in text.strip().split('\n'):
        results.append(f'{line}\t{ps.stem(line)}')
    print('\n'.join(results))
