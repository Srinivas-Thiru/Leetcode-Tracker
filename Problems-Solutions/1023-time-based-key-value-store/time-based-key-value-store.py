class TimeMap:

    def __init__(self):
        self.hashmap = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].append((value, timestamp))
        else:
            self.hashmap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        vals = self.hashmap[key]
        closeToTimestamp = ""
        l = 0
        r = len(vals) - 1

        while l <= r:
            mid = (l + r) // 2
            if timestamp >= vals[mid][1]:
                closeToTimestamp = vals[mid][0]
                l = mid + 1
            else:
                 r = mid - 1

        return closeToTimestamp
        

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)