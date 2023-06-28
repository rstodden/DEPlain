#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import os

if not os.path.exists("documents"):
    os.makedirs("documents")



data = pd.read_csv("../B__Document-level_Corpus/DEplain-web-doc/manual/open/sentence-split/test.csv")
for n, row in data.iterrows():
    original_sentences = row["original"].strip().split("|||")
    simple_sentences = row["simplification"].strip().split("|||")
    i = row["pair_id"]
    with open("documents/file_"+str(i)+".src", "w") as f:
        f.write("\n".join(original_sentences))
    with open("documents/file_"+str(i)+".tgt", "w") as f:
        f.write("\n".join(simple_sentences))
    row.drop(["simplification", "original"]).to_json("documents/file_"+str(i)+".meta")



