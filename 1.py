#!/usr/bin/env python

import random
import math

def _make_heap(team_list):
    steps = int(math.log2(len(team_list)))+1
    k=2**steps
    heap=[0 for x in range(0,k)]
    while len(team_list)>0:
        i = random.randrange(0, len(team_list))
        k-=1
        heap[k]=team_list[i]
        del team_list[i]
    return heap


def _simulate_game(team_list):
    heap = _make_heap(team_list)
    team_dict = {}
    k=len(heap)-2
    while k>0:
        pos=int((k)/2)
        first = random.randrange(0,10)
        second = random.randrange(0,10)
        if first>second:
            heap[pos]=heap[k]
        elif first==second:
            if random.randrange(0,11)>=5:
                heap[pos]=heap[k]
            else:
                heap[pos]=heap[k+1]
        else:
                heap[pos]=heap[k+1]

        if(team_dict.get(heap[k]) == None):
            team_dict[heap[k]]=[]
        if(team_dict.get(heap[k+1]) == None):
            team_dict[heap[k+1]]=[]
        team_dict[heap[k]]+=[heap[k+1], first, second]
        team_dict[heap[k+1]]+=[heap[k], second, first]
        k-=2
    team_dict['heap'] = heap
    return team_dict

def _show_result(dict, team = None):
    _show_team_results(dict, team)


def _show_team_results(dict, team=None):
    if team != None and dict.get(team)!=None:
        i=0
        while i < len(dict[team]):
            s=""
            s=team+" : " + dict[team][i]+'\n'
            i+=1
            s+=str(dict[team][i])+ " ".join('' for x in team) +" : "+" ".join('' for x in dict[team][i-1]) +str(dict[team][i+1])
            i+=2
            print(s+ "\n")
    else:
        raise ValueError



def _show_heap(heap):
    width = 2
    steps = int(math.log2(len(heap)))+1
    i = 1
    while i < len(heap):
        s = ' '.join(['' for x in range(0, width*2**int(steps-2-int(math.log2(i))))])
        j=int(math.log2(i))
        while j==int(math.log2(i)):
            s+=heap[i]+' '.join(['' for x in range(0, width*2**int(steps-1-int(math.log2(i))))])
            i+=1
        print(s+'\n'+'\n')



def _main():
    team_list = [x for x in "ABCDEFGHIJKLMNOP"] #ijklmnop
    team_dict = _simulate_game(team_list[:])
    _show_heap(team_dict['heap'])
    while 1:
        team =input()
        try:
            _show_heap(team_dict['heap'])
            _show_result(team_dict, team)
        except ValueError:
            print("team not found")

if __name__ == "__main__":
    _main()
