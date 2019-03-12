import my_cabocha
if __name__ == '__main__':
    chunks = my_cabocha.generate_chunks('neko.txt.cabocha')
    for chunk_obj in chunks:
        # 係り元、係り先表示
        if not chunk_obj.has_verb():
            continue
        dst_text = chunk_obj.get_text(no_symbol=True)
        for src in chunk_obj.srcs:
            if not chunks[src].has_noun():
                continue
            src_text = chunks[src].get_text(no_symbol=True)
            print(f'{src_text}\t{dst_text}')
