class CountSquares:

    def __init__(self):
        self.mp=defaultdict(int) #means val of each key will be of int datatype
        self.points=[]

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points.append((x,y))
        self.mp[(x,y)]+=1

    def count(self, point: List[int]) -> int:
        px,py=point[0],point[1]
        
        ans=0
        for p in self.points:
            x,y=p
            if x==px or y==py or abs(x-px)!=abs(y-py):
                continue
            
            ans+=self.mp[(x,py)]*self.mp[(px,y)]

        return ans
