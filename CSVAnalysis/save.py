import snap

def draw(G):
    print("going for graph")
    labels = snap.TIntStrH()
    for NI in G.Nodes():
        labels[NI.GetId()] = str(NI.GetId())
    snap.SaveGViz(G, "co_author.dot", "Directed multigraph Co_author network", True, labels)

def graph(G):
    FOut = snap.TFOut("test.graph")
    G.Save(FOut)
    FOut.Flush()

def save_pajek(Graph,filename):
    snap.SavePajek(Graph , filename)

def load_pajek(filename):
    Graph =  snap.LoadPajek(snap.PNEANet, filename)
    return Graph 

