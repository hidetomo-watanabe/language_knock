import my_cabocha
if __name__ == '__main__':
    with open('neko.txt.cabocha', 'r') as f:
        sentence_num = 0
        morphs = []
        chunks = []
        chunk_obj = None
        srcs_dict = {}
        for line in f.readlines():
            # 文節内容の行
            if '\t' in line:
                # 文節内容取得
                surface, tmp1 = line.split('\t')
                tmp2 = tmp1.split(',')
                pos = tmp2[0]
                pos1 = tmp2[1]
                base = tmp2[-3]
                morph_obj = my_cabocha.Morph(surface, base, pos, pos1)
                morphs.append(morph_obj)

                # 文末
                if surface == '。':
                    # 文章数追加
                    sentence_num += 1
            # 文節区切りの行
            elif ' ' in line:
                # 前のchunkにmorphsを代入
                if chunk_obj:
                    chunk_obj.morphs = morphs
                    chunks.append(chunk_obj)

                    # 係り元、係り先表示
                    dst_text = chunk_obj.get_text(no_symbol=True)
                    for src in chunk_obj.srcs:
                        src_text = chunks[src].get_text(no_symbol=True)
                        print(f'{src_text}\t{dst_text}')

                # 次のchunk初期化
                morphs = []
                tmp = line.split(' ')
                index = int(tmp[1])
                dst = int(tmp[2].replace('D', ''))
                if index in srcs_dict.keys():
                    srcs = srcs_dict[index]
                else:
                    srcs = []
                chunk_obj = my_cabocha.Chunk([], dst, srcs)
                # srcs保持
                if dst in srcs_dict.keys():
                    srcs_dict[dst].append(index)
                else:
                    srcs_dict[dst] = [index]
