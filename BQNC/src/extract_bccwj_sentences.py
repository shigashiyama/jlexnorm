#!python3

import sys


def run(input_file, output_file, sent_ids):
    fw = open(output_file, 'w')
    sent_counter = 0
    words = []

    with open(input_file) as f:
        for line in f:
            line        = line.rstrip('\n')
            array       = line.split('\t')
            doc_id      = array[1]
            tok_id      = array[4]
            bos_flag    = array[9]
            lex_item_id = array[11]
            lex_item    = array[12]
            pos         = array[16]
            conj_type   = array[17]
            conj_form   = array[18]
            w_lemma     = array[21]
            w_form      = array[22]
            surf        = array[23]
            read        = array[24]

            word = [w_form, pos, conj_type, conj_form, 
                    read, w_lemma, lex_item, lex_item_id]

            if bos_flag == 'B':
                sent_counter += 1

                if words:
                    target_flag = (now_doc_id, now_begin_idx) in sent_ids
                    if not target_flag:
                        now_doc_id = doc_id
                        now_begin_idx = tok_id
                        now_end_idx = tok_id
                        words = [word]
                        continue

                    text = ''.join([w[0] for w in words])
                    fw.write('# {}:{}-{}\n'.format(
                        now_doc_id, now_begin_idx, now_end_idx))
                    print('Extracted:', doc_id, now_begin_idx, now_end_idx, text, file=sys.stderr)
                    for w in words:
                        fw.write('\t'.join(w)+'\n')
                    fw.write('\n')
                    words = []

                now_doc_id = doc_id
                now_begin_idx = tok_id

            now_end_idx = tok_id
            words.append(word)


if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    sent_id_file = sys.argv[3]

    sent_ids = set()
    with open(sent_id_file) as f:
        for line in f:
            line  = line.rstrip('\n')

            if line.startswith('#'):
                continue
            elif line:
                array = line.split(':')
                docid = array[0]
                begin, _ = array[1].split('-')
                sent_ids.add((docid, begin))

    run(input_file, output_file, sent_ids)
