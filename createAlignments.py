from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.objects.petri import importer
import time
from pm4py.algo.conformance.alignments import versions
import pm4py.algo.conformance.alignments.algorithm as alignments
from pm4py.statistics.variants.log import get as get_variants
import sys

'''
Author : Boltenhagen Mathilde
Date : June 2020

createAlignments.py : compute alignment costs with pm4py 
'''

# read parameter : python3 createAlignments.py output_file xes_file pnml_file
argv=sys.argv
filename=argv[1]
net, m0, mf = importer.importer.apply(argv[3])
log = xes_importer.apply(argv[2])

# compute alignment for variants only
variants = get_variants.get_variants(log)


start=time.time()
for l in variants:
    ali=alignments.apply(variants[l][0],net, m0,mf,variant=versions.dijkstra_no_heuristics)
    # export in a CSV file with : trace, trace with moves, run, run with moves, cost, frequency
    if ali:
        writer=open(filename,"a")
        alignment=ali["alignment"]
        cost=ali["cost"]
        phrase1=""
        phrase1None=""
        phrase2=""
        phrase2None=""
        for (a,b) in alignment:
            if a!=">>":
                # activities are separated with :::
                phrase1+=a+":::"
            phrase1None+=a+":::"
            if b!=">>" and b!=None:
                phrase2+=b+":::"
            phrase2None+=str(b)+":::"
        writer.write(phrase1+";"+phrase1None+";"+phrase2+";"+phrase2None+";"+str(cost)+";"+str(len(variants[l]))+"\n")
        writer.close()

writer=open(filename,"a")
writer.write(str(start-time.time()))
writer.close()