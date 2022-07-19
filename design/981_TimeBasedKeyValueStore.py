# Time Based Key-Value Store
# Time: O(n) to set. O(logn) to get
# Space: O(n) overall to set n items
# Topics: Hash Table, String, Binary Search, Design
# Difficulty: Medium

from collections import defaultdict

class TimeMap:
    # All timestamps of "set" are strictly increasing

    def __init__(self):
        self.hashmap = defaultdict(lambda: [])
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        time_value_list = self.hashmap[key]
        if len(time_value_list) == 0:
            return ""
        
        if timestamp < time_value_list[0][0]:
            return ""
        
        # binary search
        left = 0
        right = len(time_value_list) - 1
        
        while left <= right:
            if left == right:
                return time_value_list[left][1]
            
            if left + 1 == right:
                left_timestamp, left_val = time_value_list[left]
                right_timestamp, right_val = time_value_list[right]
                
                if left_timestamp <= timestamp and right_timestamp > timestamp:
                    return left_val
                else:
                    return right_val
            
            mid = (left + right) // 2
            mid_timestamp, mid_val = time_value_list[mid]
            
            if mid_timestamp <= timestamp:
                left = mid
            else:  # mid_timestamp > timestamp
                right = mid


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)