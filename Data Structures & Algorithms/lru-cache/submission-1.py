class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        # self.left,self.right=Node(0,0),Node(0,0) # left=>LRU,right=>MRU
        self.prev,self.next=None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={} # to store the key node pair

        # left=>LRU,right=>MRU
        self.left,self.right=Node(0,0),Node(0,0)
        self.right.prev,self.left.next=self.left,self.right #connect left and right. to insert a node, insert it in the middle of both

    # remove a node from list
    def remove(self,node):
        prv,nxt=node.prev,node.next
        prv.next,nxt.prev=nxt,prv

    # insert a node to the right
    def insert(self,node):
        prv,nxt=self.right.prev,self.right
        prv.next,nxt.prev=node,node
        node.prev,node.next=prv,nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # del self.cache[key]
            self.remove(self.cache[key])
            #dont forget to update the value!!
            self.cache[key].val=value
            self.insert(self.cache[key])
            return

        if len(self.cache)>=self.cap:
            # lru=self.cache[self.left.next]
            # self.remove(lru) #remember that lru is the node. so dont write self.remove(self.cache[lru])
            # del self.cache[lru.key] #imp!! we have to del key of a dictionary, not del self.cache[lru]
            # lru=cache[self.left.next] # the leftmost node, not =cache[lru.next] bcz, keys of cache are not node, they are values.
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
