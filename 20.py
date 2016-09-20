import json
if __name__ == '__main__':
    f = open('jawiki-country.json')
    target = f.read().strip()
    f.close()
    for line in target.split('\n'):
        tmp = json.loads(line)
        if tmp['title'] == 'イギリス':
            print(tmp['text'])
