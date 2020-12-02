import random
from typing import List
"""
Let's explore how both (agent and environment) can be implemented in Python 
for a simple situation. We will define an environment that will give the agent 
random rewards for a limited number of steps, regardless of the agent's actions. 
This scenario is not very useful, but it will allow us to focus on specific 
methods in both the environment and agent classes. Let's start with the environment:
"""

class Environment:
    
    """
    In the preceding code, we allowed the environment to initialize its internal 
    state. In our case, the state is just a counter that limits the number of 
    time steps that the agent is allowed to take to interact with the environment
    """

    def __init__(self):
        self.steps_left = 10

    def get_observation(self) -> List[float]:
        
        """
        This method is supposed to return the current environment's observation to the 
        agent. It is usually implemented as some function of the internal state of 
        the environment. The observation vector is always zero, as the environment 
        basically has no internal state.
        """
        return [0.0, 0.0, 0.0]

    def get_actions(self) -> List[int]:
        """
        method allows the agent to query the set of actions it can execute. Normally, 
        the set of actions that the agent can execute does not change over time, but 
        some actions can become impossible in different states (for example, not every 
        move is possible in any position of the tic-tac-toe game). In our simplistic 
        example, there are only two actions that the agent can carry out, which are 
        encoded with the integers 0 and 1
        """

        return [0, 1]

    def is_done(self) -> bool:
        """
        The preceding method signaled the end of the episode to the agent. Episodes can 
        be finite, like in a game of chess, or infinite, like the Voyager 2 mission (a 
        famous space probe that was launched over 40 years ago and has traveled beyond 
        our solar system). To cover both scenarios, the environment provides us with a 
        way to detect when an episode is over and there is no way to communicate with it 
        anymore.
        """
        return self.steps_left == 0

    def action(self, action: int) -> float:
        """
        The action() method is the central piece in the environment's functionality. It 
        does two things – handles an agent's action and returns the reward for this action. 
        In our example, the reward is random and its action is discarded
        """
        if self.is_done():
            raise Exception("Game is over")
        self.steps_left -= 1
        return random.random()

class Agent:
    """
    At the agent's part, it is much simpler and includes only two methods: the constructor 
    and the method that performs one step in the environment
    """
    def __init__(self):
        """
        In the constructor, we initialize the counter that will keep the total reward 
        accumulated by the agent during the episode
        """
        self.total_reward = 0.0

    def step(self, env: Environment):
        """
        The step function accepts the environment instance as an argument and allows the 
        agent to perform the following actions:
        *  Observe the environment				
        *  Make a decision about the action to take based on the observations				
        *  Submit the action to the environment				
        *  Get the reward for the current step
        """        
        current_obs = env.get_observation()
        print (f"The current observation is: {current_obs}")        
        actions = env.get_actions()        
        print (f"The current action is: {actions}")
        reward = env.action(random.choice(actions))        
        self.total_reward += reward

"""
For our example, the agent is dull and ignores the observations obtained during the decision-making 
process about which action to take. Instead, every action is selected randomly. The final piece is 
the glue code, which creates both classes and runs one episode:
"""

if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)
    
    print("Total reward got: %.4f" % agent.total_reward)

"""
NOTE: The simplicity of the preceding code illustrates the important basic concepts that come 
from the RL model. The environment could be an extremely complicated physics model, and an agent 
could easily be a large neural network (NN) that implements the latest RL algorithm, but the basic 
pattern will stay the same – on every step, the agent will take some observations from the environment, 
do its calculations, and select the action to take. The result of this action will be a reward 
and a new observation.
"""