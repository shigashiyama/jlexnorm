BCCWJ_PATH=/path/to/BCCWJ/

OC_PATH=$BCCWJ_PATH/Disk4/TSV_SUW_OT/OC/OC.txt
OY_PATH=$BCCWJ_PATH/Disk4/TSV_SUW_OT/OY/OY.txt

mkdir -p tmp
python src/extract_bccwj_sentences.py $OC_PATH tmp/org_OC.txt data/sentence_ids.txt
python src/extract_bccwj_sentences.py $OY_PATH tmp/org_OY.txt data/sentence_ids.txt
cat tmp/org_OC.txt tmp/org_OY.txt > tmp/org_OCOY.txt
python src/restore_full_data.py tmp/org_OCOY.txt data/BQNC_masked.txt > data/BQNC_full.txt
