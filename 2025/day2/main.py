from pathlib import Path


def main(part: int):
    input_text = Path("input.txt").read_text()
    ranges = input_text.split(",")
    invalid_refs = []
    for r_str in ranges:
        low, high = map(int, r_str.split("-"))
        for reference in range(low, high + 1):
            reference_str = str(reference)
            ref_len = len(reference_str)
            if ref_len % 2 == 0:
                half_len = ref_len // 2
                first_half = reference_str[:half_len]
                second_half = reference_str[half_len:]
                if first_half == second_half:
                    invalid_refs.append(reference)
    print(sum(invalid_refs))


if __name__ == '__main__':
    main(1)
