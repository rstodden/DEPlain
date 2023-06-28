# DEplain: Alignment Algorithms

We couldn't align all documents of DEplain-web manually. Therefore, we experimented with different alignment algorithms to automatically the remaining documents as well as reproduce the data with closed licenses. Here, we present the modified code of the following alignment methods. In our experiments, MASSalign achieved the best results. If you want to reproduce our sentence-level DEplain-web corpus with closed licenses, we recommend also using MASSalign. For more information, please also read our paper.

## Alignment Algorithms
For our experiments, we used the following alignment methods. Please check out the linked repositories, for more details, the methods, and our adaptations.

- MASSalign: [https://github.com/rstodden/massalign_DE](https://github.com/rstodden/massalign_DE) (LGPL v3.0 license)
- CATS: [https://github.com/rstodden/SimpTextAlignPython_DE](https://github.com/rstodden/SimpTextAlignPython_DE) (MIT license)
- LHA: [https://github.com/omarTronto/lha_DE](https://github.com/omarTronto/lha_DE) (MIT license)
- Sent-LaBSE/RoBERTa: [https://github.com/omarTronto/sentence_transformer_alignment_DE](https://github.com/omarTronto/sentence_transformer_alignment_DE) (MIT license)
- VecAlign: [https://github.com/thompsonb/vecalign](https://github.com/thompsonb/vecalign) (Apache License 2.0)
- BERTalign: [https://github.com/omarTronto/bertalign_DE](https://github.com/omarTronto/bertalign_DE)  (GNU General Public License v3.0)


## Adaptations to existing Alignment Algorithms
We adapted all alignment algorithms with respect to their language resources. For our purpose, we added, for example, German word embeddings or set the language of NLTK to German. If you change the language to your language of interest, you might use the alignment methods also for other languages than German (or previously English).

## Data
For our experiments, we used the subcorpus od DEplain-web that has manual alignments and is open for sharing. The dataset comprises 147 aligned pairs of documents, these complex-simple document pairs were split into 6,138 and 6,402 sentences respectively. The manual alignment of these sentences resulted in 2,741 alignments, comprising 1,750 1:1 alignments (out of which are 887 identical pairs), 804 1:m alignments, 77 n:1 alignments, and 110 n:m alignments. This version also contains the identical sentence pairs (see [DEplain_web_alignment.csv](./DEplain_web_alignment.csv)), which were removed during cleaning in the version of the subcorpus used for automatic text simplification (see [E__Sentence-level_Corpus/DEplain-web-sent/manual/open](../E__Sentence-level_Corpus/DEplain-web-sent/manual/open)). 

For aligning the test documents, we provide three files per document, i.e., a src-file with all complex sentences, a tgt-file with all simplified sentences, and a json-file with the meta data of the corresponding document. These document pairs can be automatically generated using `csv2dir.py` and the document data with sentence splits [B__Document-level_Corpus/DEplain-web-doc/manual/open/sentence-split/test.csv](../B__Document-level_Corpus/DEplain-web-doc/manual/open/sentence-split/test.csv). Each resulting file is named by its pair id, which can be also found in the other subcorpora of DEplain. Some of the alignment methods require a different input format, please refer to the code of the methods for more information.

For evaluation of the alignments, we provide two parallel files which comprise all alignments of all parallel documents of the test set, i.e., a src-file with one line per alignment pair (including only the original sentences) and a tgt-file with one line per alignment pair (including only the simplified sentences). These files do not include 1-0 (deletions) and 0-1 alignments (additions). Additinally, we also add the parallel sentence pairs in a csv-file including the meta data.



## Results
The output alignments on the test data are available in [outputs/](./outputs/). Please use `python3 evaluate.py` to calculate the F-Scores.

|                     |                                                                |    1:1    |               |                |                    |    n:m    |            |                |                    |
|---------------------|:--------------------------------------------------------------:|:-------------:|---------------|----------------|--------------------|:-------------:|------------|----------------|--------------------|
| **Name**       | **Description**                                           | **P**    | **R**    | **F1** | **F0.5** | **P**    | **R** | **F1** | **F0.5** |
| LHA                 | Hierarchical alignment using sentence embeddings similarity    | .94           | .41           | .57            | .747               | -             | -          | -              | -                  |
| **Sent-LaBSE** | Similar embeddings of Language-agnostic BERT transformer       | **.961** | .444          | .608           | **.780**      | -             | -          | -              | -                  |
| Sent-RoBERTa        | Similar embeddings of Cross English \& German RoBERTa          | .960          | .444          | .607           | .779               | -             | -          | -              | -                  |
| CATS-C3G            | Different similarity measures e.g n-grams (C3G)/word vectors   | .237          | **.553** | .332           | .267               | -             | -          | -              | -                  |
| VecAlign            | Multilingual aligner based on mulitlingual sentence embeddings | .271          | .404          | .323           | .290               | .260          | .465       | .333           | .285               |
| BERTalign           | Allows sentence-transformer methods produce n:m alignments     | .743          | .465          | .572           | .664               | .387          | .561       | .458           | .412               |
| **MASSalign**  | A vicinity-driven approach with a TF-IDF similarity matrix     | .846          | .477          | **.610**  | .733               | **.819** | .509       | **.628**  | **.730**      |


## License
The parts of the work are licensed under different licenses. Please see the corresponding repositories for more information on the license per alignment method.

## Citation
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
