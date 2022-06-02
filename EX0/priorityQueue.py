
import heapq
from heapq import *

class PriorityQueue:


    def __init__(self):
        self.heap = []
        self.count=0
        heapq.heapify(self.heap)

    def findItem ( self, item):
        pos=-1
        i=0
        while (i< len(self.heap)):
            tempPr , tempItem = self.heap[i]
            if (tempItem==item):
                pos=i
                break
            i+=1
        return pos


    def push(self , item, priority):

        if (self.findItem(item) == -1 ):
            heapq.heappush(self.heap , (priority, item))
            #print("Item " , item , " with priority " , priority , " pushed successfully")
            self.count+=1
        else :
            print("Item, " , item , " already inside there ")


    def isEmpty(self):
        if (self.count ==0):
            return True
        else :
            return False

    def pop(self):
        if (self.isEmpty() == False ):
            self.count-=1
            priority, item = heappop(self.heap)
            return item
        else :
            return None

    def Update(self, item , priority):

        pos = self.findItem(item)
        if(pos != -1):
            oldpr , olditem = self.heap[pos]

            if (oldpr >= priority) :
                self.heap[pos]= (priority , item)

                heapq.heapify(self.heap)
                print(" item " ,item , " old priority = " , oldpr ," new priority = " , priority)

            else:
                print("Item already inside with bigger priority")
        else:
            self.push(item,priority)

    def HeadPriority(self):
        if (self.isEmpty() == False ):
            tempPr , tempItem = self.heap[0]
            return tempPr
        else :
            return None

def PQSort(listoula):
    pq = PriorityQueue()
    i=0
    while (i< len(listoula)):
        pq.push("item"+str(i),listoula[i])
        i+=1
    sorted=[]
    while (pq.isEmpty()==False) :
        sorted.append(pq.HeadPriority())
        item=pq.pop()
    return sorted
