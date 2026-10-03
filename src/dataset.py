"""Membaca file CSV mahasiswa, memvalidasi, lalu membentuk himpunan U, A, B, C.

Aturan pembentukan himpunan (sesuai laporan perencanaan):
  U = seluruh mahasiswa (anggota himpunan memakai NIM)
  A = mahasiswa Semester 3
  B = mahasiswa anggota organisasi (kolom Organisasi bukan "-")
  C = mahasiswa anggota UKM (kolom UKM bukan "-")
"""

import csv
from pathlib import Path

REQUIRED_COLUMNS = ["NIM", "Nama", "Semester", "Organisasi", "UKM"]
SEMESTER_A = 3
TIDAK_IKUT = "-"


class DatasetError(Exception):
    """Error khusus untuk masalah file/dataset (pesannya mudah dipahami)."""


def load_dataset(path, title=None):
    """Baca CSV lalu kembalikan dictionary berisi:
    nama, records, names (NIM -> Nama), U, A, B, C, label_A, label_B, label_C.
    Jika ada masalah, raise DatasetError dengan pesan jelas.
    """
    path = Path(path)

    if not path.exists():
        raise DatasetError(f"File dataset tidak ditemukan: {path}")

    try:
        with open(path, encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames or []
            rows = list(reader)
    except (UnicodeDecodeError, csv.Error):
        raise DatasetError(f"{path.name}: file CSV tidak bisa dibaca (format rusak).")

    missing = [col for col in REQUIRED_COLUMNS if col not in header]
    if missing:
        raise DatasetError(f"{path.name}: kolom {missing} tidak ditemukan. "
                           f"Kolom wajib: {REQUIRED_COLUMNS}")
    if not rows:
        raise DatasetError(f"{path.name}: data kosong.")

    return _build_sets(rows, title or path.stem, path.name)


def _build_sets(rows, title, filename):
    """Validasi tiap baris lalu bentuk himpunan berdasarkan aturan keanggotaan."""
    records = []
    names = {}
    U, A, B, C = set(), set(), set(), set()

    for line_number, row in enumerate(rows, start=2):  # baris 1 = header
        values = {col: (row.get(col) or "").strip() for col in REQUIRED_COLUMNS}

        for col, value in values.items():
            if value == "":
                raise DatasetError(f"{filename} baris {line_number}: kolom '{col}' kosong "
                                   f"(isi '{TIDAK_IKUT}' jika tidak mengikuti).")
        if not values["Semester"].isdigit():
            raise DatasetError(f"{filename} baris {line_number}: Semester harus berupa angka.")

        nim = values["NIM"]
        if nim in names:
            raise DatasetError(f"{filename} baris {line_number}: NIM {nim} duplikat "
                               f"(NIM harus unik).")

        semester = int(values["Semester"])
        records.append({"nim": nim, "nama": values["Nama"], "semester": semester,
                        "organisasi": values["Organisasi"], "ukm": values["UKM"]})
        names[nim] = values["Nama"]

        U.add(nim)
        if semester == SEMESTER_A:
            A.add(nim)
        if values["Organisasi"] != TIDAK_IKUT:
            B.add(nim)
        if values["UKM"] != TIDAK_IKUT:
            C.add(nim)

    return {
        "nama": title, "records": records, "names": names,
        "U": U, "A": A, "B": B, "C": C,
        "label_A": f"Semester {SEMESTER_A}",
        "label_B": "Organisasi (BEM/HMJ)",
        "label_C": "UKM",
    }
