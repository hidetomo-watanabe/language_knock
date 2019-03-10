import my_cabocha
if __name__ == '__main__':
    with open('neko.txt.cabocha', 'r') as f:
        sentence_num = 0
        for line in f.readlines():
            # 文節区切り
            if ' ' in line:
                continue

            # 文節内容取得
            surface, morph_val = line.split('\t')
            pos, pos1, _, _, _, _, base, _, _ = morph_val.split(',')

            # 3文目
            if sentence_num == 2:
                morph_obj = my_cabocha.Morph(surface, base, pos, pos1)
                morph_obj.display()
            if sentence_num > 2:
                break

            # 文章数追加
            if surface == '。':
                sentence_num += 1
