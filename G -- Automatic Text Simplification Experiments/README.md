# DEplain: Automatic Text Simplification Experiments

To exemplify the usage of DEPLAIN for training and evaluating TS models, we are presenting results on finetuning long-mBART on our document-level corpus as well as finetuning mBART on our sentence-level corpus, using code provided by [Rios et al. (2021)](https://github.com/a-rios/longmbart).

You can find our edited code here: [https://github.com/omarTronto/longmbart_model](https://github.com/omarTronto/longmbart_model).

## Document Simplification

### Results on Document-level

| train data | n | SARI ↑ | BLEU ↑ | BS-P ↑ | FRE ↑ |
|---------------------|------------|--------------------------|--------------------------|--------------------------|-------------------------|
| DEplain-APA         | 387        | **44.56**           | **38.136**          | **0.598**           | **65.4**           |
| DEplain-web         | 481        | 35.02                    | 12.913                   | 0.475                    | 59.55                   |
| DEplain-APA+web     | 868        | 42.862                   | 36.449                   | 0.589                    | 65.4                    |
| src2Src-baseline    |            | 17.637                   | 34.247                   | 0.583                    | 58.85                   |

: Results on DEplain-APA test (n=48).


| train data | n | SARI ↑ | BLEU ↑ | BS-P ↑ | FRE ↑ |
|---------------------|------------|--------------------------|--------------------------|--------------------------|-------------------------|
| DEplain-APA         | 387        | 43.087                   | 21.9                     | 0.377                    | **64.7**           |
| DEplain-web         | 481        | 49.584                   | 23.282                   | **0.462**           | 63.5                    |
| DEplain-APA+web     | 868        | **49.745**          | **23.37**           | 0.445                    | 57.95                   |
| src2Src-baseline    |            | 12.848                   | 23.132                   | 0.432                    | 59.4                    |

: Results on DEplain-web test (n=147).

## Sentence Simplification

### Results on Sentence-level
| train data | n | SARI ↑ | BLEU ↑ | BS-P ↑ | FRE ↑ |
|---------------------|------------|--------------------------|--------------------------|--------------------------|-------------------------|
| DEplain-APA         | 10660      | 34.818                   | 28.25                    | 0.639                    | **63.072**         |
| DEplain-APA+web     | 11941      | **34.904**         | **28.506**          | **0.64**            | 62.669                  |
| src2src-baseline    |            | 15.249                   | 26.893                   | 0.627                    | 59.23                   |

: Results on DEplain-APA test (n=1231).


| train data | n | SARI ↑ | BLEU ↑ | BS-P ↑ | FRE ↑ |
|----------------------|------------|--------------------------|--------------------------|--------------------------|-------------------------|
| DEplain-APA          | 10660      | 30.867                   | 15.727                   | 0.413                    | 64.516                  |
| DEplain-APA+web      | 11941      | **34.828**          | **17.88**           | **0.436**           | **65.249**         |
| src2src-baseline     |            | 11.931                   | 20.85                    | 0.423                    | 60.825                  |

: Results on DEplain-web test (n=1846).