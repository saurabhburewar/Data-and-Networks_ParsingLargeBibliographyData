import snap
from time import time 
import sqlite3


G = snap.TNEANet.New()
G.AddIntAttrE("Multiplicity")
G.AddIntAttrN("author_id")

def total_time(start, end):
    total = end - start
    hours = total // 3600
    total -= hours * 3600
    mins = total // 60
    total -= mins * 60
    #total = total // 1
    print("Total time taken:")
    print("Hour:\t\t\t%d" %hours)
    print("Minutes:\t\t%d" %mins)
    print("Seconds:\t\t%d" %total)

def save():
    print("Saving the Graph......")
    labels = snap.TIntStrH()
    for NI in G.Nodes():
        labels[NI.GetId()] = "white"
    snap.SaveGViz(G, "data.dot", "Directed multigraph Co_author network", True, labels)

def ConnectedComponents():
    ComponentDist = snap.TIntPrV()
    snap.GetWccSzCnt(G, ComponentDist)
    Component = 0
    for comp in ComponentDist:
        print("Size: %d - Number of Components: %d" % (comp.GetVal1(), comp.GetVal2()))
        Component += comp.GetVal2()
    #print('Relative size of WCC in Directed Graph:', snap.GetMxWccSz(G))
    print("Number of total Components is %d"%Component)
    print("Connectedness of Graph :\t\t" , end = "")
    print(snap.IsConnected(G))

def AddNodes(Node):
    if(G.IsNode(Node)):
        return
    G.AddNode(Node)
    G.AddIntAttrDatN(Node, int(Node) , "author_id")

def AddEdge(src, dst, weight):
    G.AddEdge(src, dst)
    G.AddIntAttrDatE(G.GetEI(src, dst), int(weight) , "Multiplicity")

def main():
    conn = sqlite3.connect("Connection.db")
    sql = "SELECT src,dst,Multiplicity FROM CoAuthor WHERE Multiplicity >= 1"
    cursor = conn.execute(sql)
    for row in cursor:
        src = int(row[0])
        dst = int(row[1])
        weight = int(row[2])  
        AddNodes(src)
        AddNodes(dst)
        AddEdge(src, dst, weight)  
    save() 
    ConnectedComponents()  
                
if __name__ == "__main__":
    start_time = time()
    main()
    end_time = time()
    total_time(start_time, end_time)
    

