class Queue:
    def __init__(self,size) -> None:
        self.size=size
        self.queue=[None]*self.size
        self.front,self.rear=0,0
    
    def initilize(self):
        self.front,self.rear=0,0
    
    def insert(self,data):
        if self.front==self.size:
            raise Exception('Queue Full')
        else:
            self.queue[self.front]=data
            self.front+=1
            #self.printqueue()

    def delete(self):
        if self.rear==self.front:
            raise Exception('Queue Empty')
        else:
            val=self.queue[self.rear]
            self.rear+=1
            #self.printqueue()
            return val

    @property
    def isEmpty(self):
        return self.rear==self.front
    
    def printqueue(self):
        print('[',end="")
        for i in range(self.rear,self.front):
            print(self.queue[i],end=" , ")
        print(']')


if __name__=="__main__":
    q=Queue(5)
    q.insert(1)
    q.insert(2)
    q.insert(3)
    q.insert(4)
    q.insert(5)
    q.insert(6)
    q.delete()
    q.delete()
    q.delete()
    q.delete()
    q.delete()
    q.delete()


