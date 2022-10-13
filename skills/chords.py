from dataclasses import dataclass
from enum import Enum
from common.tree import condition
import theory
from ly.pitch import Pitch

from theory.scales import FPitch, Scale, ScaleMode


class IntervalQuality(Enum):
    MAJOR = "M"
    MINOR = "m"
    AUGMENTED = "A"
    DIMINISHED = "d"


Perfect = condition("Perfect")

interval_state = {
    IntervalQuality.MAJOR: 0,
    IntervalQuality.MINOR: -0.5,
    IntervalQuality.DIMINISHED: {
        True: -0.5,
        False: -1,
    },
    IntervalQuality.AUGMENTED: 0.5
}

interval_state_reversed = {
    0: IntervalQuality.MAJOR,
    -0.5: {
        True: IntervalQuality.DIMINISHED,
        False: IntervalQuality.MINOR,
    },
    -1: IntervalQuality.DIMINISHED,
    0.5: IntervalQuality.AUGMENTED,
}

@dataclass
class Interval:
    root: Pitch
    quality: IntervalQuality
    distance: int

    def __str__(self) -> str:
        return f"{self.quality}{self.distance}"

    def is_perfect(self) -> bool:
        return self.distance in [1, 4, 5, 8]

    def upper(self) -> Pitch:
        root_scale = Scale(self.root, ScaleMode.IONIAN)
        upper = root_scale.pitches()[self.distance % 6]

        if self.quality == IntervalQuality.AUGMENTED:
            return FPitch.from_float(upper.to_float() + 0.5)
        elif self.is_perfect():
            if self.quality == IntervalQuality.DIMINISHED:
                return FPitch.from_float(upper.to_float() - 0.5)
            return upper
        else:
            if self.quality == IntervalQuality.MINOR:
                return FPitch.from_float(upper.to_float() - 0.5)
            elif self.quality == IntervalQuality.DIMINISHED:
                return FPitch.from_float(upper.to_float() - 1)
            return upper

    @classmethod
    def from_notes(cls, n1: Pitch, n2: Pitch):
        n1_val = FPitch(n1).to_float()
        n2_val = FPitch(n2).to_float()

        lower = FPitch.from_float(min(n1_val, n2_val))
        upper = FPitch.from_float(max(n1_val, n2_val))

        root_scale = Scale(lower, ScaleMode.IONIAN)
        deg, err = root_scale.get_degree(upper)

        if err == 0:
            return Interval(lower, IntervalQuality)

class Intervals(theory.MusicAnalyzer):
    def intervals(self):
        for notes in self.staffs:
            for n in notes:
                pass
