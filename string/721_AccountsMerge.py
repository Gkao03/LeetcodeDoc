# Accounts Merge
# Time: O(n^2). Where n is number of emails and the emails are fully connected
# Space: O(n^2). The graph representation will take O(n^2) space if fully connected
# Topics: Array, String, Depth-First Search, Breadth-First Search, Union Find
# Difficulty: Medium
# Notes: For every pair of emails in the same account, draw an edge between those emails. 
# The problem is about enumerating the connected components of this graph.

from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = defaultdict(lambda: [])
        unvisited_set = set()
        
        # create adjacency list
        for account in accounts:
            name = account[0]
            emails = account[1:]
            
            for i, emaili in enumerate(emails):
                for j, emailj in enumerate(emails):
                    if i != j:
                        adj_list[(name, emaili)].append((name, emailj))
                    else:
                        adj_list[(name, emaili)]  # add a node with no connecting nodes
                    unvisited_set.add((name, emaili))
                        
        merged_accounts = []
        
        while len(unvisited_set) > 0:
            stack = []
            curr_name, curr_email = unvisited_set.pop()
            stack.append((curr_name, curr_email))  # get a random account
            curr_emails_merge = []
            
            while len(stack) > 0:
                _, curr_email = stack.pop()
                curr_emails_merge.append(curr_email)
                
                adj_accounts = adj_list[(curr_name, curr_email)]
                for adj_name, adj_email in adj_accounts:
                    if (adj_name, adj_email) in unvisited_set:
                        stack.append((adj_name, adj_email))
                        unvisited_set.remove((adj_name, adj_email))
                        
            merged_accounts.append([curr_name] + sorted(curr_emails_merge))  # O(nlogn) to sort for n emails
            
        return merged_accounts
