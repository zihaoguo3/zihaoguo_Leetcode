class MyCalendarThree(object):

    def __init__(self):
        self.events=[]

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        insort(self.events,(startTime,1))
        insort(self.events,(endTime,-1))

        total=0
        max_count=0

        for _, count in self.events:
            total+=count
            if total>max_count:
                max_count=total
        return max_count
            
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)