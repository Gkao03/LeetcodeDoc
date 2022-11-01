# Number of Atoms
# Time: O(n^2). n is length of formula. each update can take up to O(n) for O(n) updates.
# Space: O(n)
# Topics: Hash Table, String, Stack, Sorting
# Difficulty: Hard

from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        bracket_idx_stack = []
        
        i = 0
        while i < len(formula):
            if formula[i] == '(':
                bracket_idx_stack.append(len(stack))
                i += 1
            elif formula[i].isupper():
                capital = formula[i]
                start_idx = j = i + 1
                
                while j < len(formula) and formula[j].islower():
                    j += 1
                    
                element = capital + formula[start_idx:j]
                
                integer = []
                while j < len(formula) and formula[j].isdigit():
                    integer.append(formula[j])
                    j += 1
                    
                count = 1
                if len(integer) > 0:
                    count = int("".join(integer))
                    
                stack.append([element, count])
                i = j  # update index
            else:  # remaining case has to be ')'
                pop_idx = bracket_idx_stack.pop()
                j = i + 1
                
                integer = []
                while j < len(formula) and formula[j].isdigit():
                    integer.append(formula[j])
                    j += 1
                    
                count = 1
                if len(integer) > 0:
                    count = int("".join(integer))
                    
                if count > 1:
                    update_idx = len(stack) - 1
                    while update_idx >= pop_idx:
                        stack[update_idx][1] *= count
                        update_idx -= 1
                        
                i = j  # update index
                
        hash_table = defaultdict(lambda: 0)
        for element, val in stack:
            hash_table[element] += val
        
        result = []
        for element in sorted(hash_table.keys()):
            result.append(element)
            if hash_table[element] > 1:
                result.append(str(hash_table[element]))
        
        return "".join(result)
