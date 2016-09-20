from subprocess import Popen, PIPE
if __name__ == '__main__':
    cmd = 'python -u 20.py'
    p = Popen(cmd.strip().split(' '), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    england_text = out.decode('utf-8')
    output = []
    tmp = england_text.split('\n')
    for i in range(len(tmp)):
        line = tmp[i]
        if '==' in line:
            output.append({
                line.replace('=', ''): line.count('=') / 2 - 2
            })
    for section in output:
        for key, value in section.items():
            print('%s: %s' % (key, value))
