from __future__ import annotations

import sys


class Letter:
    def __init__(self, letter: str, freq: float):
        self.letter: str = letter
        self.freq: float = freq
        self.bitstring: dict[str, str] = {}

    def __repr__(self) -> str:
        return f"{self.letter}:{self.freq}"


class TreeNode:
    def __init__(self, freq: float, left: Letter | TreeNode, right: Letter | TreeNode):
        self.freq: float = freq
        self.left: Letter | TreeNode = left
        self.right: Letter | TreeNode = right


def build_letter_list() -> list[Letter]:
    freqs = {
        'T': 0.15,
        'O': 0.15,
        'A': 0.12,
        'E': 0.10,
        'H': 0.09,
        'S': 0.07,
        'P': 0.07,
        'M': 0.07,
        'N': 0.06,
        'C': 0.06,
        'D': 0.05,
        'Z': 0.04,
        'K': 0.03,
        ',': 0.03
    }
    return [Letter(c, f) for c, f in freqs.items()]


def build_tree(letters: list[Letter]) -> Letter | TreeNode:
    response: list[Letter | TreeNode] = letters  # type: ignore
    while len(response) > 1:
        left = response.pop(0)
        right = response.pop(0)
        total_freq = left.freq + right.freq
        node = TreeNode(total_freq, left, right)
        response.append(node)
        response.sort(key=lambda x: x.freq)
    return response[0]


def traverse_tree(root: Letter | TreeNode, bitstring: str) -> list[Letter]:
    if isinstance(root, Letter):
        root.bitstring[root.letter] = bitstring
        return [root]
    treenode: TreeNode = root  # type: ignore
    letters = []
    letters += traverse_tree(treenode.left, bitstring + "0")
    letters += traverse_tree(treenode.right, bitstring + "1")
    return letters


def huffman() -> None:
    letters_list = build_letter_list()
    root = build_tree(letters_list)
    letters = {
        k: v for letter in traverse_tree(root, "") for k, v in letter.bitstring.items()
    }
    print("Huffman Coding:")
    for c, f in letters_list:
        print(f"{c}: {letters[c]}")
    print()


huffman()
