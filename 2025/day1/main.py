from pathlib import Path


def part1():
    input_text = Path("input.txt").read_text()
    lines = input_text.splitlines()
    current_position = 50
    pointed_to_zero_count = 0

    # iterate over moves
    for move in lines:
        direction = move[0]
        distance = int(move[1:])

        # Increase position if turning clockwise (Right)
        # decrease if turning anti-clockwise (Left)
        diff = distance if direction == "R" else -distance

        # Calculate next unbounded/absolute position
        absolute_position = current_position + diff
        # Normalized position to account for circling back to zero
        current_position = absolute_position % 100
        assert 0 <= current_position <= 99  # Sanity check

        # Increase counter if the current position is zero
        if current_position == 0:
            pointed_to_zero_count += 1

        print(current_position)

    print(pointed_to_zero_count)



if __name__ == "__main__":
    part1()