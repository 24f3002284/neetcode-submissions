class TimeMap:

    def __init__(self):
        self.dict={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key]=[]

        self.dict[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        timeValues=self.dict.get(key,[])
        ans=""

        low,high=0,len(timeValues)-1
        while low<=high:
            mid=(low+high)//2

            if timeValues[mid][1]==timestamp:
                return timeValues[mid][0]

            elif timeValues[mid][1]<timestamp:
                ans=timeValues[mid][0]
                low=mid+1

            else:
                high=mid-1

        return ans