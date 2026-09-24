from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
CLAIMS = ROOT / "research" / "claims"
VIDEO_ID = re.compile(r"watch\?v=([A-Za-z0-9_-]{11})")


def section(text: str, start: str, end: str) -> str:
    return text.split(start, 1)[1].split(end, 1)[0]


def ids(text: str) -> set[str]:
    return set(VIDEO_ID.findall(text))


class ResearchCoverageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        screening = (ROOT / "research" / "relevant-video-candidates-2026-09-24.md").read_text(
            encoding="utf-8"
        )
        cls.definite = ids(section(screening, "## Definite candidates", "## Probable candidates"))
        cls.probable = ids(
            section(screening, "## Probable candidates", "## Excluded after metadata review")
        )
        cls.excluded = ids(
            section(screening, "## Excluded after metadata review", "## Selection integrity checks")
        )

    def test_screening_partitions_the_635_video_catalog(self) -> None:
        self.assertEqual(len(self.definite), 185)
        self.assertEqual(len(self.probable), 49)
        self.assertEqual(len(self.excluded), 401)
        self.assertFalse(self.definite & self.probable)
        self.assertFalse(self.definite & self.excluded)
        self.assertFalse(self.probable & self.excluded)
        self.assertEqual(len(self.definite | self.probable | self.excluded), 635)

    def test_eight_batches_cover_every_definite_video_once(self) -> None:
        batch_paths = sorted(CLAIMS.glob("core-design-orientation-batch-*.md"))
        self.assertEqual(len(batch_paths), 8)
        expected_counts = [25, 25, 25, 25, 25, 25, 25, 10]
        seen: set[str] = set()
        for path, expected in zip(batch_paths, expected_counts, strict=True):
            batch_ids = ids(path.read_text(encoding="utf-8"))
            self.assertEqual(len(batch_ids), expected, path.name)
            self.assertFalse(seen & batch_ids, path.name)
            seen.update(batch_ids)
        self.assertEqual(seen, self.definite)

    def test_probable_manifest_covers_all_probable_videos(self) -> None:
        review = (CLAIMS / "probable-video-deep-review.md").read_text(encoding="utf-8")
        manifest = section(review, "## 49-video decision manifest", "## Promotion boundaries")
        self.assertEqual(ids(manifest), self.probable)
        self.assertEqual(len(re.findall(r"\| Include \|", manifest)), 34)
        self.assertEqual(len(re.findall(r"\| Exclude \|", manifest)), 15)


if __name__ == "__main__":
    unittest.main()
