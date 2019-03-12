import CaboCha


def generate_cabocha(path):
    with open(path, 'r') as f:
        text = f.read()
    c = CaboCha.Parser()
    output = c.parse(text).toString(CaboCha.FORMAT_LATTICE)
    return output


def generate_chunks(path):
    with open(path, 'r') as f:
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
                morph_obj = Morph(surface, base, pos, pos1)
                morphs.append(morph_obj)
            # 文節区切りの行
            elif ' ' in line:
                # 前のchunkにmorphsを代入
                if chunk_obj:
                    chunk_obj.morphs = morphs
                    chunks.append(chunk_obj)

                # 次のchunk初期化
                morphs = []
                tmp = line.split(' ')
                index = int(tmp[1])
                dst = int(tmp[2].replace('D', ''))
                if index in srcs_dict.keys():
                    srcs = srcs_dict[index]
                else:
                    srcs = []
                chunk_obj = Chunk([], dst, srcs)
                # srcs保持
                if dst in srcs_dict.keys():
                    srcs_dict[dst].append(index)
                else:
                    srcs_dict[dst] = [index]
    return chunks


class Morph(object):
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def display(self):
        print(
            f'surface: {self.surface}\t' +
            f'base: {self.base}\t' +
            f'pos: {self.pos}\t' +
            f'pos1: {self.pos1}')


class Chunk(object):
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def get_text(self, no_symbol=False):
        text = ''
        for morph in self.morphs:
            if no_symbol and morph.pos == '記号':
                continue
            text += morph.surface
        return text

    def display(self):
        text = self.get_text()
        print(
            f'text: {text}\t' +
            f'dst: {self.dst}\t' +
            f'srcs: {self.srcs}')


if __name__ == '__main__':
    output = generate_cabocha('neko.txt')
    with open('neko.txt.cabocha', 'w') as f:
        f.write(output)
