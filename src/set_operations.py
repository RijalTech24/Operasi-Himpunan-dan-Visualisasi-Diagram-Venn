"""Operasi himpunan dasar menggunakan Python set."""


def union_set(A, B):
    """A ∪ B : semua anggota yang ada di A atau di B."""
    return A | B


def intersection_set(A, B):
    """A ∩ B : anggota yang ada di A dan sekaligus di B."""
    return A & B


def difference_set(A, B):
    """A - B : anggota A yang tidak ada di B."""
    return A - B


def complement_set(U, A):
    """U - A (komplemen A) : anggota semesta yang bukan anggota A."""
    return U - A
