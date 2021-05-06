# BQNC (version 1.0)

Blog and Q&A site Normalization Corpus


## Requirements

- Python 3
- BCCWJ DVD version (https://ccd.ninjal.ac.jp/bccwj/en/) is required to construct the full data because this data does not include the original sentences.


## Files

~~~~
+-- run.sh               ... A script to merge annotation information into original sentences
+-- data
| +-- BQNC_masked.txt    ... Annotated sentences with masked words
| +-- BQNC_sform_ids.txt ... A list of standard form IDs for non-standard forms
| +-- sentence_ids.txt   ... A list of sentence IDs to be extracted
+-- src                  ... Python scripts called by run.sh
~~~~


## How to Use

Edit BCCWJ_PATH in run.sh and excute it. Then, data/BQNC_full.txt is generated.


## Data Format

Each line in BQNC_full.txt follows the format below. CType, CForm, Pron, Cate, and SForm indicate conjugation type, conjugation form, pronunciation, word categories, and standard form ID, respectively.

~~~~
Token   POS                CType   CForm        Pron  Lemma  LemmaID  Cate    SFormID
ねぇー  形容詞-非自立可能  形容詞  終止形-一般  ネー  無い   27442    音変化  27442:無い
~~~~

SFormID is defined in BQNC_sform_ids.txt as follows. (POS is not necessary information but included for ease of understanding.)

~~~~
SFormID     POS     SForms
27442:無い  形容詞  ない,無い
~~~~

POS sets and lemma IDs follw those of BCCWJ short unit word and UniDic.


## Citation

Please cite the paper below. A preprint for the paper is available at https://arxiv.org/abs/2104.03523

~~~~
@inproceedings{higashiyama2021,
      title = {User-Generated Text Corpus for Evaluating Japanese Morphological Analysis and Lexical Normalization},
      author = {Higashiyama, Shohei and Utiyama, Masao and Watanabe, Taro and Sumita, Eiichiro},
      booktitle = {Proceedings of the 2019 Annual Conference of the North American Chapter of the Association for Computational Linguistics},
      month = June,
      year = 2021,
      publisher = {Association for Computational Linguistics}
}
~~~~
