import json
import corenlp
if __name__ == '__main__':
    with open('./nlp.txt', 'r') as f:
        text = f.read()
    corenlp_dir = "/usr/local/lib/stanford-corenlp-full-2013-06-20/"
    parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)
    for line in text.split('\n'):
        result = json.loads(parser.parse(line))
        for sentence in result['sentences']:
            for word in sentence['words']:
                print(word[0])
