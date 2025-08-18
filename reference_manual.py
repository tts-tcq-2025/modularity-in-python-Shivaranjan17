# reference_manual.py
# New Feature: Print reference manual mapping pair numbers to color pairs

from constants import MAJOR_COLORS, MINOR_COLORS
from color_coding import get_color_from_pair_number


def format_reference_manual():
    reference_lines = []
    total_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
    for pair_number in range(1, total_pairs + 1):
        major, minor = get_color_from_pair_number(pair_number)
        reference_lines.append(f'{pair_number:2} --> {major:<6} {minor}')
    return "\n".join(reference_lines)


def print_reference_manual():
    print("25-Pair Color Code Reference Manual")
    print("-----------------------------------")
    print(format_reference_manual())
