# DEplain: German Document Simplification Data
We present two new TS corpora on the document level, DEplain-APA and DEplain-WEB, containing parallel documents in standard German and plain German. 

## Data Format
For each document-level dataset, we provide two different formats:
- plain text: plain documents per line without sentence split, and
- sentence split: documents per line with sentence split, each sentence is separated by "|||"


## Corpus Statistics

|   | Corpus Name Doc.                                                                      | License      | # Doc. Pairs (train/dev/test) | # Original Sents | # Simple Sents. |
|---|---------------------------------------------------------------------------------------|--------------|-------------------------------|------------------|-----------------|
| 1 | [DEplain-APA-doc](./B__Document-level_Corpus/DEplain-APA-doc)                         | upon request | 483  (387/48/48)              | 25,607           | 26,471          |
| 2 | [DEplain-web-doc-manual-open](./B__Document-level_Corpus/DEplain-web-doc/manual/open) | open         | 147  (-/-/147)                | 6,138            | 6,402           |
| 3 | [DEplain-web-doc-auto-open](./B__Document-level_Corpus/DEplain-web-doc/auto/open)     | open         | 249 (199/50/-)                | 7,087            | 7,760           |
| 4 | [DEplain-web-doc-auto-closed](./B__Document-level_Corpus/DEplain-web-doc/auto/closed) | closed       | 360 (288/72/-)                | 12,847           | 18,068          |
|   | In total                                                                              | mixed        | 1,239 (874/170/195)           | 51,681           | 58,701          |

## Data Availability
The DEplain-web corpus is available in the current repository. Furthermore, the dataset is also available on Huggingface:

- [DEplain-web-doc-manual](https://huggingface.co/datasets/DEplain/DEplain-web-doc-manual)
- [DEplain-web-doc-auto](https://huggingface.co/datasets/DEplain/DEplain-web-doc-auto)

## License
- **DEplain-APA**: The dataset is provided for research purposes only. Please request access using the following form: [https://zenodo.org/record/7674560](https://zenodo.org/record/7674560)
- **DEplain-web**: The corpus includes the following licenses: [CC-BY-SA-3](https://creativecommons.org/licenses/by-sa/3.0/), [CC-BY-4](https://creativecommons.org/licenses/by/4.0), and [CC-BY-NC-ND-4](https://creativecommons.org/licenses/by-nc-nd/4.0). The corpus also include a "save_use_share" license, for these documents the data provider permitted us to share the data for research purposes.
