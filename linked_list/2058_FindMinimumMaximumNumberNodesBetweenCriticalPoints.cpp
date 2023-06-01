// Find the Minimum and Maximum Number of Nodes Between Critical Points
// Time: O(n)
// Space: O(1)
// Topics: Linked List
// Difficulty: Medium

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <limits.h>
#include <vector>

class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        // at least 2 nodes exist
        ListNode* prev = head;
        ListNode* curr = prev->next;
        ListNode* nxt = curr->next;
        int counter = 0;
        int begin_cp = -1;  // point of first critical point
        int curr_cp = -1;  // point of most recent critical point
        int min_distance = INT_MAX;
        int max_distance = -1;

        while (nxt != NULL) {
            // found a critical point
            if (prev->val < curr->val && nxt->val < curr->val || prev->val > curr->val && nxt->val > curr->val) {
                if (begin_cp == -1) {
                    begin_cp = counter;
                    curr_cp = counter;
                } else {
                    max_distance = counter - begin_cp;
                    min_distance = std::min(min_distance, counter - curr_cp);
                    curr_cp = counter;
                }
            }

            // update pointers
            prev = curr;
            curr = nxt;
            nxt = nxt->next;
            counter++;
        }

        vector<int> answer{min_distance, max_distance};
        if (min_distance == INT_MAX) {
            answer[0] = -1;
        }

        return answer;
    }
};
