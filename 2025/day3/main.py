from collections import Counter
from pathlib import Path


def main(part: str):
    input_text = Path("input.txt").read_text()
    battery_banks = input_text.splitlines()
    total_joltage = 0
    for bank in battery_banks:
        bank_j = compute_bank_joltage(bank)

        print(f"{bank=}, {bank_j=}")
        total_joltage += bank_j

    print(total_joltage)
    # 17479 too high
    # 16533 not good
    # 15983 too low


def compute_bank_joltage(bank: str) -> int:
    counter = Counter(bank)
    print(f"before: {counter}")
    max_j = max(counter.keys())
    if counter[max_j] >= 2:
        return int(f"{max_j}" * 2)
    else:
        counter.pop(max_j)
        print(f"after: {counter}")
        second_max_j = max(counter.keys())
        max_joltage_idx = bank.index(max_j)
        if second_max_j in bank[max_joltage_idx + 1 :]:
            return int(f"{max_j}{second_max_j}")
        else:
            return int(f"{second_max_j}{max_j}")


if __name__ == '__main__':
    main("1")
