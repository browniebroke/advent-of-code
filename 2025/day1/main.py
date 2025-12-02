from pathlib import Path


def main(part=1):
    input_text = Path("input.txt").read_text()
    lines = input_text.splitlines()
    current_position = 50
    previous_position = None
    counter = 0

    # iterate over moves
    for move in lines:
        direction = move[0]
        distance = int(move[1:])

        # Increase position if turning clockwise (Right)
        # decrease if turning anti-clockwise (Left)
        diff = distance if direction == "R" else -distance

        # Calculate next unbounded/absolute position
        previous_position = current_position
        absolute_position = current_position + diff
        # Normalized position to account for circling back to zero
        current_position = absolute_position % 100
        assert 0 <= current_position <= 99  # Sanity check

        # Increase counter if the current position is zero
        if current_position == 0:
            counter += 1

        if part == 2:
            # Also increase counter if the dial crossed the zero point
            all_positions = range(previous_position, absolute_position, 1 if direction == "R" else -1)
            interim_positions = all_positions[1:]
            for pos in interim_positions:
                if pos % 100 == 0:
                    counter += 1

    print(counter)



if __name__ == "__main__":
    main(part=2)