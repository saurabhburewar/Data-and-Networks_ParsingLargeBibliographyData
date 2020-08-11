import hashing

def initialize_node(G, node , year):
    G.AddNode(node)
    G.AddIntAttrDatN(node, int(node) , "author_id")
    G.AddIntAttrDatN(node, int(year) , "start_year")
    G.AddIntAttrDatN(node, int(year) , "latest_year")
    G.AddIntAttrDatN(G.GetNI(node), 1, "paper_count")

def node_deg(G, node):
    deg = int(G.GetIntAttrDatN(G.GetNI(node), "paper_count"))
    G.AddIntAttrDatN(G.GetNI(node), deg+1 , "paper_count")

def node_year(G, node, year):
    id = G.GetNI(node)
    year2 = int(G.GetIntAttrDatN(id, "latest_year"))
    if(year2 >= year):
        return
    G.DelAttrDatN(id , "latest_year")
    G.AddIntAttrDatN(id , year , "latest_year")

def edge_multiplicity(G, src, dst, year):
    if not(G.IsEdge(src, dst)):
        G.AddEdge(src, dst)
        G.AddEdge(dst, src)
        id_src_dst = G.GetEI(src, dst)
        id_dst_src = G.GetEI(dst, src)
        G.AddIntAttrDatE(id_src_dst, 1 , "Multiplicity")
        G.AddIntAttrDatE(id_dst_src, 1 , "Multiplicity")
        G.AddIntAttrDatE(id_src_dst, year , "start_year")
        G.AddIntAttrDatE(id_dst_src, year , "latest_year")
    else:
        id_src_dst = G.GetEI(src, dst)
        id_dst_src = G.GetEI(dst, src)
        multiplicity = int(G.GetIntAttrDatE(id_src_dst, "Multiplicity")) + 1
        G.AddIntAttrDatE(id_src_dst, multiplicity , "Multiplicity")
        multiplicity = int(G.GetIntAttrDatE(id_dst_src, "Multiplicity")) + 1
        G.AddIntAttrDatE(id_dst_src, multiplicity , "Multiplicity")
        year2 = int(G.GetIntAttrDatE(id_src_dst, "latest_year"))
        if(year2 >= year):
            return
        G.AddIntAttrDatE(id_dst_src, year, "latest_year")
        G.AddIntAttrDatE(id_src_dst, year, "latest_year")



