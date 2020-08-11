def add(Edges, Source, Destination):
    key = str(Source) + "-" + str(Destination)
    key2 = str(Destination) + "-" + str(Destination)
    if(Edges.IsKey(key)):
        Edges[key] += 1
    elif(Edges.IsKey(key2)):
        Edges[key2] += 1
    else:
        Edges.AddKey(key)
        Edges[key] = 1

def display(Edges):
    max = 0
    min = 99999999999999
    it = Edges.BegI()
    while not it.IsEnd():
        if(it.GetDat() > max):
            max = it.GetDat()
        if(it.GetDat() < min):
            min = it.GetDat()
        it.Next()
    print(max)
    print(min)