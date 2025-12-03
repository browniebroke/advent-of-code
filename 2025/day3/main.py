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


def compute_bank_joltage(bank: str) -> int:
    batteries = []
    needed_batteries_count = 12
    lower_index = 0
    upper_index = len(bank) - needed_batteries_count
    for idx in range(needed_batteries_count):
        upper_index += 1
        bank_range = bank[lower_index:upper_index]
        best_battery = max(bank_range)
        batteries.append(best_battery)
        lower_index += bank_range.index(best_battery) + 1
    return int("".join(batteries))


if __name__ == '__main__':
    main("1")