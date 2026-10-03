"""Prinsip Inklusi-Eksklusi (PIE) untuk dua dan tiga himpunan.

Fungsi mengembalikan hasil DAN baris-baris langkah perhitungan
supaya prosesnya bisa ditampilkan.
"""


def pie_two(A, B):
    """|A ∪ B| = |A| + |B| - |A ∩ B|"""
    a, b, ab = len(A), len(B), len(A & B)
    result = a + b - ab
    lines = [
        f"|A| = {a}",
        f"|B| = {b}",
        f"|A ∩ B| = {ab}",
        "",
        "|A ∪ B|",
        "= |A| + |B| - |A ∩ B|",
        f"= {a} + {b} - {ab}",
        f"= {result}",
    ]
    return {"result": result, "lines": lines}


def pie_three(A, B, C):
    """|A ∪ B ∪ C| = |A|+|B|+|C| - |A∩B| - |A∩C| - |B∩C| + |A∩B∩C|"""
    a, b, c = len(A), len(B), len(C)
    ab, ac, bc = len(A & B), len(A & C), len(B & C)
    abc = len(A & B & C)
    result = a + b + c - ab - ac - bc + abc
    lines = [
        f"|A| = {a}",
        f"|B| = {b}",
        f"|C| = {c}",
        f"|A ∩ B| = {ab}",
        f"|A ∩ C| = {ac}",
        f"|B ∩ C| = {bc}",
        f"|A ∩ B ∩ C| = {abc}",
        "",
        "|A ∪ B ∪ C|",
        "= |A| + |B| + |C| - |A ∩ B| - |A ∩ C| - |B ∩ C| + |A ∩ B ∩ C|",
        f"= {a} + {b} + {c} - {ab} - {ac} - {bc} + {abc}",
        f"= {a + b + c} - {ab + ac + bc} + {abc}",
        f"= {result}",
    ]
    return {"result": result, "lines": lines}
