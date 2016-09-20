from subprocess import Popen, PIPE
if __name__ == '__main__':
    cmd = 'python -u 20.py'
    p = Popen(cmd.strip().split(' '), stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    england_text = out.decode('utf-8')
    output = []
    for line in england_text.split('\n'):
        if 'Category' in line:
            output.append(line)
    print('\n'.join(output))
