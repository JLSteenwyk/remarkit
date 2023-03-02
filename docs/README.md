<p align="center">
  <a href="https://github.com/jlsteenwyk/remarkit">
    <img src="https://raw.githubusercontent.com/JLSteenwyk/remarkit/master/docs/_static/img/logo.jpg" alt="Logo" width="400">
  </a>
  <p align="center">
    <a href="https://jlsteenwyk.com/remarkit/">Docs</a>
    ·
    <a href="https://github.com/jlsteenwyk/remarkit/issues">Report Bug</a>
    ·
    <a href="https://github.com/jlsteenwyk/remarkit/issues">Request Feature</a>
  </p>
    <p align="center">
        <a href="https://lbesson.mit-license.org/" alt="License">
            <img src="https://img.shields.io/badge/License-MIT-blue.svg">
        </a>
        <a href="https://pypi.org/project/remarkit/" alt="PyPI - Python Version">
            <img src="https://img.shields.io/pypi/pyversions/remarkit">
        </a>
        <a href="https://github.com/JLSteenwyk/remarkit/actions" alt="Build">
            <img src="https://img.shields.io/github/workflow/status/jlsteenwyk/remarkit/CI/master">
        </a>
        <a href="https://codecov.io/gh/jlsteenwyk/remarkit" alt="Coverage">
          <img src="https://codecov.io/gh/jlsteenwyk/remarkit/branch/master/graph/badge.svg?token=0J49I6441V">
        </a>
        <a href="https://github.com/jlsteenwyk/remarkit/graphs/contributors" alt="Contributors">
            <img src="https://img.shields.io/github/contributors/jlsteenwyk/remarkit">
        </a>
        <a href="https://twitter.com/intent/follow?screen_name=jlsteenwyk" alt="Author Twitter">
            <img src="https://img.shields.io/twitter/follow/jlsteenwyk?style=social&logo=twitter"
                alt="follow on Twitter">
        </a>
    </p>
</p>

remarkit is a fast and flexible alignment trimming tool that keeps phylogenetically informative sites and removes others.<br /><br />
If you found remarkit useful, please cite *remarkit: a multiple sequence alignment trimming software for accurate phylogenomic inference*. bioRxiv. doi: [10.1101/2020.06.08.140384](https://www.biorxiv.org/content/10.1101/2020.06.08.140384v1).
<br /><br />


---


## Guide
[Quick Start](#quick-start)<br />
[Advanced Usage](#advanced-usage)<br />
[Performance Assessment](#performance-assessment)<br />
[FAQ](#faq)


---

## Quick Start
### 1) Installation
To install, use the following commands:
```shell
pip install remarkit
```
<br />

To install from source, use the following commands:
```shell
git clone https://github.com/JLSteenwyk/remarkit.git
cd remarkit/
make install
```
<br />

If you run into permission errors when executing *make install*, create a virtual environment for your installation:
```shell
git clone https://github.com/JLSteenwyk/remarkit.git
cd remarkit/
python -m venv .venv
source .venv/bin/activate
make install
```
Note, the virtual environment must be activated to use remarkit.
<br />

### 2) Usage
To use remarkit in its simpliest form, execute the following command:
```
remarkit <input>
```
Output file with the suffix ".remarkit"

<br />

---

### Advanced Usage
This section describes the various features and options of remarkit.<br />
\- [Modes](#modes)<br />
\- [Output](#output)<br />
\- [Log](#log)<br />
\- [Complementary](#complementary)<br />
\- [All options](#all-options)

<br />

### Modes
remarkit can be run with five different modes (gappy, kpic, kpic-gappy, kpi, and kpi-gappy), which are specified with the -m/--mode argument.<br /> 
*Default: 'gappy'*<br />
* gappy: trim all sites that are above a threshold of gappyness (default: 0.9)<br />
* kpic (alias: medium): keep only parismony informative and constant sites<br />
* kpic-gappy (alias: medium-gappy): a combination of kpic- and gappy-based trimming<br />
* kpi (alias: heavy): keep only parsimony informative sites<br />
* kpi-gappy (alias: heavy-gappy): a combination of kpi- and gappy-based trimming<br />
```
# gappy-based trimming
remarkit <input>
remarkit <input> -m gappy

# kpic-based trimming
remarkit <input> -m kpic
remarkit <input> -m medium

# kpic- and gappy-based trimming
remarkit <input> -m kpic-gappy
remarkit <input> -m medium-gappy

# kpi-based trimming
remarkit <input> -m kpi
remarkit <input> -m heavy

# kpi- and gappy-based trimming
remarkit <input> -m kpi-gappy 
remarkit <input> -m heavy-gappy
```

<br />

### Output

By default, output files will have the same name as the input file with the suffix ".remarkit"
appended to the name. Users can specify output file names with the -o option. 

```
# specify output
remarkit <input> -o <output>
```

<br />

### Log
It can be very useful to have information about the each position in an alignment. For example, this information could be used in alignment diagnostics, fine-tuning of trimming parameters, etc. To create the log file, use the -l/--log option. Using this option will create a four column file with the suffix '.remarkit.log'. *Default: off*
* col1: position in the alignment (starting at 1)
* col2: reports if site was trimmed or kept (trim or keep, respectively)
* col3: reports if the site is constant or not (Const or nConst), parsimony informative or not (PI or nPI), or neither (nConst, nPI)
* col4: reports the gappyness of the position (number of gaps / entries in alignment)
<br />

```
remarkit <input> -l
```
Output file with the suffix ".remarkit.log"

<br />

### Complementary
Having an alignment of the sequences that were trimmed can be useful for other analyses. To obtain an alignment of the sequences that were trimmed, use the -c/--complementary option. 
*Default: off*<br />

```
remarkit <input> -c
```
Output file with the suffix ".remarkit.complementary"

<br />

### All options
| Option        | Usage and meaning |
| ------------- | ------------------ |
| -h/--help     | Print help message |
| -v/--version  | Print software version |
| -o/--output   | Specify output file name |
| -m/--modes    | Specify trimming mode. *Default: gappy* |
| -g/--gaps     | Specify gappyness threshold (between 0 and 1). *Default: 0.9* |
| -if/--input_file_format | Specify input file format*. *Default: auto-detect* |
| -of/--input_file_format | Specify output file format*. *Default: input file type* |
| -l/--log      | Create a log file. *Default: off* |
| -c/--complementary      | Create a complementary alignment file. *Default: off* |

*Acceptable file formats include: [fasta](https://en.wikipedia.org/wiki/FASTA_format), [clustal](http://meme-suite.org/doc/clustalw-format.html), [maf](http://www.bx.psu.edu/~dcking/man/maf.xhtml), [mauve](http://darlinglab.org/mauve/user-guide/files.html), [phylip](http://scikit-bio.org/docs/0.2.3/generated/skbio.io.phylip.html), [phylip-sequential](http://rosalind.info/glossary/phylip-format/), [phylip-relaxed](https://www.hiv.lanl.gov/content/sequence/FORMAT_CONVERSION/FormatExplain.html), [stockholm](https://en.wikipedia.org/wiki/Stockholm_format)
<br />
<br />

---

## Performance Assessment
In brief, performance assessment and comparison of multiple trimming alignment software revealed that remarkit with nearly any mode is a top-performing software. Here, we provide greater detail into the empirical datasets used to assess alignment trimming performance. 
<p align="center">
  <a href="https://www.biorxiv.org/content/10.1101/2020.06.08.140384v1">
    <img src="https://raw.githubusercontent.com/JLSteenwyk/remarkit/master/docs/_static/img/Performance_summary.jpg" alt="Performance Summary" width="1000">
  </a>
</p>

**remarkit is a top-performing software for trimming multiple sequence alignments.** Across a total of 138,152 multiple sequence alignments (MSAs) from empirical (left) and simulated (right) datasets, desirability-based integration of accuracy and support metrics per MSA facilitated the comparison of relative software performance and revealed remarkit is a top-performing software. MSA trimming approaches are ordered along the x-axis from the highest-performing software to the lowest-performing software according to average desirability-based rank. Abbreviations of trimmers and parameters are as follows: remarkit: g = gappy mode; remarkit: kc = kpic; remarkit: kcg = kpic-gappy; remarkit: k = kpi mode; remarkit: kg = kpi-gappy mode; BMGE = BMGE default; BMGE 0.3 = 0.3 entropy threshold; BMGE 0.7 = 0.7 entropy threshold; trimAl: s = strict; trimAl: sp = strictplus; Noisy = default; Gblocks = default; No trim = no trimming.   

For additional performance details, please see the manuscript *remarkit: a multiple sequence alignment trimming software for accurate phylogenomic inference*. bioRxiv. doi: [10.1101/2020.06.08.140384](https://www.biorxiv.org/content/10.1101/2020.06.08.140384v1).

<br /><br /><br />

---

## FAQ

<strong>If tree inference with no trim works well, why even trim?</strong>

Tree inference with trimmed multiple sequence alignments is computationally efficient. In other words, shorter alignments require less computational time and memory during tree search. We found that remarkit reduced computation time by an average of 20%. As datasets continuously become bigger, an alignment trimming algorithm that can reduce computational time will be of great value. 

<br />

<strong>Does remarkit trim amino acids, nucleotides, or codons?</strong>

remarkit's trims amino acid and nucleotide alignments. Currently, remarkit does not trim codons. 

<br />

<strong>Is there a website version of remarkit?</strong>

Currently, there is not website version of remarkit.

<br />

---

## Developers
* [Jacob Steenwyk](https://jlsteenwyk.github.io/)<br />
* [Thomas Buida](https://tjbiii.com)<br />
<br />

## All Team Members
* [Jacob Steenwyk](https://jlsteenwyk.github.io/)<br />
* [Thomas Buida](https://tjbiii.com)<br />
* [Yuanning Li](https://scholar.google.com/citations?user=65ygCIsAAAAJ&hl=en&oi=ao)
* [Xing-Xing Shen](https://xingxingshen.github.io/)
* [Antonis Rokas](https://as.vanderbilt.edu/rokaslab/)
<br />
