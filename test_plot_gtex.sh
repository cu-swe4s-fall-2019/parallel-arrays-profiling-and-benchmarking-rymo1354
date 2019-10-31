#!/bin/bash

test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_style pycodestyle plot_gtex.py
assert_no_stdout
run test_style pycodestyle data_viz.py
assert_no_stdout
run test_style pycodestyle test_plot_gtex.py
assert_no_stdout

echo "...bad gzip file..."
run bad_gzip python3 plot_gtex.py --gene_reads bad.gz --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTS --output_file test1.png
assert_exit_code 1
assert_stdout

echo "...bad text file..."
run bad_text python3 plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true --sample_attributes bad.txt --gene ACTA2 --group_type SMTS --output_file test1.png
assert_exit_code 1
assert_stdout

echo "...gene not in files..."
run bad_gene python3 plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTS --output_file test1.png
assert_exit_code 0
assert_no_stdout

echo "...group not in files..."
run bad_group python3 plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type BADBAD --output_file test1.png
assert_exit_code 1
assert_stdout

echo "...test boxplot..."
run box1 python3 plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTS --output_file test1.png
assert_exit_code 0
assert_no_stdout
if [ -f "test1.png" ]; then
    echo "test1.png successful"
    rm test1.png
fi

echo "...test boxplot..."
run box2 python3 plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTSD --output_file test2.png
assert_exit_code 0
assert_no_stdout
if [ -f "test2.png" ]; then
    echo "test2.png successful"
    rm test2.png
fi

echo "...test boxplot..."
run box3 python3 plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene SDHC --group_type SMTS --output_file test3.png
assert_exit_code 0
assert_no_stdout
if [ -f "test3.png" ]; then
    echo "test3.png successful"
    rm test3.png
fi


