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
        output[key] = value.replace('\'', '')
    print(output)
