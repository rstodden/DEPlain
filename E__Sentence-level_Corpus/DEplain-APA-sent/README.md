# DEPlain: DEplain-APA for Sentence Simplification
This directory contains the sentence-level data of DEplain-APA (DEplain-APA-sent).

The data of APA (Austrian Press Agency) is restricted for non-commercial research purposes. To get access to DEplain-APA please request the access via zenodo (https://zenodo.org/record/7674560).
Download the data and add the content with ```cp -r src/* target```.

# Dataset Statement for DEplain-APA
In the following, we provide a dataset for DEplain-APA (following Huggingface's data cards). 

### Table of Contents
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

### Dataset Description

- **Repository:** [DEplain-APA zenodo repository](https://zenodo.org/record/7674560)
- **Paper:** Regina Stodden, Momen Omar, and Laura Kallmeyer. 2023. ["DEplain: A German Parallel Corpus with Intralingual Translations into Plain Language for Sentence and Document Simplification."](https://arxiv.org/abs/2305.18939). In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Toronto, Canada. Association for Computational Linguistics.
- **Point of Contact:** [Regina Stodden](regina.stodden@hhu.de)

#### Dataset Summary

DEplain-APA [(Stodden et al., 2023)](https://arxiv.org/abs/2305.18939) is a dataset for the training and evaluation of sentence and document simplification in German. All texts of this dataset are provided by the Austrian Press Agency. The simple-complex sentence pairs are manually aligned.

#### Supported Tasks and Leaderboards

The dataset supports the training and evaluation of `text-simplification` systems. Success in this task is typically measured using the [SARI](https://huggingface.co/metrics/sari) and [FKBLEU](https://huggingface.co/metrics/fkbleu) metrics described in the paper [Optimizing Statistical Machine Translation for Text Simplification](https://www.aclweb.org/anthology/Q16-1029.pdf).

#### Languages

The text in this dataset is in Austrian German (`de-at`).

#### Domains
All texts in this dataset are news data.

## Dataset Structure

#### Data Access

- The dataset is licensed with restricted access for only academic purposes. To download the dataset, please request access on [zenodo](https://zenodo.org/record/7674560).

#### Data Instances
- `document-simplification` configuration: an instance consists of an original document and one reference simplification (in plain-text format).
- `sentence-simplification` configuration: an instance consists of  original sentence(s) and one manually aligned reference simplification (inclusing one or more sentences).


#### Data Fields

| data field                                      | data field description                                                                                |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `original`                                      | an original text from the source dataset                                                              |
| `simplification`                                | a simplified text from the source dataset                                                             |
| `pair_id`                                       | document pair id                                                                                      |
| `complex_document_id ` (on doc-level)           | id of complex document (-1)                                                                           |
| `simple_document_id ` (on doc-level)            | id of simple document (-0)                                                                            |
| `original_id ` (on sent-level)                  | id of sentence(s) of the original text                                                                |
| `simplification_id ` (on sent-level)            | id of sentence(s) of the simplified text                                                              |
| `domain `                                       | text domain of the document pair                                                                      |
| `corpus `                                       | subcorpus name                                                                                        |
| `simple_url `                                   | origin URL of the simplified document                                                                 |
| `complex_url `                                  | origin URL of the simplified document                                                                 |
| `simple_level ` or `language_level_simple `     | required CEFR language level to understand the simplified document                                    |
| `complex_level ` or  `language_level_original ` | required CEFR language level to understand the original document                                      |
| `simple_location_html `                         | location on hard disk where the HTML file of the simple document is stored                            |
| `complex_location_html `                        | location on hard disk where the HTML file of the original document is stored                          |
| `simple_location_txt `                          | location on hard disk where the content extracted from the HTML file of the simple document is stored |
| `complex_location_txt `                         | location on hard disk where the content extracted from the HTML file of the simple document is stored |
| `alignment_location `                           | location on hard disk where the alignment is stored                                                   |
| `simple_author `                                | author (or copyright owner) of the simplified document                                                |
| `complex_author `                               | author (or copyright owner) of the original document                                                  |
| `simple_title `                                 | title of the simplified document                                                                      |
| `complex_title `                                | title of the original document                                                                        |
| `license `                                      | license of the data                                                                                   |
| `last_access ` or `access_date`                 | data origin data or data when the HTML files were downloaded                                          |
| `rater`                                         | id of the rater who annotated the sentence pair                                                       |
| `alignment`                                     | type of alignment, e.g., 1:1, 1:n, n:1 or n:m                                                         |

  
#### Data Splits

DEplain-APA is randomly split into a training, development and test set. The training set of the sentence-simplification configuration contains only texts of documents which are part of the training set of document-simplification configuration and the same for dev and test sets.
The statistics are given below.


|                            | Train  | Dev    | Test | Total |
| -----                      | ------ | ------ | ---- | ----- |
| Document Pairs            |  387  | 48  | 48  |483 |
| Sentence Pairs  | 10660  | 1231 | 1231 | 13122|

Inter-Annotator-Agreement: 0.7497 (moderate).

Here, more information on simplification operations will follow soon.

### Dataset Creation

#### Curation Rationale

DEplain-APA was created to improve the training and evaluation of German document and sentence simplification. The data is provided by the same data provided as for the APA-LHA data. In comparison to APA-LHA (automatic-aligned), the sentence pairs of DEplain-APA are all manually aligned. Further, DEplain-APA aligns the texts in language level B1 with the texts in A2, which result in mostly mild simplifications.

Further DEplain-APA, contains parallel documents as well as parallel sentence pairs.

#### Source Data

##### Initial Data Collection and Normalization

The original news texts (in CEFR level B2) were manually simplified by professional translators, i.e. capito – CFS GmbH, and provided to us by the Austrian Press Agency.
All documents date back to 2019 to 2021. 
Two German native speakers have manually aligned the sentence pairs by using the text simplification annotation tool TS-ANNO. The data was split into sentences using a German model of SpaCy.

##### Who are the source language producers?
The original news texts (in CEFR level B2) were manually simplified by professional translators, i.e. capito – CFS GmbH. No other demographic or compensation information is known.

#### Annotations

##### Annotation process

The instructions given to the annotators are available [here](https://github.com/rstodden/TS_annotation_tool/tree/master/annotation_schema).

##### Who are the annotators?

The annotators are two German native speakers, who are trained in linguistics. Both were at least compensated with the minimum wage of their country of residence.
They are not part of any target group of text simplification.

#### Personal and Sensitive Information

No sensitive data.

### Considerations for Using the Data

#### Social Impact of Dataset

Many people do not understand texts due to their complexity. With automatic text simplification methods, the texts can be simplified for them. Our new training data can benefit in training a TS model.

#### Discussion of Biases

No bias is known.

#### Other Known Limitations

The dataset is provided for research purposes only. Please check the dataset license for additional information.

### Additional Information

#### Dataset Curators

Researchers at the Heinrich-Heine-University Düsseldorf, Germany, developed DEplain-APA. This research is part of the PhD-program `Online Participation` supported by the North Rhine-Westphalian (German) funding scheme `Forschungskolleg`.

#### Licensing Information

The dataset (DEplain-APA) is provided for research purposes only. Please request access using the following form: [https://zenodo.org/record/7674560](https://zenodo.org/record/7674560).

#### Citation Information

If you use part of this work, please cite our paper:


```
@inproceedings{stodden-etal-2023-deplain,
    title = "{DE}-plain: A German Parallel Corpus with Intralingual Translations into Plain Language for Sentence and Document Simplification",
    author = "Stodden, Regina  and
      Momen, Omar  and
      Kallmeyer, Laura",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    notes = "preprint: https://arxiv.org/abs/2305.18939",
}
```
This dataset card uses material written by [Juan Diego Rodriguez](https://github.com/juand-r) and [Yacine Jernite](https://github.com/yjernite).

