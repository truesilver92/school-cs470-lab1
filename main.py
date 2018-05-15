
import numpy as np
import random
import math

def agent_pp(quality):
    # add variance of 10%
    variance1 = random.uniform(1.2, 0.8)
    variance2 = random.uniform(1.2, 0.8)
    variance3 = random.uniform(1.2, 0.8)
#    quality = quality * variance
    remaining = (1 - quality) / 2
    return (quality * variance1, remaining * variance2, remaining * variance3)

def agent_pp2(quality):
    remaining = (1 - quality) /2
    return (quality, remaining, remaining)

def agent_pp3(quality, min_utility):
    remaining = (1 - quality) /2
    return (quality, remaining, remaining, min_utility) # the foruth is else

def problem1():
    quality = 0.1
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
    return (agents,agent_choices)

def problem2():
    state1 = True
    state2 = False
    state3 = False
    NUM_AGENTS = 20
    percent_good = 0.20
    likelihood = 0.9
    quality = 0.1
    agents = []
    first_agent_info = math.floor(NUM_AGENTS * percent_good)
    for i in range(first_agent_info):
        agents.append(agent_pp2(quality))
    for i in range(first_agent_info, NUM_AGENTS):
        agents.append(agent_pp2(random.uniform(0.0, 1)))
    # block
    decisions = []
    for i in range(NUM_AGENTS):
        for decision in decisions:
            agents[i] = Bayes(agents[i], decision, likelihood)
        decisions.append(agents[i].index(max(agents[i])) + 1)
    return decisions
            
def Bayes(priors, observation, likelihood):
    normalizer = 0.0
    numerators = []
    for i in range(len(priors)):
        real_likelihood = 0.0
        if observation == i:
            real_likelihood = likelhood
        else:
            real_likelihood = (1 - likelihood)/2

        numerator = priors[i] * real_likelihood
        normalizer += numerator
        numerators.append(numerator)
        return list(map(lambda x : x / normalizer, numerators))

def Bayes3(priors, observation, likelihood, minimum_utility):
    normalizer = 0.0
    real_likelihood = 0.0
    numerators = []
    if observation == -1:
        return priors
    for i in range(3):
        if observation == i:
            real_likelihood = likelihood
        else:
            real_likelihood = (1 - likelihood)/2
        numerator = priors[i] * real_likelihood
        normalizer = numerator + normalizer
        numerators.append(numerator)
    partial = list(map(lambda x : x / normalizer, numerators))
    partial.append(priors[3])
    return partial

def problem3():
    state1 = True
    state2 = False
    state3 = False
    NUM_AGENTS = 20
    percent_good = 0.20
    likelihood = 0.8
    quality = 0.8
    minimum_utility = 0.1
    agents = []
    first_agent_info = math.floor(NUM_AGENTS * percent_good)
    for i in range(first_agent_info):
        agents.append(agent_pp3(quality, minimum_utility))
    for i in range(first_agent_info, NUM_AGENTS):
        agents.append(agent_pp3(random.uniform(0.0, 1), minimum_utility))
    # block
    decisions = []
    for i in range(NUM_AGENTS):
        for decision in decisions:
            agents[i] = Bayes3(agents[i], decision, likelihood, minimum_utility)
        #decisions.append(agents[i].index(max(agents[i])) + 1)
        #print(len(agents[i]))
        #print(agents)
        best = max(agents[i][:3])
        if best < minimum_utility:
            decisions.append(-1)
        else:
            decisions.append(agents[i].index(max(agents[i])) + 1)
    return decisions
            
a = problem3()
print(a)
