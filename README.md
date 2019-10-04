# parallel-arrays-profiling-and-benchmarking
Parallel Arrays, Profiling, and Benchmarking

## Files:
- https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
- https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

## .travis.yml Status
![](https://travis-ci.com/cu-swe4s-fall-2019/parallel-arrays-profiling-and-benchmarking-rymo1354.svg?branch=master)

## Usage
`plot_gtex.py` is the main program used to generate boxplots from the GTEx datasets in this repository. Example usage of `plot_gtex.py`:

```
`python3 plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTS --output_file ACTA2.png`
```

## Profiling and Benchmarking
Profiling and benchmarking was performed using cProfile:
```
python -m cProfile -s time plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTS --output_file ACTA2.png
```
The `linear_search` call in `plot_gtex.py` took a tottime of 20.315 seconds compared with the `binary_search` call in `plot_gtex.py` which took a tottime of 0.123 seconds. This is a marked increase in the runtime of the `plot_gtex.py` program.
 
## Installation
To use this program, you need to have Python 3.6 installed
The dependencies of this program include: 
- numpy
- matplotlib
- pycodestyle

These can be installed in the command line using the following prompts: 
```
conda install -yes numpy
conda install -yes matplotlib
conda install -yes pycodestyle
conda install -yes python=3.6
