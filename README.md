# 二元搜尋樹的實作與走訪演算法分析：基於 Python 的物件導向設計

Implementation and Traversal Algorithm Analysis of Binary Search Tree: An Object-Oriented Design Based on Python

## 題目目標
建立自訂二元搜尋樹類別（Binary Search Tree, BST），完整實作節點插入、查找、樹資訊查詢與三種深度優先遍歷（前序、中序、後序），並分析各操作時間複雜度。

## 我設計的資料結構：二元搜尋樹（BST）
本作業使用物件導向設計，包含兩個核心類別：

### 1. 節點類別（Node）
- value：節點值
- left：左子節點
- right：右子節點

### 2. 二元搜尋樹類別（BinaryTree）
核心操作：

1. insert(value)：依 BST 規則插入節點
2. search(value)：查找指定值是否存在
3. size()：計算節點總數
4. height()：計算樹高
5. preorder_traversal()：前序遍歷（根->左->右）
6. inorder_traversal()：中序遍歷（左->根->右）
7. postorder_traversal()：後序遍歷（左->右->根）

另外提供與題目命名一致的方法：

- PreorderTraversal()
- InorderTraversal()
- PostorderTraversal()

## 操作流程（高階）
1. 初始化 BinaryTree 物件
2. 透過 insert() 或建構子批次插入資料建立 BST
3. 使用 search() 驗證指定值是否存在
4. 使用 size()、height() 取得樹的整體資訊
5. 分別執行 preorder/inorder/postorder 輸出遍歷結果
6. 驗證遞迴與迭代版本結果一致

## 時間複雜度分析
令輸入大小為 $n$（節點數量），$h$ 為樹高。

### 1) Insert（插入）
- 需沿單一路徑比較至插入位置
- 時間：$O(h)$
- 平衡樹時約為 $O(\log n)$；退化時為 $O(n)$

### 2) Search（查找）
- 與插入同樣沿路徑向下查找
- 時間：$O(h)$

### 3) Get Height / Size（計算高度與節點數）
- 需遍歷全部節點
- 時間：$O(n)$
- 空間：$O(h)$（遞迴堆疊）

### 4) Preorder / Inorder / Postorder Traversal（三種遍歷）
- 每個節點恰好訪問一次
- 時間：$O(n)$
- 空間：$O(h)$

### 綜合複雜度
| 操作 | 時間複雜度 | 空間複雜度 | 說明 |
|---|---|---|---|
| insert() | $O(h)$ | $O(h)$ | BST 路徑插入 |
| search() | $O(h)$ | $O(1)$ | 迭代查找 |
| size() | $O(n)$ | $O(h)$ | 遍歷全部節點 |
| height() | $O(n)$ | $O(h)$ | 遞迴取最大深度 |
| preorder_traversal() | $O(n)$ | $O(h)$ | DFS 前序 |
| inorder_traversal() | $O(n)$ | $O(h)$ | DFS 中序 |
| postorder_traversal() | $O(n)$ | $O(h)$ | DFS 後序 |

## 程式檔案
1. tree_traversal.py - BinaryTree 與三種遍歷完整實作
2. README.md - 作業說明、流程與複雜度分析

可直接執行：

```bash
python tree_traversal.py
```

## 實測結果（實際執行輸出）
本次執行結果如下：

```text
指定樹形:
        50
      /    \
    30      70
   /  \    /  \
 20   40  60   80

節點資料: [50, 30, 70, 20, 40, 60, 80]
節點總數: 7
樹高: 2
搜尋 60: True
搜尋 99: False

前序走訪（遞迴）: [50, 30, 20, 40, 70, 60, 80]
中序走訪（遞迴）: [20, 30, 40, 50, 60, 70, 80]
後序走訪（遞迴）: [20, 40, 30, 60, 80, 70, 50]

前序走訪（迭代）: [50, 30, 20, 40, 70, 60, 80]
中序走訪（迭代）: [20, 30, 40, 50, 60, 70, 80]
後序走訪（迭代）: [20, 40, 30, 60, 80, 70, 50]

【基礎測試】
  三種走訪輸出正確，且遞迴與迭代結果一致。
```

## 流程圖

### 前序走訪（Preorder）
```mermaid
flowchart TD
  A[開始 preorder(node)] --> B{node 是否為空?}
  B -- 是 --> C[返回]
  B -- 否 --> D[訪問 node.value]
  D --> E[遞迴 preorder(node.left)]
  E --> F[遞迴 preorder(node.right)]
  F --> G[結束]
```

### 中序走訪（Inorder）
```mermaid
flowchart TD
  A[開始 inorder(node)] --> B{node 是否為空?}
  B -- 是 --> C[返回]
  B -- 否 --> D[遞迴 inorder(node.left)]
  D --> E[訪問 node.value]
  E --> F[遞迴 inorder(node.right)]
  F --> G[結束]
```

### 後序走訪（Postorder）
```mermaid
flowchart TD
  A[開始 postorder(node)] --> B{node 是否為空?}
  B -- 是 --> C[返回]
  B -- 否 --> D[遞迴 postorder(node.left)]
  D --> E[遞迴 postorder(node.right)]
  E --> F[訪問 node.value]
  F --> G[結束]
```

## 結論
本作業已完整實作 BST 的核心操作與三種樹遍歷，並完成複雜度分析與輸出驗證。實作結果符合 Tree Traversal 題目要求，且中序遍歷可驗證 BST 之有序特性。整體程式具可讀性、可維護性與擴充性，可作為後續平衡樹或刪除操作的基礎。
