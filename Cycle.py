from AdjacencyList import AList

class Cycle:

    def __init__(self) -> None:
        self.alist=None
        num=self.initilize()
        self.visited=[-1]*num
        self.timer=1
        self.TimerStart=[None]*num
        self.TimerEnd=[None]*num
        self.cycle=0
        
    def initilize(self):
        num=5
        self.alist=AList(num)
        self.alist.insert(0,1)
        self.alist.insert(1,3)
        #self.alist.insert(3,4)
        self.alist.insert(4,0)
        self.alist.insert(1,2)
        #self.alist.insert(3,4)

        '''
        g1.addEdge(1, 0); 
        g1.addEdge(0, 2); 
        g1.addEdge(2, 1); 
        g1.addEdge(0, 3); 
        g1.addEdge(3, 4); 
        '''

        self.alist.print_graph()
        return num

    def DFS_Start(self, node):

        self.visited[node]=0
        self.TimerStart[node]=self.timer
        self.timer+=1
        print(node,"==>",end="")
        k=self.alist.aL[node]
        u=k.nodeVal
        while k:
            if self.visited[u]==-1:
                self.DFS_Start(u)
            k=k.next
            if k:
                u=k.nodeVal
        if self.visited[u]==0:
                self.cycle+=1
        
        self.TimerEnd[node]=self.timer
        self.timer+=1
        self.visited[node]=1
        print(node,"==>",end="")
    
    def print_time(self):
        for i in range(self.alist.nodes):
            print(f'Node {i}: Start Time {self.TimerStart[i]} and End Time {self.TimerEnd[i]}')


dfs=Cycle()
dfs.DFS_Start(4)
print()
dfs.print_time()
print(dfs.cycle)