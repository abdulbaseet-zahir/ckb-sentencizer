# CkbSentencizer

CkbSentencizer is a Python package designed to convert paragraphs, long texts, or articles into sentences in Central Kurdish (Sorani).

## Installation

You can install CkbSentencizer using pip:

```bash
pip install git+https://github.com/abdulbaseet-zahir/ckb-sentencizer.git
```

## Usage

Here's a basic example of how to use the CkbSentencizer:

```python
from ckb_sentencizer import CkbSentencizer, ARGS

# Initialize the sentencizer
tokenizer = CkbSentencizer(by=list(ARGS.keys()))

# Sample text in Central Kurdish (Sorani) from rudaw.net/sorani/sports/260620241
text = """
بەرەبەیانی ئەمڕۆ، لە دووەم یارییاندا لە رکابەرییەکانی کۆپا ئەمریکا، هەڵبژاردەی ئەرجەنتین بەرامبەر چیلی یاریکرد، یارییەکە بە گۆڵێکی بێبەرامبەر لە بەرژەوەندی ئەرجەنتین کۆتاییهات و لاوتارۆ مارتینێز گۆڵەکەی تۆمارکرد.
 
دوای یارییەکە لیۆنێل مێسی، قسەی بۆ میدیاکان کرد و گوتی "ئێستا سەرکەوتووین بۆ قۆناخی هەشت، بەڵام یارییەکی قورس بوو بەرامبەر چیلی. هەرچۆنێک بێت با بزانین یاری داهاتوو چۆن دەبێت".
"""

# Sentencize the articles
sentences = tokenizer.tokenize(text)

# Print the sentencized text
print(sentences)
```