// Maximum Binary Tree
// Time: O(n)
// Space: O(n)
// Topics: Array, Divide and Conquer, Stack, Tree, Monotonic Stack, Binary Tree
// Difficulty: Medium

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
#include <stack>

class Solution {
public:
    TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
        stack<TreeNode*> stk; // O(n) space

        // iterate over nums
        for (auto num: nums) {
            TreeNode* node = new TreeNode(num);

            TreeNode* popped = NULL;
            while (!stk.empty() && num > stk.top()->val) { // keep popping until empty or bigger number
                // node->left = stk.top();
                popped = stk.top();
                stk.pop();
            }

            // update pointers
            if (!stk.empty()) {
                stk.top()->right = node;
            }
            node->left = popped;
            stk.push(node);
        }

        // get front of stack to return O(n) time.
        TreeNode* ret = NULL;
        while (!stk.empty()) {
            ret = stk.top();
            stk.pop();
        }

        return ret;
    }
};
