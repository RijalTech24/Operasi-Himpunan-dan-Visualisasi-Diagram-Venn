"""Testing operasi himpunan, PIE, dan kedua dataset."""

import tempfile
import unittest
from pathlib import Path

from src.dataset import DatasetError, load_dataset
from src.inclusion_exclusion import pie_three, pie_two
from src.set_operations import (complement_set, difference_set,
                                intersection_set, union_set)

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
FILE_1 = DATA_DIR / "dataset_mahasiswa.csv"
FILE_2 = DATA_DIR / "dataset_mahasiswa_2.csv"


class TestSetOperations(unittest.TestCase):
    def setUp(self):
        self.U = {1, 2, 3, 4, 5, 6}
        self.A = {1, 2, 3}
        self.B = {3, 4}

    def test_union(self):
        """Test Union"""
        self.assertEqual(union_set(self.A, self.B), {1, 2, 3, 4})

    def test_intersection(self):
        """Test Intersection"""
        self.assertEqual(intersection_set(self.A, self.B), {3})

    def test_difference(self):
        """Test Difference"""
        self.assertEqual(difference_set(self.A, self.B), {1, 2})
        self.assertEqual(difference_set(self.B, self.A), {4})

    def test_complement(self):
        """Test Complement"""
        self.assertEqual(complement_set(self.U, self.A), {4, 5, 6})


class TestDatasets(unittest.TestCase):
    def _check_pie(self, file):
        data = load_dataset(file)
        A, B, C = data["A"], data["B"], data["C"]
        self.assertEqual(pie_two(A, B)["result"], len(A | B))
        self.assertEqual(pie_three(A, B, C)["result"], len(A | B | C))
        self.assertGreater(len(A & B), 0)
        self.assertGreater(len(A & B & C), 0)

    def test_pie_dataset1(self):
        """Test PIE Dataset 1"""
        self._check_pie(FILE_1)

    def test_pie_dataset2(self):
        """Test PIE Dataset 2"""
        self._check_pie(FILE_2)

    def test_sets_dataset1(self):
        """Test Pembentukan Himpunan Dataset 1"""
        d = load_dataset(FILE_1)
        self.assertEqual(len(d["U"]), 15)
        self.assertEqual((len(d["A"]), len(d["B"]), len(d["C"])), (7, 7, 7))
        self.assertEqual(len(d["A"] & d["B"]), 4)
        self.assertEqual(len(d["A"] | d["B"] | d["C"]), 13)

    def test_sets_dataset2(self):
        """Test Pembentukan Himpunan Dataset 2"""
        d = load_dataset(FILE_2)
        self.assertEqual(len(d["U"]), 15)
        self.assertEqual((len(d["A"]), len(d["B"]), len(d["C"])), (6, 7, 7))
        self.assertEqual(len(d["A"] & d["B"]), 4)
        self.assertEqual(len(d["A"] | d["B"] | d["C"]), 12)

    def test_datasets_different(self):
        """Test Dataset 1 dan 2 berbeda"""
        d1, d2 = load_dataset(FILE_1), load_dataset(FILE_2)
        self.assertNotEqual(d1["U"], d2["U"])
        self.assertNotEqual(len(d1["A"] | d1["B"]), len(d2["A"] | d2["B"]))

    def test_dataset_not_found(self):
        """Test Dataset tidak ditemukan"""
        with self.assertRaises(DatasetError):
            load_dataset(DATA_DIR / "tidak_ada.csv")

    def test_dataset_invalid(self):
        """Test CSV tidak valid (kolom hilang & NIM duplikat)"""
        isi_salah = {
            "NIM,Nama\n1,Andi\n": "kolom hilang",
            "NIM,Nama,Semester,Organisasi,UKM\n": "kosong",
            "NIM,Nama,Semester,Organisasi,UKM\n1,A,3,-,-\n1,B,3,-,-\n": "NIM duplikat",
        }
        with tempfile.TemporaryDirectory() as folder:
            for isi in isi_salah:
                path = Path(folder) / "uji.csv"
                path.write_text(isi, encoding="utf-8")
                with self.assertRaises(DatasetError):
                    load_dataset(path)


if __name__ == "__main__":
    unittest.main()
