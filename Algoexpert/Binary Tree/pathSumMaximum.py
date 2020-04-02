def maxPathSum(tree):

    def dp(tree):
        if tree is None:
            return 0

        sum = max(dp(tree.left)+dp(tree.right)+tree.value, tree.value+dp(tree.left), tree.value+dp(tree.right))
        return sum

{
  "nodes": [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "3", "left": "6", "right": "7", "value": 3},
    {"id": "4", "left": None, "right": None, "value": 4},
    {"id": "5", "left": None, "right": None, "value": 5},
    {"id": "6", "left": None, "right": None, "value": 6},
    {"id": "7", "left": None, "right": None, "value": 7}
  ],
  "root": "1"
}