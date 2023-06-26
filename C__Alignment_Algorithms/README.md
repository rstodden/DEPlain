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

## Results

|                     |                                                                |    1:1    |               |                |                    |    n:m    |            |                |                    |
|---------------------|:--------------------------------------------------------------:|:-------------:|---------------|----------------|--------------------|:-------------:|------------|----------------|--------------------|
| **Name**       | **Description**                                           | **P**    | **R**    | **F1** | **F0.5** | **P**    | **R** | **F1** | **F0.5** |
| LHA                 | Hierarchical alignment using sentence embeddings similarity    | .94           | .41           | .57            | .747               | -             | -          | -              | -                  |
| **Sent-LaBSE** | Similar embeddings of Language-agnostic BERT transformer       | **.961** | .444          | .608           | **.780**      | -             | -          | -              | -                  |
| Sent-RoBERTa        | Similar embeddings of Cross English \& German RoBERTa          | .960          | .444          | .607           | .779               | -             | -          | -              | -                  |
| CATS-C3G            | Different similarity measures e.g n-grams (C3G)/word vectors   | .247          | **.553** | .342           | .278               | -             | -          | -              | -                  |
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
