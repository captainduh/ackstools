import random
import math

random.seed()

def roll(instr):
    if ',' in instr:
        [instr,prob] = instr.split(',')
        prob = float(prob)
    else: prob = 1.0
    if 'x' in instr:
        [instr,mult] = instr.split('x')
        mult = int(mult)
    else: mult = 1
    if '-' in instr:
        [instr,sub] = instr.split('-')
        sub = int(sub)
    else: sub = 0
    if 'd' in instr:
        [n,m] = instr.split('d')
        n = int(n)
        m = int(m)
    else:
        n = int(instr)
        m = 1
    total = 0
    if random.random() < prob:
        for i in range(n):
            total += random.randint(1,m)
        total -= sub
        total *= mult
    return total

def doLine(marketclass, line, numMonths):
    if len(line) < 6:
        return (line[0] + "\n")
    else:
        total = 0
        for i in range(numMonths):
            total += roll(line[marketclass])
        if total > 0:
            week1 = int(math.ceil(total/2.0))
            week2 = int(math.ceil((total-week1)/2.0))
            week3 = total - week1 - week2
            return (line[0] + ': ' + str(total) +" ("+str(week1)+"/"+str(week2)+"/"+str(week3)+")\n")

def genHirelings(inFile:str, marketClass:int, months:int):
    '''
    inFile should be ackstools/hireprices
    '''
    import os
    infile = open(inFile,"r")
    lines = infile.readlines()
    infile.close()
    lines = filter(lambda s: not s.startswith('#'), lines)
    lines = map(lambda k: k.lstrip().rstrip(), lines)
    lines = map(lambda k: k.split(":"), lines)

    hirelingMessage = "Hireling generator by jedavis. https://github.com/jedavis-rpg/ackstools\n"
    for line in lines:
        parsedLine = doLine(marketClass, line, months)
        if parsedLine is not None:
            hirelingMessage += parsedLine
    return hirelingMessage
