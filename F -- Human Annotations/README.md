# DEplain: Human Annotations on the Sentence Simplification Data

For manual evaluation of DEplain-APA-sent and DEplain-web-sent, more than 300  randomly sampled sentence-pairs were annotated (not automatically aligned, not automatically simplified). Each sentence-pair is annotated with respect to evaluation aspects on a Liekrt-scale (grammaticality, simplicity, etc.) and with respect to the operations performed during the simplification (e.g., lexical substitution, clause deletion, change of verb's voice, etc.).



## Data Format
The annotations are provided in csv-files, one file for ratings and one file for operations. Each line correspond to one manually aligned sentence pair (not automatically aligned, not automatically simplified). The first row contains the column headers. The first two columns contains the original and the simplified sentence. For the APA data, the texts of the original and simplification columns are removed due to data license restrictions. To rebuild the full data, please match the original_ids and simplification ids with of the annotation files with the sentence-wise alignment files or the simplification plan files.
Furthermore, one column exists for each rating aspect and each sub-sub-level operation. 


## Data Statistics

### Quality Assessment
To assess the quality of the manual alignments, two annotators rated > 300 random selected sentence pairs regarding the following aspects. We provide a statement per aspect on which the annotators are asked to agree or disagree on on a 5-point Liekrt scale. The aspects were rated on different Likert-scales (see line 3 of the following table). In the annotation files, one column per aspect exist.

- Overall simplicity: The simplified sentence is easier to understand than the original sentence.
- lexical simplicity: The words of the simplified sentence are easier to understand than the words of the original sentence.
- structural simplicity: The structure of the simplified sentence is easier to understand than the structure of the original sentence.
- meaning preservation: The simplified sentence adequately expresses the meaning of the original sentence, perhaps omitting the least important information.
- coherence: The (simplified|original) sentence is understandable without reading
the whole paragraph.
- ambiguity: The (simplified|original) sentence is ambiguous. It can be read in different ways. 
- grammaticality: The (simplified|original) sentence is fluent, and there are no grammatical errors.
- simplificity:The (simplified|original) sentence is easy to understand.


|              |            | Simplicity | LexSimp    | StructSimp | MeaningP.  |     Coherence     |                   |    Grammaticality   |                     |     Simplicity    |                   |
|-----------------------|------------|---------------------|---------------------|---------------------|---------------------|:-----------------:|-------------------|:-------------------:|---------------------|:-----------------:|-------------------|
|                       |            | sent. pair | sent. pair | sent. pair | sent. pair | complex  | simple   | complex    | simple     | complex  | simple   |
| corpus       | n | (-2 to +2) | (-2 to +2) | (-2 to +2) | (1 to 5)   | (1 to 5) | (1 to 5) | (-2 to +2) | (-2 to +2) | (1 to 5) | (1 to 5) |
| DEplain-apa | 46         | 0.57±0.86       | 0.28±0.54       | 0.5±0.81        | 4.33±0.97       | 3.26±1.6      | 3.54±1.54     | 1.96±0.29       | 2.0±0.0         | 4.39±0.77     | 4.72±0.46     |
| DEplain-web | 384        | 1.04±0.82       | 0.67±0.75       | 0.95±0.87       | 4.29±0.93       | 2.82±1.48     | 3.08±1.4      | 1.72±0.79       | 1.96±0.26       | 3.48±1.18     | 4.46±0.69     |
| news         | 46         | 0.57±0.86       | 0.28±0.54       | 0.5±0.81        | 4.33±0.97       | 3.26±1.6      | 3.54±1.54     | 1.96±0.29       | 2.0±0.0         | 4.39±0.77     | 4.72±0.46     |
| bible        | 155        | 1.39±0.68       | 0.98±0.78       | 1.28±0.77       | 4.34±0.84       | 2.12±1.22     | 2.63±1.22     | 1.45±1.06       | 1.92±0.35       | 2.97±1.27     | 4.44±0.72     |
| lang.        | 157        | 0.67±0.74       | 0.36±0.57       | 0.57±0.73       | 4.46±0.73       | 3.83±1.27     | 3.82±1.27     | 1.96±0.22       | 1.97±0.21       | 4.01±0.81     | 4.43±0.71     |
| fiction      | 72         | 1.1±0.95        | 0.69±0.78       | 1.08±1.02       | 3.82±1.29       | 2.08±1.06     | 2.42±1.33     | 1.75±0.71       | 2.0±0.0         | 3.42±1.16     | 4.56±0.58     |

: Results of the Ratings per Corpus and Domain.

### Simplification Process: Used Transformations/Operations to Simplify the Sentence
To get insights into the simplification process of the manual alignments, two annotators annotated > 300 random selected sentence pairs regarding their simplification operations. The full annotation schema can be found here: [https://github.com/rstodden/TS_annotation_tool/tree/master/annotation_schema](https://github.com/rstodden/TS_annotation_tool/tree/master/annotation_schema).

In the rating files, the operations are grouped by their 

- level (column ends with #): 
    - paragraph,
    - phrase/clause,
    - sentence,
    - word,
- sublevel (column ends with *), and
- subsublevel (column ends with +).
The operation columns contain the number how often the operation was annotated in the sentence pair. The (sub-)level columns are the sum of the (sub-)sub-levels.


## License
This work is licensed under [GPL-3.0 license](LICENSE).

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
