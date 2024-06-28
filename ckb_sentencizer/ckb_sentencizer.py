import re
from typing import List
from .constants import *


class CkbSentencizer:
    def __init__(self, by: List[str] = None) -> None:
        """
        Initializes the sentencizer with the specified patterns.

        Args:
            by (List[str], optional): List of patterns to split by. Defaults to all keys in ARGS.

        Raises:
            ValueError: If any of the patterns in by is not in ARGS.

        Returns:
            None
        """

        if by is None:
            self.by = list(ARGS.keys())
        else:
            for arg in by:

                if arg not in ARGS.keys():
                    raise ValueError(
                        f"Unknown argument: {arg}. Available: {list(ARGS.keys())}"
                    )
            self.by = by
        self.pattern = re.compile(r"|".join([ARGS[item] for item in self.by]))

    def tokenize(self, text: str) -> List[str]:
        """
        Sentencizes the input paragraph, long text or article into sentences.

        Args:
            text (str): The text to be sentencized.

        Returns:
            List[str]: A list of sentences.
        """

        return [line for line in self.pattern.split(text)]
