 def printMiddle(self):
        slow_ptr=self.head
        fast_ptr=self.head
        if self.head is not None:
            while(fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr=fast_ptr.next.next
                slow_ptr=slow_ptr.next
            print("The middle element is",slow_ptr.data)        