# a file containing many useful annotations from the python-ly-stubs package

from fractions import Fraction
from typing import Literal

FractionalDuration = tuple[Fraction, Fraction]

Note = Literal[0, 1, 2, 3, 4, 5, 6]
Alter = float
Octave = Literal[-2, 2]
Accidental = Literal["", "?", "!"]

Language = Literal["nederlands", "english", "deutsch", "svenska",
                   "italiano", "espanol", "portugues", "vlaams",
                   "norsk", "suomi", "catalan"]
