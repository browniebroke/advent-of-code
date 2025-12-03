from pathlib import Path
import textwrap


def main(part: int):
    input_text = Path("input.txt").read_text()
    ranges = input_text.split(",")
    invalid_refs = []
    for r_str in ranges:
        low, high = map(int, r_str.split("-"))
        for reference in range(low, high + 1):
            reference_str = str(reference)
            validator = VALIDATORS[part]
            if validator(reference_str):
                invalid_refs.append(reference)
    print(sum(invalid_refs))


def is_ref_invalid_part1(reference_str: str) -> bool:
    ref_len = len(reference_str)
    if ref_len % 2 == 0:
        half_len = ref_len // 2
        first_half = reference_str[:half_len]
        second_half = reference_str[half_len:]
        return first_half == second_half
    return False


def is_ref_invalid_part2(reference_str: str) -> bool:
    ref_len = len(reference_str)
    if ref_len == 1:
        return False
    for slice_len in range(1, ref_len // 2 + 1):
        slices = textwrap.wrap(reference_str, slice_len)
        unique_slices = set(slices)
        if len(unique_slices) == 1:
            return True
    return False




VALIDATORS = {
    1: is_ref_invalid_part1,
    2: is_ref_invalid_part2, # 28858486244
}


if __name__ == '__main__':
    main(2)
