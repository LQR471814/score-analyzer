from enum import Enum
from fractions import Fraction
from typing import Iterator, cast

from common.node import filter_ancestors, get_children, get_descendants
from ly.music.items import (Document, KeySignature, MusicList, Note, Relative,
                            Rest, TimeSignature)

from theory.scales import Scale, scale_name_mapping


class Quality(Enum):
    MAJOR = "M"
    MINOR = "m"
    DOMINANT = ""
    AUGMENTED = "+"
    DIMINISHED = "o"
    MAJOR_MINOR = "m#"
    OTHER = "?"


MeasureElement = tuple[Note | Rest, Fraction]


class MusicAnalyzer:
    music: Document
    staffs: list[list[Note | Rest]]
    key: Scale

    key_signature: KeySignature
    time_signature: TimeSignature

    def __init__(self, document: Document) -> None:
        self.music = document

        staffs: list[list[Note | Rest]] = []
        for r in get_children(
            get_descendants([self.music], [Relative]),
            [MusicList]
        ):
            notes = list(filter_ancestors(
                r.find((Note, Rest)),
                [KeySignature]
            ))
            staffs.append(cast(list[Note | Rest], notes))
        self.staffs = staffs

        key_signature: KeySignature = next(self.music.find(KeySignature))
        time_signature: TimeSignature = next(self.music.find(TimeSignature))

        self.key_signature = key_signature
        self.time_signature = time_signature

        self.key = Scale(
            key_signature.pitch(),
            scale_name_mapping[key_signature.mode()],
        )

    def iterate_measures(self, group: Fraction | None = None) -> Iterator[list[list[MeasureElement]]]:
        if group is None:
            group = self.time_signature.measure_length()

        consumed: dict[int, int] = {}
        last_duration: dict[int, Fraction] = {}

        staffs = list(reversed(self.staffs))

        while True:
            running = False

            current: list[list[MeasureElement]] = [
                [] for _ in range(len(staffs))]
            for i, staff in enumerate(staffs):
                if i not in consumed:
                    consumed[i] = 0

                elapsed_duration = Fraction(0, 1)
                for n in staff[consumed[i]:]:
                    if elapsed_duration >= group:
                        break

                    note_length = n.length()
                    if isinstance(note_length, int):
                        note_length = Fraction.from_float(note_length)
                    if note_length > 0:
                        last_duration[i] = note_length
                    else:
                        note_length = last_duration[i]

                    # * explicitly set length for all notes
                    n.duration = (note_length, n.duration[1])

                    current[i].append((n, elapsed_duration))
                    elapsed_duration += note_length
                    consumed[i] += 1

                if len(staff[consumed[i]:]) > 0:
                    running = True

            yield current

            if not running:
                break
