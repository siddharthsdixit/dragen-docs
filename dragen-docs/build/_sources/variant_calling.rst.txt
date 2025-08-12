.. _variant_calling:

Variant Calling: SNVs and CNVs
==============================

**Purpose:**
Identify genetic variants such as SNVs (Single Nucleotide Variants) and CNVs (Copy Number Variants) from aligned sequencing reads.

What is Variant Calling?
------------------------
Variant calling involves detecting positions in the genome where a sample differs from the reference genome. These differences can be SNVs, insertions/deletions (INDELs), or larger structural changes like CNVs.

The DRAGEN variant caller is designed to handle germline, somatic, and de novo workflows efficiently.

Steps for Variant Calling
-------------------------

Command Example:

.. code-block:: bash

    dragen -r /ref_dir \
           -1 sample_R1.fastq.gz \
           -2 sample_R2.fastq.gz \
           --output-directory varcall_output \
           --output-file-prefix sample \
           --enable-variant-caller true \
           --enable-cnv true

Expected Outputs:
-----------------
- `sample.vcf.gz`: SNV calls
- `sample.cnv.vcf.gz`: CNV calls
- `vc_metrics.csv`, `cnv_metrics.csv`: Quality metrics

QC Review Guidelines:
---------------------
- QUAL > 30 for confident calls
- Evaluate CNV filters (e.g., cnvQual)
- Ensure GQ and DP fields reflect strong supporting evidence