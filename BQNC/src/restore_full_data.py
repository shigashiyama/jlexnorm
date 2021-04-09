#!python3

import sys


def sentence_reader(path):
    with open(path) as f:
        b_offset = 0
        sid = None
        text = ''
        spans = []
        words = []

        for line in f:
            line = line.strip('\n')

            if line.startswith('#'):
                sid = line.split('# ')[1].rstrip('\t')

            elif line:
                warray = line.split('\t')
                words.append(warray)
                token = warray[0]
                text += token
                e_offset = b_offset + len(token)
                spans.append((b_offset, e_offset))
                b_offset = e_offset

            else:
                yield sid, text, spans, words
                b_offset = 0
                sid = None
                text = ''
                spans = []
                words = []

        raise StopIteration                


def masked_sentence_reader(path):
    with open(path) as f:
        sid = None
        words = []

        for line in f:
            line = line.strip('\n')

            if line.startswith('#'):
                sid = line.split('# ')[1].rstrip('\t')

            elif line:
                warray = line.split('\t')
                b_offset, e_offset = warray[0].split('-')
                word = [(int(b_offset), int(e_offset))]
                word.extend(warray[1:])
                words.append(word)

            else:
                yield sid, words
                sid = None
                words = []

        raise StopIteration                


def run(orig_path, mask_path):
    for ment, oent in zip(masked_sentence_reader(mask_path), sentence_reader(orig_path)):
        msid, mwords = ment
        osid, otext, ospans, owords = oent
        if msid != osid:
            print('Error: SenID mismatched', file=sys.stderr)
            sys.exit()

        print('# {}'.format(msid))
        for mword in mwords:
            span = mword[0]
            token = otext[span[0]:span[1]]

            if span in ospans:
                j = ospans.index(span)
                oword = owords[j]

                pos   = oword[1] if mword[1] == '_' else mword[1]
                ctype = oword[2] if mword[2] == '_' else mword[2]
                cform = oword[3] if mword[3] == '_' else mword[3]
                pron  = oword[4] if mword[4] == '_' else mword[4]
                lemma = oword[6] if mword[5] == '_' else mword[5]
                lid   = oword[7] if mword[6] == '_' else mword[6]
                cate  = mword[7]
                nid   = mword[8]
                
            else:
                pos, ctype, cform, pron, lemma, lid, cate, nid = mword[1:]

            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
                token, pos, ctype, cform, pron, lemma, lid, cate, nid))
        print()


if __name__ == '__main__':
    orig_path = sys.argv[1]
    mask_path = sys.argv[2]
    run(orig_path, mask_path)
