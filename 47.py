import my_cabocha
if __name__ == '__main__':
    chunks = my_cabocha.generate_chunks('neko.txt.cabocha')
    for chunk_obj in chunks:
        # 述語、文節表示
        if not chunk_obj.has_verb():
            continue

        # 述語
        for morph in chunk_obj.morphs:
            if morph.pos == '動詞':
                predicate = morph.base
                break
        # 動詞に係る文節のうち、動詞に最も近いもの
        if len(chunk_obj.srcs) == 0:
            continue
        pre_predicate_morphs = chunks[chunk_obj.srcs[-1]].morphs
        # 文節が「サ変接続+を」なら述語に追加
        if len(pre_predicate_morphs) != 2:
            continue
        pre_predicates = []
        morph0 = pre_predicate_morphs[0]
        if morph0.pos == '名詞' and morph0.pos1 == 'サ変接続':
            pre_predicates.append(morph0.base)
        morph1 = pre_predicate_morphs[1]
        if morph1.pos == '助詞' and morph1.base == 'を':
            pre_predicates.append(morph1.base)
        if len(pre_predicates) != 2:
            continue
        predicate = ''.join(pre_predicates) + predicate

        # 述語に係る文節
        # 格
        cases = []
        # 項
        texts = []
        for i, src in enumerate(chunk_obj.srcs):
            # 述語に含めた文節は無視
            if i == (len(chunk_obj.srcs) - 1):
                continue
            add_text = False
            for morph in chunks[src].morphs:
                if morph.pos == '助詞':
                    cases.append(morph.base)
                    add_text = True
            if add_text:
                texts.append(chunks[src].get_text())
        if len(cases) == 0 or len(texts) == 0:
            continue

        print(f'{predicate}\t{" ".join(cases)}\t{" ".join(texts)}')
