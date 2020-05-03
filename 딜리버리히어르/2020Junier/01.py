from typing import List, Text

class NoAgentFoundException(Exception):
    pass


class Agent(object):
    instances = []
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load
        self.instances.append(self)
    def __str__(self):
        return "<Agent: {}>".format(self.name)

    def get_least_loaded(self):
        return min(self.instances, key=lambda x : x.load)

class Ticket(object):
    def __init__(self, id, restrictions):
        self.id = id
        self.restriction = restrictions

#
class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        return list(filter(lambda x : x.load > 0, List[Agent]))

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        print('finder policy')
        print(Agent.instances)
        return Agent.instances




#
class LeastLoadedAgent(FinderPolicy):
    print('Leastloaded')
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        Agents = FinderPolicy.find(self, ticket=ticket, agents=agents)
        print('Leat Loaded Agents : ', Agents)
        least_loaded_agent = min(Agents, key=lambda x: x.load)
        print(type(least_loaded_agent))
        return least_loaded_agent.name
# #
#
#
class LeastFlexibleAgent(FinderPolicy):
    print('leastFlexible')
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        Agents = FinderPolicy.find(self, ticket=ticket, agents=agents)
        print('least Flexible agents : ' ,Agents)
        print(min(Agents, key=lambda x : len(x.skills)))


ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)
agent3 = Agent(name="C", skills=["English", "Japanese"], load=-1)

# print(Agent.get_least_loaded(agent2))

least_loaded_policy = LeastLoadedAgent()
# returns the Agent with name "B" because of their currently lower load.
print(least_loaded_policy.find(ticket, [agent1, agent2]))

least_flexible_policy = LeastFlexibleAgent()
# returns the Agent with name "A" because of their lower flexibility.
least_flexible_policy.find(ticket, [agent1, agent2])
print(2 ** 20)
print(sorted([6,5,8]))