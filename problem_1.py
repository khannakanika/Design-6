"""
Time Complexity : O(1)- for all get , release and check 
Space Complexity : O(2n)- for queue and the set 
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No


Your code here along with comments explaining your approach:
For this solution we will be making a queue and a hashset and will input all the numbers in the range
inside both. For get, we will just pop out the leftmost element from queue and remoe it from the hashset as
well. For check, we just need to check if it is present inside map or not. For release, we will add the number
back to queue and set.
"""

from collections import deque


class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.q = deque()
        self.map = set()
        for i in range(0, maxNumbers):
            self.q.append(i)
            self.map.add(i)

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if self.q:
            a = self.q.popleft()
            self.map.remove(a)
            return a
        return -1

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return (number in self.map)

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number not in self.map:
            self.map.add(number)
            self.q.append(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
