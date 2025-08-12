==============================
DRAGEN DNA Pipeline SVP Guide

.. _svp_index:

This section presents the Standard Validation Plan (SVP) for validating the DRAGEN DNA pipeline components, primarily using truth sets and quality metrics. It includes validation goals, test strategies, acceptance criteria, and QC benchmarks.

.. contents:: SVP Contents
:depth: 2

Overview

The Software Validation Plan (SVP) ensures the DRAGEN DNA pipeline performs with high accuracy, reproducibility, and reliability across datasets and environments. The SVP focuses on evaluating:

Raw read quality metrics

Mapping and alignment performance

Variant calling accuracy (SNV/CNV)

End-to-end runtime and resource efficiency

Validation Strategy and Approach

Use of NIST and NA12878 truth sets for variant call benchmarking

Comparison of pipeline output with expected results

Concordance metrics (Precision, Recall, F1-score)

Repeatability tests with same input

Reproducibility with different input conditions (depth, format)

QC Metrics to Evaluate

FASTQ QC: Mean Phred scores, adapter content, GC content

Alignment QC: % mapped reads, properly paired reads, MAPQ distribution

Variant QC (SNV): QUAL, GQ, QD scores; false positives/negatives

Variant QC (CNV): Copy ratios, filters applied, uniformity

Run Metrics: Total runtime, stage-wise time, temp storage usage

Expected Output Format

Validation will generate structured outputs like:

.vcf.gz (variant calls)

.bam / .bai (aligned reads)

*_metrics.csv (QC and time)

.seg.called.merged (CNV segments)

Acceptance Criteria Definition

SNV/INDEL concordance > 95% (vs truth set)

CNV detection: sensitivity > 90%, PPV > 90%

FASTQ mean quality > 30, adapter < 5%

Alignment rate > 95%

Properly paired reads > 90%

Variant call QUAL > 30 average

Contamination < 3%

Runtime < 25 mins for 30X genome

Summary and Outcome

