// In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

// Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

// We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

// Return true if and only if the nodes corresponding to the values x and y are cousins.

 

// Example 1:


// Input: root = [1,2,3,4], x = 4, y = 3
// Output: false

class Solution {
    TreeNode xParent = null, yParent = null;
    int xDepth = -1, yDepth = -1;
    public boolean isCousins(TreeNode root, int x, int y) {
        
        // performing dfs to search the nodes 
        dfs(root, null, x, y, 0);
        return xDepth == yDepth && xParent != yParent;
        
    }
    public void dfs(TreeNode root, TreeNode parent, int x, int y, int depth){
        if(root == null)
            return;
        if(x == root.val)
        {
            xParent = parent;
            xDepth = depth;
        }
        else if(y == root.val)
        {
            yParent = parent;
            yDepth = depth;
        }
        else{
            dfs(root.left, root, x ,y, depth + 1);
            dfs(root.right, root, x ,y ,depth + 1);
        }
    }
}