"""
Constants for sentence tokenization in Central Kurdish (Sorani).

Defines regex patterns for identifying sentence boundaries based on punctuation:
- FULLSTOP: Matches sentence-ending periods, question marks, commas, exclamation points, and semicolons.
- COMMA: Matches commas used as sentence separators.
- QUOTATION: Matches sentence-ending quotations.
- NEWLINE: Matches newline characters.

ARGS dictionary contains these patterns for easy access.
"""

FULLSTOP = "".join(["(?<!\w\.\w)", "(?<!\s.\.)", "(?<=\.|\?|,|؟|\!|;|؛)", "\s"])
COMMA = "".join(
    ["(?<!\w،\w)", "(?<!\w، \w،)", "(?<!\(\w،)", "(?<!\w\. \w،)", "(?<=،)", "\s"]
)
QUOTATION = "|".join(
    [
        '(?<=\.")\s',
        '(?<=\.)"',
    ]
)
NEWLINE = "|".join(["\n"])

ARGS = {"fullstop": FULLSTOP, "comma": COMMA, "quotation": QUOTATION, "newline": NEWLINE}