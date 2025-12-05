class Node:
    __slots__='prev', 'next', 'value', 'key'

    def __init__(self, key=0, value=0):
        self.key=key
        self.value=value

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.key_to_node={}
        self.dummy=Node()
        self.dummy.prev=self.dummy
        self.dummy.next=self.dummy
    

    def get_node(self, key:int):
        if key not in self.key_to_node:
            return None

        node=self.key_to_node[key]
        self.remove(node)

        self.push_front(node)
        return node
        

    def get(self, key: int) -> int:
        node=self.get_node(key)
        return node.value if node else -1
        

    def put(self, key: int, value: int) -> None:
        node=self.get_node(key)
        if node:
            node.value=value
            return
        self.key_to_node[key]=node=Node(key, value)
        self.push_front(self.key_to_node[key])
        if len(self.key_to_node)>self.capacity:
            back_node=self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)

    def remove(self, x:Node)->None:
        x.prev.next=x.next
        x.next.prev=x.prev

    def push_front(self, x:Node)->None:
        x.prev=self.dummy
        x.next=self.dummy.next
        x.next.prev=x
        x.prev.next=x
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)