.. _alignment:

Alignment and Post-Alignment QC
===============================

**Purpose:**
To map sequencing reads to a reference genome and perform quality control on alignment outputs.

What is Alignment?
-------------------
Alignment is the process of mapping short sequencing reads to a known reference genome. It is a crucial step that ensures downstream variant calls are accurate and meaningful.

The DRAGEN alignment module offers high-performance alignment with optional duplicate marking and indexing, producing BAM files as output.

Steps to Perform Alignment
--------------------------

Command Example:

.. code-block:: bash

    dragen -r /ref_dir \
           -1 sample_R1.fastq.gz \
           -2 sample_R2.fastq.gz \
           --output-directory alignment_output \
           --output-file-prefix sample \
           --enable-map-align-output true \
           --enable-duplicate-marking true

Expected Outputs:
-----------------
- `sample.bam`: Sorted and aligned reads
- `sample.bam.bai`: BAM index file
- `sample.mapping_metrics.csv`: Alignment statistics

QC Review Guidelines:
---------------------
- % Mapped Reads > 95%
- Proper Pairing > 90%
- Low Duplication Rate
- High MAPQ (mapping quality)