import re
from subprocess import Popen, PIPE
import my_wiki
if __name__ == '__main__':
    cmd = 'python -u 20.py'
    p = Popen(cmd.strip().split(' '), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    england_text = out.decode('utf-8')
    tmp_json = my_wiki.generateBasicInfo(england_text)
    output = {}
    for key, value in tmp_json.items():
        match_obj = re.search(r'\'+.*\'+', value)
        if not match_obj:
            tmp_value = value
        else:
            tmp = value[match_obj.start():match_obj.end()]
            tmp_conv = tmp.replace('\'', '')
            tmp_value = value.replace(tmp, tmp_conv)

        match_obj = re.search(r'\[\[.*\]\]', tmp_value)
        if match_obj:
            tmp = tmp_value[match_obj.start():match_obj.end()]
            tmp_conv = tmp.replace('[[', '').replace(']]', '')
            if '|' in tmp_conv:
                tmp_conv = tmp_conv.split('|')[0]
                if '#' in tmp_conv:
                    tmp_conv = tmp_conv.split('#')[0]
            tmp_value = tmp_value.replace(tmp, tmp_conv)
        output[key] = tmp_value
    print(output)
    for tmp in output.items():
        print(tmp)
