# DEplain: German Sentence Simplification Data

For sentence simplification part of DEplain, we aligned both document simplification corpora, DEplain-APA and DEplain-WEB, also on the sentence level. All 483 available parallel documents of DEplain-APA
and 147 documents of DEplain-web are manually aligned on the sentence level with the assistance of a TS annotation tool ([Stodden & Kallmeyer, 2022](https://aclanthology.org/2022.acl-demo.14/)). Overall, 14,968 sentence pairs of 630 document pairs are manually aligned. 

To exemplify the usage of the manual alignments and to provide sentence-wise alignments for the unaligned documents of DEplain-WEB we evaluate different alignment algorithms (see [../C__Alignment_Algorithms](../C__Alignment_Algorithms)) on the manually aligned data. 

This directory contains:

- a link to the [manual sentence-wise alignments](./DEplain-APA-sent) of DEplain-APA, 
- the [manual sentence-wise alignments](./DEplain-APA-web-sent/manual)  of DEplain-web,  and
- the [automatic sentence-wise alignments](./DEplain-APA-web-sent/auto) of DEplain-web.

## Corpus Statistics

|   | Corpus Name Sent.                                              | # Original Sents | # Simple Sents. | Alignment | License      | # Sent. Pairs (train/dev/test) |
|---|----------------------------------------------------------------|------------------|-----------------|-----------|--------------|--------------------------------|
| 1 | [DEplain-APA-sent](./DEplain-APA-sent)                         | 25,607           | 26,471          | manual    | upon request | 13,122 (10,660/1,231/1,231)    |
| 2 | [DEplain-web-sent-manual-open](./DEplain-web-sent/manual/open)  | 6,138            | 6,402           | manual    | open         | 1,846  (-/-/1846)              |
| 3 | [DEplain-web-sent-auto-open](./DEplain-web-sent/auto/open)     | 7,087            | 7,760           | auto      | open         | 652 (514/138/-)                |
| 4 | [DEplain-web-sent-auto-closed](./DEplain-web-sent/auto/closed) | 12,847           | 18,068          | auto      | closed       | 942  (767/175/-)               |


## Annotation

### Alignment
The documents were aligned by two annotators. For the inter-annotator agreement see the table below. In the dataset, we provide only the alignments of one annotator per document, because otherwise sentence pairs would be repeated. 

### Inter-Annotator Agreement
| domain  | avg. | std. | interpretation | \# sents | \# docs |
|------------------|---------------|---------------|-------------------------|-------------------|------------------|
| news             | 0.7497        | 0.28          | moderate                | 25224             | 10                |
| bible            | 0.7011        | 0.31          | moderate                | 6903              | 3                |
| fiction          | 0.6131        | 0.39          | moderate                | 23289             | 3                |
| health           | 0.5147        | 0.28          | weak                    | 13736             | 6                |
| language learner | 0.9149        | 0.17          | almost perfect          | 18493             | 65               |
| all              | 0.8505        | 0.23          | strong                  | 87645             | 87               |

### Simplification Evaluation Aspects & Simplification Operations
Further annotation on the sentence simplification data, e.g., regarding grammaticality, simpliciy or simplification operations can be found here: [../F__Human_Annotations](../F__Human_Annotations).

### Alignment Types
We provide statistics regarding the alignment types in the manual aligned corpora. In the first table, we show the statistics on n:m alignments, where n and m are \> 0. 

| Name        | \# pairs | 1:1 (rephrase) | 1:n (split) | n:1 (merge) | n:m (fusion) |
|-------------|----------|----------------|-------------|-------------|--------------|
| DEplain-apa | 13122    | 9912           | 2360        | 382         | 468          |
| DEplain-web | 1846     | 863            | 796         | 77          | 110          |

In the second table, we show the statsitics on n:m aligned pairs, where n and m are ≤ 1.

| Name        | \# pairs | 1:1(identical) | 0:1(addition) | 1:0(deletion) |
|-------------|----------|----------------|---------------|---------------|
| DEplain-apa | 12353    | 2712           | 3964          | 5677          |
| DEplain-web | 5482     | 887            | 1572          | 3050          |


## Data Availability
The DEplain-web corpus is available in the current repository. Furthermore, the dataset is also available on Huggingface: [https://huggingface.co/datasets/DEplain/DEplain-web-sent](https://huggingface.co/datasets/DEplain/DEplain-web-sent).

## License
- **DEplain-APA**: The dataset is provided for research purposes only. Please request access using the following form: [https://zenodo.org/record/7674560](https://zenodo.org/record/7674560)
- **DEplain-web**: The corpus includes the following licenses: [CC-BY-SA-3](https://creativecommons.org/licenses/by-sa/3.0/), [CC-BY-4](https://creativecommons.org/licenses/by/4.0), and [CC-BY-NC-ND-4](https://creativecommons.org/licenses/by-nc-nd/4.0). The corpus also include a "save_use_share" license, for these documents the data provider permitted us to share the data for research purposes.
