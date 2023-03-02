.. _faq:


FAQ
===

**Does remarkit trim amino acids, nucleotides, or codons?**

remarkit trims amino acid and nucleotide alignments. Currently, remarkit does not trim codons. 

|

**Is there a website application of remarkit?**

Currently, remarkit is only a command line tool.

|

**If tree inference with no trim works well, why even trim?**

Tree inference with trimmed multiple sequence alignments is computationally efficient.
In other words, shorter alignments require less computational time and memory during tree
search. We found that remarkit reduced computation time by an average of 20%. As datasets
continuously become bigger, an alignment trimming algorithm that can reduce computational
time will be of great value. 

|

**I am having trouble install remarkit, what should I do?**

Please install remarkit using a virtual environment as directed in the installation instructions.
If you are still running into issues after installing in a virtual environment, please contact the
main software developer via email_ or twitter_.

.. _email: https://jlsteenwyk.com/contact.html
.. _twitter: https://twitter.com/jlsteenwyk

^^^^^
