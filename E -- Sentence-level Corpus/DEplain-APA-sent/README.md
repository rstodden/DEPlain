# Dataset Statement for DEplain-APA
The dataset statement and the dataset can also be found on huggingface: [https://huggingface.co/datasets/DEplain/DEplain-APA](https://huggingface.co/datasets/DEplain/DEplain-APA).

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Repository:** [DEplain-APA zenodo repository](https://zenodo.org/record/7674560)
- **Paper:** Regina Stodden, Momen Omar, and Laura Kallmeyer. 2023. ["DEplain: A German Parallel Corpus with Intralingual Translations into Plain Language for Sentence and Document Simplification."](https://arxiv.org/abs/2305.18939). In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Toronto, Canada. Association for Computational Linguistics.
- **Point of Contact:** [Regina Stodden](regina.stodden@hhu.de)

### Dataset Summary

[DEplain-APA](https://zenodo.org/record/7674560) [(Stodden et al., 2023)](https://arxiv.org/abs/2305.18939) is a dataset for the training and evaluation of sentence and document simplification in German. All texts of this dataset are provided by the Austrian Press Agency. The simple-complex sentence pairs are manually aligned.

### Supported Tasks and Leaderboards

The dataset supports the training and evaluation of `text-simplification` systems. Success in this task is typically measured using the [SARI](https://huggingface.co/metrics/sari) and [FKBLEU](https://huggingface.co/metrics/fkbleu) metrics described in the paper [Optimizing Statistical Machine Translation for Text Simplification](https://www.aclweb.org/anthology/Q16-1029.pdf).

### Languages

The text in this dataset is in Austrian German (`de-at`).

### Domains
All texts in this dataset are news data.

## Dataset Structure

### Data Access

- The dataset is licensed with restricted access for only academic purposes. To download the dataset, please request access on [zenodo](https://zenodo.org/record/7674560).

### Data Instances
- `document-simplification` configuration: an instance consists of an original document and one reference simplification.
- `sentence-simplification` configuration: an instance consists of an original sentence and one manually aligned reference simplification.


### Data Fields

- `original`: an original text from the source datasets written for people with German skills equal to CEFR level B1
- `simplification`: a simplified text from the source datasets written for people with German skills equal to CEFR level A2
- more metadata is added to the dataset

  
### Data Splits

DEplain-APA is randomly split into a training, development and test set. The training set of the sentence-simplification configuration contains only texts of documents which are part of the training set of document-simplification configuration and the same for dev and test sets.
The statistics are given below.


|                            | Train  | Dev    | Test | Total |
| -----                      | ------ | ------ | ---- | ----- |
| Document Pairs            |   387 |  48 |  48 | 483
| Sentence Pairs  |  10660 | 1231 | 1231 | 13122


Here, more information on simplification operations will follow soon.

## Dataset Creation

### Curation Rationale

DEplain-APA was created to improve the training and evaluation of German document and sentence simplification. The data is provided by the same data provided as for the APA-LHA data. In comparison to APA-LHA (automatic-aligned), the sentence pairs of DEplain-APA are all manually aligned. Further, DEplain-APA aligns the texts in language level B1 with the texts in A2, which result in mostly mild simplifications.

Further DEplain-APA, contains parallel documents as well as parallel sentence pairs.

### Source Data

#### Initial Data Collection and Normalization

The original news texts (in CEFR level C2) were manually simplified by professional translators, i.e. capito – CFS GmbH, and provided to us by the Austrian Press Agency.
All documents date back to 2019 to 2021. 
Two German native speakers have manually aligned the sentence pairs by using the text simplification annotation tool TS-ANNO. The data was split into sentences using a German model of SpaCy.

#### Who are the source language producers?
The original news texts (in CEFR level C2) were manually simplified by professional translators, i.e. capito – CFS GmbH. No other demographic or compensation information is known.

### Annotations

#### Annotation process

The instructions given to the annotators are available [here](https://github.com/rstodden/TS_annotation_tool/tree/master/annotation_schema).

#### Who are the annotators?

The annotators are two German native speakers, who are trained in linguistics. Both were at least compensated with the minimum wage of their country of residence.
They are not part of any target group of text simplification.

### Personal and Sensitive Information

No sensitive data.

## Considerations for Using the Data

### Social Impact of Dataset

Many people do not understand texts due to their complexity. With automatic text simplification methods, the texts can be simplified for them. Our new training data can benefit in training a TS model.

### Discussion of Biases

No bias is known.

### Other Known Limitations

The dataset is provided for research purposes only. Please check the dataset license for additional information.

## Additional Information

### Dataset Curators

Researchers at the Heinrich-Heine-University Düsseldorf, Germany, developed DEplain-APA. This research is part of the PhD-program `Online Participation` supported by the North Rhine-Westphalian (German) funding scheme `Forschungskolleg`.

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

This dataset card uses material written by [Juan Diego Rodriguez](https://github.com/juand-r) and [Yacine Jernite](https://github.com/yjernite).

