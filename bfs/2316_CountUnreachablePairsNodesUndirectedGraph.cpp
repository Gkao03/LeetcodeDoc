// Count Unreachable Pairs of Nodes in an Undirected Graph
// Time: O(V + E) to traverse all nodes and edges
// Space: O(V + E) to store adjacency list and visited set.
// Topics: Depth-First Search, Breadth-First Search, Union Find, Graph
// Difficulty: Medium

#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <set>

class Solution {
public:
    long long countPairs(int n, vector<vector<int>>& edges) {
        // first build adj map from edges
        map<int, set<int>> adj_list; // O(E) space
        for (auto edge: edges) {
            int node1 = edge[0];
            int node2 = edge[1];

            // insert both edges as undirected
            adj_list[node1].insert(node2);
            adj_list[node2].insert(node1);
        }

        // initialize some stuff
        set<int> visited;  // O(V) space
        long long answer = 0;

        for (int i = 0; i < n; i++) {
            if (visited.find(i) == visited.end()) {  // node not visited yet
                int curr_connected = 0;
                queue<int> q;
                q.push(i);
                visited.insert(i);

                while (!q.empty()) {
                    int curr_node = q.front();
                    q.pop();
                    curr_connected++;

                    for (auto next_node: adj_list[curr_node]) {
                        if (visited.find(next_node) == visited.end()) {  // not visited yet
                            q.push(next_node);
                            visited.insert(next_node);
                        }
                    }
                }

                answer += curr_connected * (visited.size() - curr_connected);
            }
        }

        std::cout << n << " " << visited.size() << std::endl;

        return answer;
    }
};
