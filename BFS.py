from AdjacencyList import AList
from Queue import Queue
class BFS:

    def __init__(self) -> None:
        self.alist=None
        num=self.initilize()
        self.visited=[-1]*num
        self.Queue=Queue(10*num)

    def initilize(self):
        num=5
        self.alist=AList(num)
        self.alist.insert(0,2)
        self.alist.insert(0,3)
        self.alist.insert(0,4)
        self.alist.insert(1,3)
        self.alist.insert(1,4)
        self.alist.insert(2,3)
        self.alist.insert(3,4)

        self.alist.print_graph()
        return num
    
    def BFS_Start(self, node):
        self.visited[node]=0
        k=self.alist.aL[node]
        while k:
            self.Queue.insert(k.nodeVal)
            k=k.next
        
        

        while not self.Queue.isEmpty:
            u=self.Queue.delete()


            


bfs=BFS()
bfs.BFS_Start(0)