import my_cabocha
if __name__ == '__main__':
    chunks = my_cabocha.generate_chunks('neko.txt.cabocha')
    for chunk_obj in chunks:
        # 述語、格表示
        if not chunk_obj.has_verb():
            continue
        # 述語
        for morph in chunk_obj.morphs:
            if morph.pos == '動詞':
                predicate = morph.base
                break
        for src in chunk_obj.srcs:
            # 格
            cases = []
            for morph in chunks[src].morphs:
                if morph.pos == '助詞':
                    cases.append(morph.base)
            if len(cases) == 0:
                continue
            print(f'{predicate}\t{" ".join(cases)}')
