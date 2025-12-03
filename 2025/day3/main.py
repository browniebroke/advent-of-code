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
    # 16854 Good
    # 15983 too low


def compute_bank_joltage(bank: str) -> int:
    d0 = max(bank[:-1])
    d0_idx = bank.index(d0)
    d1 = max(bank[d0_idx + 1:])
    return int(f"{d0}{d1}")


if __name__ == '__main__':
    main("1")