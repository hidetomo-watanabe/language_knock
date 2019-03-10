import re
from subprocess import Popen, PIPE
import my_wiki
if __name__ == '__main__':
    cmd = 'python -u 20.py'
    p = Popen(cmd.strip().split(' '), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    england_text = out.decode('utf-8')
    tmp_json = my_wiki.generate_basic_info(england_text)
    output = {}
    for key, value in tmp_json.items():
        tmp_value = value
        match_obj = re.search(r'\'+[^\']*\'+', tmp_value)
        while match_obj:
            tmp = tmp_value[match_obj.start():match_obj.end()]
            tmp_conv = tmp.replace('\'', '')
            tmp_value = tmp_value.replace(tmp, tmp_conv)
            match_obj = re.search(r'\'+[^\']*\'+', tmp_value)

        match_obj = re.search(r'\[\[[^\[\]]*\]\]', tmp_value)
        while match_obj:
            tmp = tmp_value[match_obj.start():match_obj.end()]
            tmp_conv = tmp.replace('[[', '').replace(']]', '')
            if '|' in tmp_conv:
                tmp_conv = tmp_conv.split('|')[0]
                if '#' in tmp_conv:
                    tmp_conv = tmp_conv.split('#')[0]
            tmp_value = tmp_value.replace(tmp, tmp_conv)
            match_obj = re.search(r'\[\[[^\[\]]*\]\]', tmp_value)

        match_strs = [r'<ref.*/>', r'<ref.*/ref>']
        for match_str in match_strs:
            match_obj = re.search(match_str, tmp_value)
            while match_obj:
                tmp = tmp_value[match_obj.start():match_obj.end()]
                tmp_conv = ''
                tmp_value = tmp_value.replace(tmp, tmp_conv)
                match_obj = re.search(match_str, tmp_value)
        output[key] = tmp_value
    for key, value in output.items():
        print('%s: %s' % (key, value))
