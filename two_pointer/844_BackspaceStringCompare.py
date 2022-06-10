# Backspace String Compare
# Time: O(n + m). n is length of s. m is length of t.
# Space: O(1)
# Topics: Two Pointers, String, Stack, Simulation
# Difficulty: Easy

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_ptr = len(s) - 1
        t_ptr = len(t) - 1
        
        s_hashtag_count = 0
        t_hashtag_count = 0
        
        while s_ptr >=0 and t_ptr >= 0:
            if s[s_ptr] == '#' or t[t_ptr] == '#':
                if s[s_ptr] == '#':
                    s_hashtag_count += 1
                    s_ptr -= 1
                if t[t_ptr] == '#':
                    t_hashtag_count += 1
                    t_ptr -= 1
            else:  # both chars are not '#'
                if s_hashtag_count > 0 or t_hashtag_count > 0:
                    if s_hashtag_count > 0:
                        s_hashtag_count -= 1
                        s_ptr -= 1
                    if t_hashtag_count > 0:
                        t_hashtag_count -= 1
                        t_ptr -= 1
                else:  # no backspaces needed for both strings
                    if s[s_ptr] != t[t_ptr]:
                        return False
                    s_ptr -= 1
                    t_ptr -= 1
                    
        # check remaining characters. either s_ptr or t_ptr is -1
        # should be no more letters if no backspaces available
        while s_ptr >= 0:
            if s[s_ptr] != '#':  # is a letter
                if s_hashtag_count <= 0:
                    return False
                s_hashtag_count -= 1
                s_ptr -= 1
            else:  # hashtag
                s_hashtag_count += 1
                s_ptr -= 1
                
        while t_ptr >= 0:
            if t[t_ptr] != '#':  # is a letter
                if t_hashtag_count <= 0:
                    return False
                t_hashtag_count -= 1
                t_ptr -= 1
            else:  # hashtag
                t_hashtag_count += 1
                t_ptr -= 1
                    
        return True
