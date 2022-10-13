from ly.document import Document
from ly.music import document
from metadata import Metadata

from theory import MusicAnalyzer

if __name__ == "__main__":
    with open("canon_in_d.ly", "r") as f:
        doc = Document(f.read())
        music = document(doc)

        with open("output.txt", "w") as f:
            f.write(music.dump())

        analyzer = MusicAnalyzer(music)

        metadata = Metadata.from_music(music)
        print(metadata)

        print(analyzer.key.pitches())
        # for chunk in analyzer.iterate_measures():
        #     print(" ".join([f"{n.token}-{p}" for n, p in chunk]))
