import snap
import csv
from time import time 
import __main__

import hashing
import save
import stats
import update
import database


G = snap.TNEANet.New()
G.AddIntAttrE("Multiplicity")
G.AddIntAttrE("latest_year")
G.AddIntAttrE("start_year")

G.AddIntAttrN("author_id")
G.AddIntAttrN("start_year")
G.AddIntAttrN("latest_year")
G.AddIntAttrN("paper_count")

Edges = snap.TStrH()

def total_time(start, end):
    total = end - start
    hours = total // 3600
    total -= hours * 3600
    mins = total // 60
    total -= mins * 60
    total = total // 1
    print("Total time taken:")
    print("Hour:\t\t\t%d" %hours)
    print("Minutes:\t\t%d" %mins)
    print("Seconds:\t\t%d" %total)

def display_inf():
    stats.author(G)
    stats.multiplicity(G, Edges)
    stats.info(G)
    #hashing.display(Edges) 

def save_inf():
    save.draw(G)
    save.graph(G)

def main():
    with open("../Data/CoAuthors.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        count = 0
        for row in reader:
            count += 1
            if count == 50:
                break
            src = int(float(row[0]))
            year = 0
            if row[2]:
                year = int(row[2][0:4].split()[0].split("-")[0])
            
            if not(G.IsNode(src)):
                update.initialize_node(G, src , year)
            else:
                update.node_deg(G, src)
                update.node_year(G, src, year)
            dst = 0 
            if row[1].isdigit():
                dst = int(row[1])
                
                if not(G.IsNode(dst)):
                    update.initialize_node(G, dst, year)
                else:
                    update.node_deg(G, dst)
                    update.node_year(G, dst, year)
                update.edge_multiplicity(G, src , dst, year)
                hashing.add(Edges, src, dst)

    display_inf()
    #save_inf()
    database.build_CoAuthor_database(G)

    database.build_authpap_database()  
    database.build_author_database() 
    database.build_paper_database()    
                
if __name__ == "__main__":
    start_time = time()
    main()
    end_time = time()
    total_time(start_time, end_time)
    

