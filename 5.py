import sys
import my_ngram
if __name__ == '__main__':
    target = sys.argv[1]
    n = int(sys.argv[2])
    mode = sys.argv[3]
    print(my_ngram.generate_ngram(target, n, mode))
