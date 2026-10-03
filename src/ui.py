"""Semua fungsi tampilan terminal dan animasi."""

import os
import sys
import time

LINE = "=" * 50


def _delay(seconds):
    """Jeda hanya jika output tampil di terminal (bukan di-pipe)."""
    if sys.stdout.isatty():
        time.sleep(seconds)


def clear_screen():
    """Bersihkan layar (cls di Windows, clear di Linux/Mac)."""
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def type_text(text, delay=0.01):
    """Cetak teks huruf demi huruf seperti mesin ketik."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        _delay(delay)
    print()


def loading_animation(message, duration=1.0, width=24):
    """Tampilkan progress bar sederhana."""
    print(message)
    for step in range(width + 1):
        percent = int(step / width * 100)
        bar = "█" * step + "░" * (width - step)
        sys.stdout.write(f"\r{bar} {percent}%")
        sys.stdout.flush()
        _delay(duration / width)
    print()


def show_banner():
    print(LINE)
    type_text("SISTEM KLASIFIKASI DATA", 0.02)
    type_text("BERBASIS HIMPUNAN", 0.02)
    type_text("PJBL-2", 0.02)
    print(LINE)
    print()


def show_section(title):
    """Judul sesi/bagian."""
    print()
    print(LINE)
    print(title)
    print(LINE)
    _delay(0.4)


def show_check(message, pause=0.3):
    print(f"✓ {message}")
    _delay(pause)


def show_error(message):
    print(f"✗ {message}")


def pause_session(seconds=1.0):
    """Jeda antar sesi pada animasi pembukaan."""
    _delay(seconds)


def wait_enter():
    """Tunggu user menekan Enter."""
    try:
        input("\nTekan Enter untuk kembali ke menu...")
    except EOFError:
        pass
