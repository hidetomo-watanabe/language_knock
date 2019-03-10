import json
import requests
from subprocess import Popen, PIPE
import my_wiki
if __name__ == '__main__':
    cmd = 'python -u 20.py'
    p = Popen(cmd.strip().split(' '), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    england_text = out.decode('utf-8')
    filename = my_wiki.generate_basic_info(england_text)['国旗画像']
    api_url = 'https://en.wikipedia.org/w/api.php' + \
        '?format=json&action=query&prop=imageinfo&iiprop=url&titles=File:' + \
        filename.replace(' ', '%20')
    tmp_json = json.loads(requests.get(api_url).content.decode('utf-8'))
    for tmp in tmp_json['query']['pages'].values():
        if 'imageinfo' in tmp:
            image_url = tmp['imageinfo'][0]['url']
    print(image_url)
