
import random

def agent_pp(quality):
    # add variance of 10%
    variance = random.uniform(1, 0.8)
    quality = quality * variance
    remaining = (1 - quality) / 2
    return (quality, remaining, remaining)

def problem1():
    quality = 0.8
    state1 = True
    state2 = False
    state3 = False
    agents = []
    for i in range(20):
        agents.append(agent_pp(quality))
    return agents
    
