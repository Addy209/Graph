# class Graph:
#     def __init__(self,data) -> None:
#         self.nodeVal=data
#         self.next=None

from Graph import Graph


class AList:
    def __init__(self, all_nodes) -> None:
        self.nodes=all_nodes
        self.aL=[None]*self.nodes
    
    def insert(self, src, dest):
        '''
        Creats Adjacency List 
        1. Create src and dest node.
        2. put the content of aL[src] in dest node's next.
        3. Replace the content of aL[src] with dest node.
        4. All data prior to inserting dest node will be in the dest node's next variable.
        5. As this is an undirected graph, do the same for src node and aL[dest].
        '''
        src_node=Graph(src)
        dest_node=Graph(dest)

        dest_node.next=self.aL[src]
        self.aL[src]=dest_node

        src_node.next=self.aL[dest]
        self.aL[dest]=src_node

    def print_graph(self) ->None:
        for i in range(self.nodes):
            print(f"{i} is adjacent to : |{i}|", end=" ")
            k=self.aL[i]
            while(k is not None ):
                print(f"-->{k.nodeVal}",end="")
                k=k.next
            print()

if __name__=="__main__":
    al=AList(5)
    al.insert(0,2)
    al.insert(0,3)
    al.insert(0,4)
    al.insert(1,3)
    al.insert(1,4)
    al.insert(2,3)
    al.insert(3,4)

    al.print_graph()