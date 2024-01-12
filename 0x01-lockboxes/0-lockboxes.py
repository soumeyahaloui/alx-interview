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


