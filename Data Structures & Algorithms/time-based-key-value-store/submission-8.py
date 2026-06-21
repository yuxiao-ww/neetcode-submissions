class TimeMap:

    def __init__(self):
        self.count = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.count:
            self.count[key] = []
        self.count[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.count:
            return ""
        
        arr = self.count[key]
        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res

