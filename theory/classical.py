from dataclasses import dataclass
from fractions import Fraction

from ly.music.items import Document

from . import MusicAnalyzer, Quality

roman_numerals: list[str] = ["I", "II", "III", "IV", "V", "VI", "VII"]
cadences: dict[int, list[int]] = {
    -1: [1],
    1: [5],
    3: [1],
    4: [1, 6],
}


@dataclass
class ClassicalChord:
    degree: int
    quality: Quality
    seventh: bool = False

    def __str__(self) -> str:
        return (
            roman_numerals[self.degree] +
            str(self.quality) + '7' if self.seventh else ''
        )


class ClassicalAnalyzer(MusicAnalyzer):
    def __init__(self, document: Document) -> None:
        super().__init__(document)

    def batch_size(self) -> Fraction:
        time_signature = self.time_signature.length()
        beats_per_measure = time_signature.numerator

        if beats_per_measure == 1:
            return Fraction(1, time_signature.denominator)

        compound = beats_per_measure % 3 == 0 and beats_per_measure / 3 > 1
        if compound:
            return Fraction(3, time_signature.denominator)
        return Fraction(2, time_signature.denominator)

    # def chords(self) -> list[ClassicalChord]:
    #     chords: list[ClassicalChord] = []

    #     previous_chord: ClassicalChord = ClassicalChord(-1, Quality.OTHER)
    #     for measure in self.iterate_measures(self.batch_size()):
    #         if len(measure) == 0:
    #             continue

    #     return chords
