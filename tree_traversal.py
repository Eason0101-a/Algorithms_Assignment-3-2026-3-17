from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional


@dataclass
class Node:
    """二元樹節點。"""

    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BinaryTree:
    """二元搜尋樹，包含作業所需的走訪方法。"""

    def __init__(self, values: Optional[Iterable[int]] = None) -> None:
        self.root: Optional[Node] = None
        if values is not None:
            self.build_from_iterable(values)

    @classmethod
    def from_assignment_tree(cls) -> "BinaryTree":
        """建立題目指定樹形：

                50
              /    \\
            30      70
           /  \\    /  \\
          20   40  60   80
        """
        tree = cls()
        tree.root = Node(50)
        tree.root.left = Node(30)
        tree.root.right = Node(70)
        tree.root.left.left = Node(20)
        tree.root.left.right = Node(40)
        tree.root.right.left = Node(60)
        tree.root.right.right = Node(80)
        return tree

    def build_from_iterable(self, values: Iterable[int]) -> None:
        """依序插入資料以建立樹。"""
        for value in values:
            self.insert(value)

    def insert(self, value: int) -> None:
        """將數值插入樹中（BST 規則）。"""
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: Optional[Node], value: int) -> Node:
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        return node

    def search(self, value: int) -> bool:
        """若數值存在於樹中則回傳 True。"""
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def size(self) -> int:
        """回傳樹中的節點總數。"""
        return self._size_recursive(self.root)

    def _size_recursive(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)

    def height(self) -> int:
        """回傳樹高，空樹高度定義為 -1。"""
        return self._height_recursive(self.root)

    def _height_recursive(self, node: Optional[Node]) -> int:
        if node is None:
            return -1
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))

    def preorder_traversal(self) -> List[int]:
        """前序走訪：根 -> 左 -> 右。"""
        result: List[int] = []
        self._preorder_recursive(self.root, result)
        return result

    def PreorderTraversal(self) -> List[int]:
        """符合題目命名的前序走訪方法。"""
        return self.preorder_traversal()

    def _preorder_recursive(self, node: Optional[Node], result: List[int]) -> None:
        if node is None:
            return
        result.append(node.value)
        self._preorder_recursive(node.left, result)
        self._preorder_recursive(node.right, result)

    def preorder_traversal_iterative(self) -> List[int]:
        """使用堆疊的前序走訪（迭代版）。"""
        if self.root is None:
            return []

        result: List[int] = []
        stack: List[Node] = [self.root]

        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return result

    def inorder_traversal(self) -> List[int]:
        """中序走訪：左 -> 根 -> 右。"""
        result: List[int] = []
        self._inorder_recursive(self.root, result)
        return result

    def InorderTraversal(self) -> List[int]:
        """符合題目命名的中序走訪方法。"""
        return self.inorder_traversal()

    def _inorder_recursive(self, node: Optional[Node], result: List[int]) -> None:
        if node is None:
            return
        self._inorder_recursive(node.left, result)
        result.append(node.value)
        self._inorder_recursive(node.right, result)

    def inorder_traversal_iterative(self) -> List[int]:
        """使用堆疊的中序走訪（迭代版）。"""
        result: List[int] = []
        stack: List[Node] = []
        current = self.root

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.value)
            current = current.right

        return result

    def postorder_traversal(self) -> List[int]:
        """後序走訪：左 -> 右 -> 根。"""
        result: List[int] = []
        self._postorder_recursive(self.root, result)
        return result

    def PostorderTraversal(self) -> List[int]:
        """符合題目命名的後序走訪方法。"""
        return self.postorder_traversal()

    def _postorder_recursive(self, node: Optional[Node], result: List[int]) -> None:
        if node is None:
            return
        self._postorder_recursive(node.left, result)
        self._postorder_recursive(node.right, result)
        result.append(node.value)

    def postorder_traversal_iterative(self) -> List[int]:
        """使用雙堆疊的後序走訪（迭代版）。"""
        if self.root is None:
            return []

        result: List[int] = []
        stack1: List[Node] = [self.root]
        stack2: List[Node] = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left is not None:
                stack1.append(node.left)
            if node.right is not None:
                stack1.append(node.right)

        while stack2:
            result.append(stack2.pop().value)

        return result


if __name__ == "__main__":
    print("指定樹形:")
    print("        50")
    print("      /    \\")
    print("    30      70")
    print("   /  \\    /  \\")
    print(" 20   40  60   80")
    print()

    tree = BinaryTree.from_assignment_tree()

    sample_data = [50, 30, 70, 20, 40, 60, 80]
    print("節點資料:", sample_data)
    print("節點總數:", tree.size())
    print("樹高:", tree.height())
    print("搜尋 60:", tree.search(60))
    print("搜尋 99:", tree.search(99))
    print()

    print("前序走訪（遞迴）:", tree.preorder_traversal())
    print("中序走訪（遞迴）:", tree.inorder_traversal())
    print("後序走訪（遞迴）:", tree.postorder_traversal())
    print()

    print("前序走訪（迭代）:", tree.preorder_traversal_iterative())
    print("中序走訪（迭代）:", tree.inorder_traversal_iterative())
    print("後序走訪（迭代）:", tree.postorder_traversal_iterative())
