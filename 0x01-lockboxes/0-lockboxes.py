#!/usr/bin/python3
"""
Determine if all boxes in the list can be opened
"""
def canUnlockAll(boxes):
    """Determine if boxes can be unlocked"""
    pos = 0
    unlocked = {}

    for box in boxes:
        if len(box) == 0 or pos == 0:
            unlocked[pos] = "unlocked"
        for key in box:
            if key < len(boxes) and key != pos:
                unlocked[key] = "unlocked"
        if len(unlocked) == len(boxes):
            return True
        pos += 1
    return False