#!/usr/bin/python3
"""
Solves the lock boxes puzzle
"""


def canUnlockAll(boxes):
    """
    Check if all boxes can be opened
    Args:
        boxes (list): List which contain all the boxes with the keys
    Returns:
        bool: True if all boxes can be opened, otherwise, False
    """
    if not boxes:
        return True

    num_boxes = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        current_box = stack.pop()
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited and key < num_boxes:
                stack.append(key)

    return len(visited) == num_boxes


def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
