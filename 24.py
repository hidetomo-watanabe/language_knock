from subprocess import Popen, PIPE
if __name__ == '__main__':
    cmd = 'python -u 20.py'
    p = Popen(cmd.strip().split(' '), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    england_text = out.decode('utf-8')
    output = []
    for line in england_text.split('\n'):
        if 'ファイル' in line:
            tmp = line.split('ファイル:')[1]
            tmp_diff = tmp.count(']]') - tmp.count('[[')
            if tmp_diff != 0:
                output.append(tmp.replace(']]', '', tmp_diff))
            else:
                output.append(tmp)
    print('\n'.join(output))
