import pm4py.objects.log.importer.xes.importer as xes_importer
import pm4py.objects.log.exporter.xes.exporter as xes_exporter
from pm4py.objects.log.log import Event, Trace
from pm4py.statistics.attributes.log.get import get_attribute_values
from pm4py.objects.log.util.log import project_traces
import numpy.random as random
random.seed(0)
import pm4py.statistics.variants.log.get as getvariants

'''
Author : Boltenhagen Mathilde
Date : June 2020

randomSequences.py : this file has been created to get 1000 mock traces 
'''

log = xes_importer.apply("<original log>")
variants = getvariants.get_variants(log)

# get activities and maximum length in log
activities = list(get_attribute_values(log,"concept:name").keys())
max_len = (len(max(project_traces(log),key=len)))

log._list=[]
for t in range(0,1000):
    new_sequence = Trace()
    # random length of the fake sequence
    size_of_sequence = random.randint(1,max_len-1)
    # random activities
    for e in range(0,size_of_sequence):
        event = Event()
        event["concept:name"]=activities[random.randint(1,len(activities))]
        new_sequence.append(event)
    log._list.append(new_sequence)

xes_exporter.apply(log,"<1000 mock traces>")


