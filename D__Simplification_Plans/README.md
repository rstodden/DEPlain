# DEplain: Simplification Plan of Documents

In the alignments of DEplain-APA and DEplain-WEB, the complex documents are fully aligned with the simplified documents. This means the alignments also reflect deletions and additions. The published  alignment of each document corresponds to the sentence-wise alignment of one human annoator on one document. 
The publication of the full document alignments, also enhance the option for example: 

1) to build a simplification plan for document-level simplification using sequence labeling (see [Cripwell et al. 2023](https://aclanthology.org/2023.eacl-main.70/)), 
2) to include preceding and following sentences for context-aware sentences simplification (see [Sun et al. 2020](https://aclanthology.org/2020.coling-main.121/)), or 
3) to use identical pairs and additions as augmented data during training (see [Palmero Aprosio et al. 2019](https://aclanthology.org/W19-2305/)).

The here published alignments only correspong to the manual sentence-wise alignment and not the one by the alignment methods.


## Data Format

For each document or each one simplification plan, one file exist. The files are named by their pair_id (the same pair_id is also assigned to the data in the document and the sentence corpus).

The files contain one line pair simplification pair where one side of the pair (either original or simplified text) can be empty. 

In the last column the alignment relation between the original and the simplified text is described. The alignment relations can be described as follows:

- aligned (n:m): all pairs which are manually aligned on the sentence level. In the brackets, the number of sentences of the original (n) and simplified (m) texts are specified. In this case, n and m are equal or greather than 1. 
- aligned (removed): the pair was manually aligned but was deleted from the sentence-level corpus (e.g., if the pair occurs more than once in the dataset). The number of original sentences and simplified sentences is not specified.
- identical: a sentence of the original document is exactly copied to the simplified document, both sentences are identical. The original sentence was not simplified, but just copied, maybe because it is already easy to read.
- identical (removed): a sentence of the original document is exactly copied to the simplified document, both sentences are identical. However, the pair was deleted from the sentence-level corpus.
- deletion: during the manual alignment, this sentence of the original document was not aligned. Hence, we can interprete that this sentence was deleted and do not occur in a similar way in the simplified document. 
- addition: during the manual alignment, this sentence of the simplified document was not aligned. Hence, we can interprete that this sentence was added and do not occur in a similar way in the original document.

Each file contains the following columns:

| data field                                      | data field description                                                                                |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `original`                                      | an original text from the source dataset                                                              |
| `simplification`                                | a simplified text from the source dataset                                                             |
| `pair_id`                                       | document pair id                                                                                      |
| `original_id `                                  | id of sentence(s) of the original text                                                                |
| `simplification_id `                            | id of sentence(s) of the simplified text                                                              |
| `domain `                                       | text domain of the document pair                                                                      |
| `corpus `                                       | subcorpus name                                                                                        |
| `simple_url `                                   | origin URL of the simplified document                                                                 |
| `complex_url `                                  | origin URL of the simplified document                                                                 |
| `language_level_simple `                        | required CEFR language level to understand the simplified document                                    |
|  `language_level_original `                     | required CEFR language level to understand the original document                                      ||
| `author`                                        | author (or copyright owner) of the simplified document                                                |
| `simple_title `                                 | title of the simplified document                                                                      |
| `complex_title `                                | title of the original document                                                                        |
| `license `                                      | license of the data                                                                                   |
| `access_date`                 | data origin data or data when the HTML files were downloaded                                          |
| `rater`                                         | id of the rater who annotated the sentence pair                                                       |
| `alignment`                                     | type of alignment, e.g., aligned (n:m), deletion, identical, addition                                                        |


## License
- **DEplain-APA**: The dataset is provided for research purposes only. Please request access using the following form: [https://zenodo.org/record/7674560](https://zenodo.org/record/7674560)
- **DEplain-web**: The corpus includes the following licenses: [CC-BY-SA-3](https://creativecommons.org/licenses/by-sa/3.0/), [CC-BY-4](https://creativecommons.org/licenses/by/4.0), and [CC-BY-NC-ND-4](https://creativecommons.org/licenses/by-nc-nd/4.0). The corpus also include a "save_use_share" license, for these documents the data provider permitted us to share the data for research purposes.

## Citation
If you use part of this work, please cite our paper:


```
@inproceedings{stodden-etal-2023-deplain,
    title = "{DE}plain: A {G}erman Parallel Corpus with Intralingual Translations into Plain Language for Sentence and Document Simplification",
    author = "Stodden, Regina and Momen, Omar and Kallmeyer, Laura",
    booktitle = "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.acl-long.908",
    doi = "10.18653/v1/2023.acl-long.908",
    pages = "16441--16463",
}
```
