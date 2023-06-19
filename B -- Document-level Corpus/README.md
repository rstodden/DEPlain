# DEplain: German Document Simplification Data
We present two new TS corpora on the document level, DEplain-APA and DEplain-WEB, containing parallel documents in standard German and plain German. 

## Data Format
For each document-level dataset, we provide two different formats:
- plain text: plain documents per line without sentence split, and
- sentence split: documents per line with sentence split, each sentence is separated by "|||"


## Data Statistics
|   | Name        | License      | # Doc. Pairs (train/dev/test) | # Original Sents | # Simple Sents. |
|---|-------------|--------------|-------------------------------|------------------|-----------------|
| 1 | DEplain-apa | upon request | 483  (387/48/48)              | 25,607           | 26,471          |
| 2 | DEplain-web | open         | 147  (-/-/147)                | 6,138            | 6,402           |
| 3 | DEplain-web | open         | 249 (199/50/-)                | 7,087            | 7,760           |
| 4 | DEplain-web | closed       | 360 (288/72/-)                | 12,847           | 18,068          |
|   | In total    | mixed        | 1,239 (874/170/195)           | 51,681           | 58,701          |

## License
- **DEplain-APA**: The dataset is provided for research purposes only. Please request access using the following form: [https://zenodo.org/record/7674560](https://zenodo.org/record/7674560)
- **DEplain-web**: The corpus includes the following licenses: [CC-BY-SA-3](https://creativecommons.org/licenses/by-sa/3.0/), [CC-BY-4](https://creativecommons.org/licenses/by/4.0), and [CC-BY-NC-ND-4](https://creativecommons.org/licenses/by-nc-nd/4.0).
