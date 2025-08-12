.. _fastqc:

FASTQC: Raw FASTQ Quality Control
=================================

**Purpose:**
The goal of FASTQ Quality Control is to assess the base quality, GC distribution, and potential contamination in sequencing data before downstream processing.

DRAGEN includes a FastQC module that runs independently of alignment, ensuring the integrity of raw input data.

Overview of FASTQ QC
---------------------
FASTQ files contain raw reads from sequencers, usually in paired-end format. Before alignment, it's essential to evaluate read quality using FastQC to identify any issues like low base quality, adapter contamination, or GC bias.

Steps to Run QC
---------------

Command Example:

.. code-block:: bash

    dragen --fastqc-only=true \
           -1 sample_R1.fastq.gz \
           -2 sample_R2.fastq.gz \
           --output-directory fastqc_output \
           --output-file-prefix sample_qc

Expected Outputs:
-----------------
- `sample_qc.fastqc_metrics.csv`

Key QC Metrics:
---------------
- Read Mean Quality
- Positional Base Quality
- GC Content
- Adapter Content

QC Review Guidelines:
---------------------
- Check for high-quality average scores across positions.
- Evaluate GC content consistency with expected genome distribution.
- Confirm low adapter contamination.