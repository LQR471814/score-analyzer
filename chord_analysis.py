from dataclasses import dataclass
from enum import Enum
import ly.music
import ly.music.items as li
from ly.document import Document

from utils import filter_ancestors, get_children, get_descendants, roman_numerals


class Context:
    music: Document
    staffs: list[list[li.Note | li.Rest]]
    key_signature: li.KeySignature
    time_signature: li.TimeSignature

    def __init__(self, document: Document) -> None:
        self.music = document

        staffs: list[list[li.Note | li.Rest]] = []
        for r in get_children(
            get_descendants([music], [li.Relative]),
            [li.MusicList]
        ):
            notes = list(filter_ancestors(
                r.find((li.Note, li.Rest)), [li.KeySignature]))
            staffs.append(notes)
        self.staffs = staffs

        self.key_signature = next(self.music.find(li.KeySignature))
        self.time_signature = next(self.music.find(li.TimeSignature))

    def batch_notes(self, group: li.Fraction) -> list[list[li.Note]]:
        chunks: list[list[li.Note]] = []

        consumed: dict[int, int] = {}
        last_duration: dict[int, li.Fraction] = {}

        staffs = list(reversed(self.staffs))

        while True:
            running = False

            current: list[li.Note] = []
            for i, staff in enumerate(staffs):
                if i not in consumed:
                    consumed[i] = 0

                duration = li.Fraction(0, 1)
                for n in staff[consumed[i]:]:
                    if duration >= group:
                        break

                    note_length = n.length()
                    if float(note_length) > 0:
                        last_duration[i] = note_length
                    else:
                        note_length = last_duration[i]

                    if type(n) == type(li.Note()):
                        current.append(n)
                    duration += note_length
                    consumed[i] += 1

                if len(staff[consumed[i]:]) > 0:
                    running = True

            chunks.append(current)

            if not running:
                break

        return chunks


class Quality(Enum):
    MAJOR = "M"
    MINOR = "m"
    DOMINANT = ""
    AUGMENTED = "+"
    DIMINISHED = "o"
    MAJOR_MINOR = "m#"
    OTHER = "?"


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


class ClassicalAnalyzer:
    context: Context
    cadences: dict[int, list[int]]

    def __init__(self, context: Context) -> None:
        self.context = context
        self.cadences = {
            -1: [1],
            1: [5],
            3: [1],
            4: [1, 6],
        }

    def batch_size(self) -> li.Fraction:
        time_signature = context.time_signature.length()
        beats_per_measure = time_signature.numerator

        if beats_per_measure == 1:
            return li.Fraction(1, time_signature.denominator)

        compound = beats_per_measure % 3 == 0 and beats_per_measure / 3 > 1
        if compound:
            return li.Fraction(3, time_signature.denominator)
        return li.Fraction(2, time_signature.denominator)

    def chords(self) -> list[ClassicalChord]:
        chords: list[ClassicalChord] = []

        chunks = context.batch_notes(self.batch_size())
        previous_chord: ClassicalChord = ClassicalChord(-1, Quality.OTHER)
        for c in chunks:
            pass

        return chords


if __name__ == "__main__":
    with open("canon_in_d.ly", "r") as f:
        doc = Document(f.read())
        music = ly.music.document(doc)

        with open("output.txt", "w") as f:
            f.write(music.dump())

        context = Context(music)
        collected = context.batch_notes(li.Fraction(1, 2))
        for chunk in collected:
            print(" ".join([n.token for n in chunk]))
