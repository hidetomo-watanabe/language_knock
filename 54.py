import json
import corenlp
if __name__ == '__main__':
    with open('./nlp.txt', 'r') as f:
        text = f.read()
    corenlp_dir = "/usr/local/lib/stanford-corenlp-full-2013-06-20/"
    parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)
    # 一度に処理すると、途中で処理が切れる
    for line in text.split('\n'):
        result = json.loads(parser.parse(line))
        for sentence_data in result['sentences']:
            for word_data in sentence_data['words']:
                word = word_data[0]
                lemma = word_data[1]['Lemma']
                pos = word_data[1]['PartOfSpeech']
                print(f'{word}\t{lemma}\t{pos}')
