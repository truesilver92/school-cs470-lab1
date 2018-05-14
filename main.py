
import numpy as np
import random

def agent_pp(quality):
    # add variance of 10%
    variance = random.uniform(1, 0.8)
    quality = quality * variance
    remaining = (1 - quality) / 2
    return (quality, remaining * variance, remaining * (1 / variance))

def problem1():
    quality = 0.8
    state1 = True
    state2 = False
    state3 = False
    agents = []
    agent_choices = []
    for i in range(20):
        a = agent_pp(quality)
        agents.append(a)
        m = max(a)
        if m == a[0]:
            agent_choices.append(1)
        elif m == a[1]:
            agent_choices.append(2)
        else:
            agent_choices.append(3)
    return agent_choices
        
