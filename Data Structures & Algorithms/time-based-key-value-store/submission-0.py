class TimeMap:

    def __init__(self):
        # self.dict=collections.defaultdict(list)
        self.dict={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in self.dict:
        self.dict[(key,timestamp)]=value

    def get(self, key: str, timestamp: int) -> str:
        for i in range(timestamp,-1,-1):
            if (key,i) in self.dict:
                return self.dict[(key,i)]

        return ""
                