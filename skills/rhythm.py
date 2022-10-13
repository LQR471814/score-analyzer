from fractions import Fraction
from theory import MusicAnalyzer

class RhythmAnalyzer(MusicAnalyzer):
    def analyze_rhythm(self):
        durations: set[Fraction | int] = set()
        difficulty: list[float] = []

        for staffs in self.iterate_measures():
            for s in staffs:
                for n in s:
                    durations.add(n[0].length())
