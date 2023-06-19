# DEPlain: DEplain-APA for Sentence Simplification

## Dataset Statement for DEplain-web

The dataset statement and the dataset can also be found on huggingface: [https://huggingface.co/datasets/DEplain/DEplain-web](https://huggingface.co/datasets/DEplain/DEplain-web).

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

- **Repository:** [DEplain-web GitHub repository](https://github.com/rstodden/DEPlain)
- **Paper:**  Regina Stodden, Momen Omar, and Laura Kallmeyer. 2023. ["DEplain: A German Parallel Corpus with Intralingual Translations into Plain Language for Sentence and Document Simplification."](https://arxiv.org/abs/2305.18939). In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Toronto, Canada. Association for Computational Linguistics.
- **Point of Contact:** [Regina Stodden](regina.stodden@hhu.de)

#### Dataset Summary

[DEplain-web](https://github.com/rstodden/DEPlain) [(Stodden et al., 2023)](https://arxiv.org/abs/2305.18939) is a dataset for the evaluation of sentence and document simplification in German. All texts of this dataset are scraped from the web. All documents were licenced with an open license. The simple-complex sentence pairs are manually aligned.
This dataset only contains a test set. For additional training and development data, please scrape more data from the web using a [web scraper for text simplification data](https://github.com/rstodden/data_collection_german_simplification) and align the sentences of the documents automatically using, for example, [MASSalign](https://github.com/ghpaetzold/massalign) by [Paetzold et al. (2017)](https://www.aclweb.org/anthology/I17-3001/).

#### Supported Tasks and Leaderboards

The dataset supports the evaluation of `text-simplification` systems. Success in this task is typically measured using the [SARI](https://huggingface.co/metrics/sari) and [FKBLEU](https://huggingface.co/metrics/fkbleu) metrics described in the paper [Optimizing Statistical Machine Translation for Text Simplification](https://www.aclweb.org/anthology/Q16-1029.pdf).

#### Languages

The texts in this dataset are written in German (de-de). The texts are in German plain language variants, e.g., plain language (Einfache Sprache) or easy-to-read language (Leichte Sprache).

#### Domains
The texts are from 6 different domains: fictional texts (literature and fairy tales), bible texts, health-related texts, texts for language learners, texts for accessibility, and public administration texts.

### Dataset Structure

#### Data Access

- The dataset is licensed with different open licenses dependent on the subcorpora.

#### Data Instances
- `document-simplification` configuration: an instance consists of an original document and one reference simplification.
- `sentence-simplification` configuration: an instance consists of an original sentence and one manually aligned reference simplification.
- `sentence-wise alignment` configuration: an instance consists of original and simplified documents and manually aligned sentence pairs. In contrast to the sentence-simplification configurations, this configuration contains also sentence pairs in which the original and the simplified sentences are exactly the same.


#### Data Fields

- `original`: an original text from the source datasets written for people with German skills equal to CEFR level B1
- `simplification`: a simplified text from the source datasets written for people with German skills equal to CEFR level A2
- more metadata is added to the dataset

  
#### Data Splits
DEplain-web contains a training set, development set and a test set. 
The dataset was split based on the license of the data. All manually-aligned sentence pairs with an open license are part of the test set. The document-level test set, also only contains the documents which are manually aligned. For document-level dev and test set the documents which are not aligned or not public available are used. For the sentence-level, the alingment pairs can be produced by automatic alignments (see [Stodden et al., 2023](https://arxiv.org/abs/2305.18939)).


|                            | Train  | Dev    | Test | Total |
| -----                      | ------ | ------ | ---- | ----- |
| Document Pairs            |  481  | 122  | 147  | 756
| Sentence Pairs  | 1281  | 313 | 1846 | 3440



| **subcorpus**              | **simple**  | **complex** | **domain**  | **description**                                                          | **\# doc.** |
|----------------------------------|------------------|------------------|------------------|-------------------------------------------------------------------------------|------------------|
| **EinfacheBücher**          | Plain German               | Standard German / Old German            | fiction          | Books in plain German                                                         | 15               |
| **EinfacheBücherPassanten** | Plain German               | Standard German / Old German            | fiction          | Books in plain German                                                         | 4                |
| **ApothekenUmschau**        | Plain German               | Standard German               | health           | Health magazine in which diseases are explained in plain German               | 71               |
| **BZFE**                    | Plain German               | Standard German               | health           | Information of the German Federal Agency for Food on good nutrition           | 18               |
| **Alumniportal*}**            | Plain German               | Plain German               | language learner | Texts related to Germany and German traditions written for language learners. | 137              |
| **Lebenshilfe**             | Easy-to-read German              | Standard German               | accessibility    |                                                                               | 49               |
| **Bibel**                   | Easy-to-read German              | Standard German               | bible            | Bible texts in easy-to-read German                                            | 221              |
| **NDR-Märchen    **         | Easy-to-read German              | Standard German / Old German            | fiction          | Fairytales in easy-to-read German                                             | 10               |
| **EinfachTeilhaben**        | Easy-to-read German              | Standard German               | accessibility    |                                                                               | 67               |
| **StadtHamburg**            | Easy-to-read German              | Standard German               | public authority | Information of and regarding the German city Hamburg                          | 79               |
| **StadtKöln**              | Easy-to-read German              | Standard German               | public authority | Information of and regarding the German city Cologne                          | 85               |

: Documents per Domain in DEplain-web.



| domain  | avg. | std. | interpretation | \# sents | \# docs |
|------------------|---------------|---------------|-------------------------|-------------------|------------------|
| bible            | 0.7011        | 0.31          | moderate                | 6903              | 3                |
| fiction          | 0.6131        | 0.39          | moderate                | 23289             | 3                |
| health           | 0.5147        | 0.28          | weak                    | 13736             | 6                |
| language learner | 0.9149        | 0.17          | almost perfect          | 18493             | 65               |
| all              | 0.8505        | 0.23          | strong                  | 87645             | 87               |

: Inter-Annotator-Agreement per Domain in DEplain-web-manual.

| operation | # documents | percentage |
|-----------|-------------|------------|
| rehphrase | 863         | 11.73      |
| deletion  | 3050        | 41.47      |
| addition  | 1572        | 21.37      |
| identical | 887         | 12.06      |
| fusion    | 110         | 1.5        |
| merge     | 77          | 1.05       |
| split     | 796         | 10.82      |
| in total  | 7355        | 100        |

: Information regarding Simplification Operations in DEplain-web-manual.

### Dataset Creation

#### Curation Rationale

Current German text simplification datasets are limited in their size or are only automatically evaluated. 
We provide a manually aligned corpus to boost text simplification research in German.

#### Source Data

##### Initial Data Collection and Normalization
The parallel documents were scraped from the web using a [web scraper for text simplification data](https://github.com/rstodden/data_collection_german_simplification).
The texts of the documents were manually simplified by professional translators. 
The data was split into sentences using a German model of SpaCy.
Two German native speakers have manually aligned the sentence pairs by using the text simplification annotation tool [TS-ANNO](https://github.com/rstodden/TS_annotation_tool) by [Stodden & Kallmeyer (2022)](https://aclanthology.org/2022.acl-demo.14/). 

##### Who are the source language producers?
The texts of the documents were manually simplified by professional translators. See for an extensive list of the scraped URLs see Table 10 in [Stodden et al. (2023)](https://arxiv.org/abs/2305.18939).

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

no bias is known.

#### Other Known Limitations

The dataset is provided under different open licenses depending on the license of each website were the data is scraped from. Please check the dataset license for additional information.

### Additional Information

#### Dataset Curators

DEplain-APA was developed by researchers at the Heinrich-Heine-University Düsseldorf, Germany. This research is part of the PhD-program ``Online Participation'', supported by the North Rhine-Westphalian (German) funding scheme ``Forschungskolleg''.

#### Licensing Information

The corpus includes the following licenses: CC-BY-SA-3, CC-BY-4, CC-BY-NC-ND-4, MIT.

#### Citation Information


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
