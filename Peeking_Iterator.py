# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        
        self._next = iterator.next()
        self._iterator = iterator
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next
        

    def next(self):
        """
        :rtype: int
        """
        print("Done with Next")
        if self._next is None:
            raise StopIteration()
        else:
            return_val = self._next
            if self._iterator.hasNext():
                self._next = self._iterator.next()
            else:
                self._next = None
            
            return return_val
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self._next is None:
            return False
        return True

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].