import snap

def multiplicity(G, Edges):
    MaxE = 0
    MinE = 500
    MedianE = 0
    MeanE = 0
    print("\nEDGE STATS:\n")
    Edge = snap.TIntV()
    it = Edges.BegI()
    while(not it.IsEnd()):
        Edge.Add(int(it.GetDat()))
        it.Next()
    Edge.Sort()
    MaxE = Edge[Edge.Len()-1]
    MinE = Edge[0]
    Index = Edge.Len()//2
    for val in Edge:
        MeanE += val
        
    print("Max Multiplicity \t%d"%MaxE)  
    print("Min Multiplicity \t%d" % MinE)
    print("Mean Multiplicity \t%f" % (MeanE/(G.GetEdges()/2)))
    if(Edge.Len()%2 == 0):
        print("Median Multiplicity \t%f" % ((Edge[Index] + Edge[Index-1])/2))
    else:
        print("Median Multiplicity \t%f" % Edge[Index-1])
         

def author(G):
    MaxN = 0
    MinN = 0
    MedianN = 0 
    MeanN = 0
    print("\nNODE STATS:\n")
    Node = snap.TIntV()
    for NI in G.Nodes():
        Node.Add(int(G.GetIntAttrDatN(NI , "paper_count")))
    Node.Sort()
    MaxN = Node[Node.Len() - 1]
    print("Maximum number of papers wrote \t%d"%MaxN)
    MinN = Node[0]
    print("Minimum number of papers wrote \t%d"%MinN)
    for val in Node:
        MeanN += val
    print("Mean Author Statistics \t%f"%(MeanN / Node.Len()))
    Index = Node.Len()//2
    if(Node.Len()%2 == 0):
        print("Meadian Author Statistics \t%f"%((Node[Index - 1]+Node[Index]/2)))
    else:
        print("Meadain Author Statistics \t%f"%(Node[Index]))

def info(G):
    snap.PrintInfo(G , "Python type PNEANet")
    print("Connected:",end="\t\t")
    print(snap.IsConnected(G))