#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    :param boxes: list of lists, where each sublist contains keys
    :return: True if all boxes can be opened, else False
    """
    unlocked = set([0])  # The first box is always unlocked
    keys = set(boxes[0])  # Start with keys from the first box

    while keys:
        new_keys = set()
        for key in keys:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                new_keys.update(boxes[key])
        if not new_keys:
            break
        keys = new_keys

    return len(unlocked) == len(boxes)


if __name__ == "__main__":
    # Test case 1: Sequential unlocking
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected output: True

    # Test case 2: Keys that don't have corresponding boxes
    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected output: True

    # Test case 3: Not all boxes can be unlocked
    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected output: False

    # Additional test cases can be added here

