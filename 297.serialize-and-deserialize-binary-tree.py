#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        preorder = []

        def dfs(curr):
            if not curr:
                preorder.append(str(None))
            else:
                preorder.append(str(curr.val))
                dfs(curr.left)
                dfs(curr.right)

        dfs(root)

        return ",".join(preorder)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        data = [None if x == 'None' else int(x) for x in data.split(",")]
        print(data)

        def build(idx):
            if data[idx] is None:
                return (None, idx + 1)

            node = TreeNode(data[idx])

            # idx + 1 is immediate left child
            left, ldx = build(idx + 1)

            right, rdx = build(ldx)

            node.left = left
            node.right = right

            return (node, rdx)

        return build(0)[0]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# @lc code=end
