/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if (root == nullptr) {
            return true;
        } 
        else if (heightHelper(root) == -1) {
            return false;
        } else {
            return true;
        }
    }
    int heightHelper(TreeNode* LorR) {
        int leftHeight = 0;
        int rightHeight = 0;
        if (LorR == nullptr) {
            return 0;
        }
        else {
            leftHeight = heightHelper(LorR->left);
            if (leftHeight != -1) leftHeight += 1;
            rightHeight = heightHelper(LorR->right);
            if (rightHeight != -1) rightHeight += 1;
            if (abs(leftHeight - rightHeight) > 1) {
                return -1;
            }
        }
        return max(leftHeight, rightHeight);
    }
};
