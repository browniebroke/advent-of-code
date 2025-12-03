from pathlib import Path


def main(part: str):
    input_text = Path("input.txt").read_text()
    battery_banks = input_text.splitlines()
    total_joltage = 0
    for bank in battery_banks:
        joltages: dict[int, str] = {}
        batteries = list(map(int, bank))
        for _ in range(2):
            value = max(batteries)
            position = None
            for previous_pos in list(joltages.keys())[::-1]:
                print(previous_pos)
                try:
                    position = batteries[previous_pos - 1:].index(value)
                except ValueError:
                    pass
            if position is None:
                position = batteries.index(value)
            batteries.remove(value)
            joltages[position] = str(value)

        bank_joltage = int("".join(joltages[k] for k in sorted(joltages.keys())))

        print(f"{bank=}, {bank_joltage=}")

        total_joltage += bank_joltage

    print(total_joltage)
    # 15983 too low


if __name__ == '__main__':
    main("1")
