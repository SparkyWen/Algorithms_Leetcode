# 二叉树第K个最小元素

## 1. 知识点

> 1. 在二叉搜索树中，任意子节点都满足“左子节点 < 根节点 < 右子节点”的规则。因此二叉搜索树具有一个重要性质：**二叉搜索树的中序遍历为递增序列**。
>
>    <img src="./property.png" style="zoom:20%;" />

> 2. 思路：
>
>    为求第 k 个节点，需要实现以下三项工作：
>
>    1. 递归遍历时计数，统计当前节点的序号。
>    2. 递归到第 k 个节点时，应记录结果 res 。
>    3. 记录结果后，后续的遍历即失去意义，应提前返回。

> 3. return用法：
>
>    ```
>    1) “单写一个 return” 是什么？
>    
>    在 Python 里，return 立即结束当前函数，把控制权交回给调用它的上层；
>    
>    “单写 return” 等价于 return None（函数不显式返回时默认就是 None）。
>    
>    一旦执行到 return，该函数后面的代码就不会再执行。
>    ```
>
> 4. 理解的关键核心：==函数到结尾，没有更多代码，所以 dfs(4) 自然执行完毕、栈帧被弹出，控制权回到调用它的上一层：dfs(3)。==
>
>    

## 2. 代码

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            if not root: return
            dfs(root.left)              # 先走左子树（更小的元素）
            if self.k == 0: return      # 如果已经找到了，直接“短路”返回
            self.k -= 1                 # 访问当前节点，相当于“拿到”一个更大的元素
            if self.k == 0:             # 刚好是第 k 个
                self.res = root.val
            dfs(root.right)             # 再走右子树（更大的元素）

        self.k = k
        dfs(root)
        return self.res
```

### 	一、核心思想（为什么可行）

- **BST 性质**：左子树所有值 ≤ 根值 ≤ 右子树所有值（或严格 <，实现约定即可）。

- **中序遍历**：在 BST 上的访问顺序就是升序序列。

- 因此：每访问一个节点（走到“根”这一步），就拿到下一个更大的元素；从 `k` 开始往下数，数到 0 时的那个值就是答案。

- ```
  用这棵 BST（节点值互不相同，典型题设）：
  
          5
        /   \
       3     7
      / \     \
     2   4     8
  
  
  这棵树的中序序列是：[2, 3, 4, 5, 7, 8]
  
  示例 1：k = 4（期望答案是 5）
  
  我们跟着代码的执行顺序与 self.k 的变化走：
  
  进入 dfs(5)
  
  先递归左：dfs(3)
  
  进入 dfs(3)
  
  先递归左：dfs(2)
  
  进入 dfs(2)
  
  ***：对叶子来说，叶子的左孩子是 None，于是会先调用一次 dfs(None)，它命中基线条件立刻返回，然后才轮到“访问叶子本身”的那几行。***
  
  先递归左：dfs(None) → 返回
  
  self.k == 0? 否（初始 self.k = 4）
  
  访问当前节点 2：self.k 由 4 → 3
  
  递归右：dfs(None) → 返回
  
  dfs(2) 结束
  
  回到 dfs(3)
  
  检查 self.k == 0? 否（现在是 3）
  
  访问当前节点 3：self.k 由 3 → 2
  
  递归右：dfs(4)
  
  进入 dfs(4)
  
  先递归左：dfs(None) → 返回
  
  self.k == 0? 否（现在是 2）
  
  访问当前节点 4：self.k 由 2 → 1
  
  递归右：dfs(None) → 返回
  
  dfs(4) 结束
  
  回到 dfs(5)
  
  检查 self.k == 0? 否（现在是 1）
  
  访问当前节点 5：self.k 由 1 → 0，命中！
  
  于是 self.res = 5
  
  递归右：dfs(7)
  
  注意：虽然已经找到答案，但代码仍然调用了 dfs(7)；不过进入 dfs(7) 后很快会因为 self.k == 0 立即返回（见下）。
  
  进入 dfs(7)
  
  先递归左：dfs(None) → 返回
  
  self.k == 0? 是，因此直接 return，右子树完全不再深入
  
  dfs(7) 结束
  
  整体返回，self.res == 5，与中序序列第 4 个元素一致 ✅
  
  小结：访问顺序正是中序：2（k=3）、3（k=2）、4（k=1）、5（k=0 命中）。
  命中之后，借助“if self.k == 0: return”这个短路判断，能避免继续无谓的遍历。
  ```

  ```python
  3) if not root: return 的作用
  def dfs(root):
      if not root: return   # 遇到空指针，结束当前调用
      ...
  
  
  这是递归的基线条件。
  
  当递归深入到“空孩子”（None）时，立刻返回，防止继续往下递归（不然会无限下降或报错）。
  
  这同样是“单写 return”，等价于 return None：结束这一层递归。
  ```

  ```python
  def dfs(root):
      if not root:                     # [1] 基线：None 直接返回
          return
      dfs(root.left)                   # [2] 先递归左子树
      if self.k == 0: return           # [3] 若已经找到，短路返回
      self.k -= 1                      # [4] 访问当前节点（计数 -1）
      if self.k == 0: self.res = root.val  # [5] 命中第 k 个
      dfs(root.right)                  # [6] 再递归右子树
  关键点：只有当第 [2] 行的递归返回后，程序计数器才会继续往下走到 [3]、[4]、[5]。
  对叶子 2 来说：
  
  调用 dfs(2)，不是 None → 进入
  
  执行 [2] dfs(2.left)，但 2.left 是 None
  
  调用 dfs(None) 命中 [1]，立刻返回（什么也不做）
  
  回到 dfs(2) 这一层，继续往下执行 [3][4][5]：
  
  self.k == 0? 否（初始是 4）
  
  self.k -= 1：4 → 3
  
  不是 0，不赋值
  
  执行 [6] dfs(2.right)，2.right 也是 None，再次命中 [1] 直接返回
  
  dfs(2) 完整结束，把控制权交回给它的调用者（比如 dfs(3)）
  
  这正是你看到的顺序：“先递归左：dfs(None) → 返回 → 检查/访问当前节点 → 递归右：dfs(None) → 返回”。
  ```

  

```python
左子树为空，啥也不干就返回，然后：

if self.k == 0: return      # 现在 self.k 还是 4
self.k -= 1                  # self.k: 4 -> 3
if self.k == 0: self.res = ...
dfs(1.right)                 # 右子树也是 None，直接 return


此时已经按中序访问了第 1 个节点：1，k 从 4 变成了 3。

dfs(1) 完成，返回到谁？
👉 返回到它的调用者：dfs(2)。



dfs(2.left)  # 已经执行完 dfs(1)
# 现在继续向下走：
if self.k == 0: return      # 当前 self.k = 3，不返回
self.k -= 1                  # self.k: 3 -> 2
if self.k == 0: self.res = ...
dfs(2.right)                 # None, 直接 return


现在我们按中序访问了第 2 个节点：2，k 从 3 变成了 2。

dfs(2) 完成，返回到 dfs(3)。


dfs(4.left)   # None，直接 return
这时 self.k = 1，继续：

python
Copy code
if self.k == 0: return      # k = 1 ≠ 0
self.k -= 1                  # self.k: 1 -> 0
if self.k == 0:              # 条件满足
    self.res = root.val      # 记录答案：self.res = 4
dfs(4.right)                 # 虽然还会调用，但后面 self.k==0 会一路短路

```

