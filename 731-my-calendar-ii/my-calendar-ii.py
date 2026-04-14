class MyCalendarTwo(object):

    def __init__(self):
        self.events=[]
        

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        insort(self.events,(startTime,1))
        insort(self.events,(endTime,-1))

        total_count=0

        for _, count in self.events:
            total_count+=count
            if total_count>=3:
                self.events.remove((startTime,1))
                self.events.remove((endTime,-1))
                return False
        return True

        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)