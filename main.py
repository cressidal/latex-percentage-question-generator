#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 18:24:33 2021

@author: cressidal
"""

import random as rd

# percentage of quantity questions
def pcOfQuant():
    item = "\item {"
    of = "\% of "
    endItem = "?}\n"
    endAns = "}\n"
    question = ""
    answer = ""
    
    for i in range(0,10):
        a = rd.randint(1, 200)
        b = rd.randint(1, 200)
        question = question + item + str(a) + of + str(b) + endItem
        answer = answer + item + str(a*b/100)+endAns
        
    print(question)
    print(answer)
    return(question,answer)

# increase or decrease of quantity by a percentage
def incOrDecOfQuant():
    item = "\item {"
    endItem = "\%?}\n"
    endAns = "}\n"
    question = ""
    answer = ""
    
    seq = [" increased by "," decreased by "]
    
    i=0
    
    while i < 11:
        a = rd.randint(1, 200)
        b = rd.randint(1, 200)
        
        if i%2 == 0:
            ans = a*((100 + b)/100)
        else:
            ans = a*((100 - b)/100)
        
        if len(str(ans).rsplit('.')[-1]) < 3:
            if i%2 == 0:
                if ans%1 == 0:
                    ans = int(ans)
                answer = answer + item + str(ans) + endAns
                question = question + item + str(a) + seq[0] + str(b) + endItem
                i += 1
            else:
                if ans%1 == 0:
                    ans = int(ans)
                answer = answer + item + str(ans) + endAns
                question = question + item + str(a) + seq[1] + str(b) + endItem
                i += 1
        
    print(question)
    print(answer)
    return(question,answer)

# what percentage of this quantity is another quantity
def wotPc():
    item = "\item {"
    endItem = "?}\n"
    endAns = "\%}\n"
    question = ""
    answer = ""
    
    i = 0
    
    while i < 10:
        a = rd.randint(1, 500)
        b = rd.randint(1, 200)
        
        ans = b/a * 100
        if len(str(ans).rsplit('.')[-1]) < 3:
            if ans%1 == 0:
                ans = int(ans)
            answer = answer + item + str(ans) + endAns
            question = question + item + str(a) + " is " + str(b) + endItem
            i += 1
        
    print(question)
    print(answer)
    return(question,answer)

a = pcOfQuant()
b = incOrDecOfQuant()
c = wotPc()

def wrapInQuestion():
  #TODO 
  # writes questions into proper latex
  
  return latexCode
  
# writes questions into a latex file
def writeToFile(latexCode):
  f = open("percentages.tex", "w")
  f.write(latexCode)
  f.close()

