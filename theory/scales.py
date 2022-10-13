from dataclasses import dataclass
from enum import Enum
from typing import cast

from common.annotations import Note
from ly.pitch import Pitch

ScaleDegree = Note


class ScaleMode(Enum):
    IONIAN = 0
    DORIAN = 1
    PHRYGIAN = 2
    LYDIAN = 3
    MIXOLYDIAN = 4
    AEOLIAN = 5
    LOCRIAN = 6


scale_degree: list[float] = [0, 1, 2, 2.5, 3.5, 4.5, 5.5]
scale_degree_offsets: list[float] = [0, 1, 1, 0.5, 1, 1, 1]
scale_name_mapping: dict[str, ScaleMode] = {
    "major": ScaleMode.IONIAN,
    "dorian": ScaleMode.DORIAN,
    "phrygian": ScaleMode.PHRYGIAN,
    "lydian": ScaleMode.LYDIAN,
    "mixolydian": ScaleMode.MIXOLYDIAN,
    "minor": ScaleMode.AEOLIAN,
    "locrian": ScaleMode.LOCRIAN,
}


class FPitch(Pitch):
    def __init__(self, pitch: Pitch) -> None:
        super().__init__(pitch.note, pitch.alter, pitch.octave,
                         pitch.accidental, pitch.octavecheck)

    @classmethod
    def from_float(cls, value: float) -> "FPitch":
        value = value % 6
        note = 0
        alter = 0.0
        for degree in scale_degree:
            if value - degree < 1:
                alter = value - degree
                break
            note += 1
        return cls(Pitch(note=cast(Note, note), alter=alter))

    def to_float(self) -> float:
        return scale_degree[self.note] + self.alter


@dataclass
class Scale:
    root: Pitch
    mode: ScaleMode

    # * return (degree: ScaleDegree, error: float)
    def get_degree(self, target: Pitch) -> tuple[ScaleDegree, float]:
        target_float = FPitch(target).to_float()
        pitches = self.pitches()

        distance = float('inf')
        closest: ScaleDegree = 0
        for i, p in enumerate(pitches):
            scale_float = p.to_float()
            if scale_float == target_float:
                return (cast(ScaleDegree, i), 0)

            if scale_float < distance:
                distance = scale_float
                closest = cast(ScaleDegree, i)

        return (closest, distance)

    def pitches(self) -> list[FPitch]:
        notes: list[FPitch] = []

        current_pitch: FPitch = FPitch(self.root)
        last_pitch: float = 0
        for degree in scale_degree:
            current_pitch = FPitch.from_float(
                current_pitch.to_float() + (degree - last_pitch))
            last_pitch = degree
            notes.append(current_pitch)

        return notes
