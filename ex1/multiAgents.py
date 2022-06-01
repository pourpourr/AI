# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)

        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood().asList()

        temp=0;
        for i in newFood:
            temp+=1/(manhattanDistance(i,newPos))




        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()+temp

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        actions=gameState.getLegalActions(0)
        max=  -999999999999999999
        bestAct=actions[0]
        for a in actions:
            successorGameState=gameState.generateSuccessor(0,a)
            eval= minimax(self,successorGameState, 1, self.depth)
            if eval > max :
                max= eval
                bestAct= a
        return bestAct






def minimax(self,gameState, agentIndex , depth):


    if depth==0 or gameState.isWin() or gameState.isLose() :
        return self.evaluationFunction(gameState)

    agentActions=gameState.getLegalActions(agentIndex)
    if agentIndex==0:
        maxEval= -99999999999999999
        for act in agentActions:
            successorGameState= gameState.generateSuccessor(0,act)
            eval=minimax(self,successorGameState ,  1  , depth)
            if eval > maxEval :
                maxEval=eval;




        return maxEval
    else :

        minEval=99999999999999999
        for act in agentActions :
            successorGameState= gameState.generateSuccessor(agentIndex,act)

            if (agentIndex< (successorGameState.getNumAgents()-1)) :

                eval2= minimax(self, successorGameState, agentIndex+1 , depth)
            else:
                eval2= minimax(self, successorGameState ,0 , depth-1)


            if eval2<minEval:
                minEval= eval2


        return minEval







class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        actions=gameState.getLegalActions(0)
        eval=  -9999999999999
        maxEval=-999999999999999999
        a=-99999999999999999
        b=99999999999999999
        bestAct=actions[0]
        for act in actions:
            successorGameState=gameState.generateSuccessor(0,act)
            eval= max(eval,min_value(self,successorGameState, 1 ,self.depth, a ,b))

            a=max(a,eval)
            if eval>maxEval :
                maxEval=eval
                bestAct= act
        return bestAct



def max_value(self, gameState, agentIndex,depth, a , b):
    if depth==0 or gameState.isWin() or gameState.isLose() :
        return self.evaluationFunction(gameState)
    v= -99999999999999999
    agentActions=gameState.getLegalActions(agentIndex)
    for act in agentActions:
        successorGameState= gameState.generateSuccessor(0, act)
        v= max(v,min_value(self,successorGameState, 1 ,depth, a ,b))
        a=max(a,v)

        if a>b : return v
    return v

def min_value(self, gameState, agentIndex,depth, a , b):

    if depth==0 or gameState.isWin() or gameState.isLose() :
        return self.evaluationFunction(gameState)
    v= 99999999999999999
    minEval=9999999999999999999
    agentActions=gameState.getLegalActions(agentIndex)
    for act in agentActions :
        successorGameState= gameState.generateSuccessor(agentIndex,act)
        if (agentIndex< (successorGameState.getNumAgents()-1)) :

            v=min(v,min_value(self, successorGameState, agentIndex+1 ,depth,a,b))
        else :
            v=min(v,max_value(self, successorGameState, 0 ,depth-1,a,b))

        b= min(b,v)
        if b<a:
            return v
        if v<minEval:
            minEval= v

    return v








class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        actions=gameState.getLegalActions(0)
        max=  -999999999999999999
        bestAct=actions[0]
        for a in actions:
            successorGameState=gameState.generateSuccessor(0,a)
            eval= exp(self,successorGameState, 1, self.depth)
            if eval > max :
                max= eval
                bestAct= a
        return bestAct


##############
def exp(self, gameState, agentIndex , depth):
    if depth==0 or gameState.isWin() or gameState.isLose() :
        return self.evaluationFunction(gameState)
    agentActions=gameState.getLegalActions(agentIndex)

    if agentIndex==0:
        maxEval= -99999999999999999
        for act in agentActions:
            successorGameState= gameState.generateSuccessor(0,act)
            eval=exp(self,successorGameState ,  1  , depth)
            if eval > maxEval :
                maxEval=eval;

        return maxEval


    else :

        minEval=9999999999999999999
        eval2=0
        for act in agentActions :
            successorGameState= gameState.generateSuccessor(agentIndex,act)
            if (agentIndex< (successorGameState.getNumAgents()-1)) :

                eval2= eval2 +exp(self, successorGameState, agentIndex+1 , depth)/ len(agentActions)
            else:
                eval2= eval2+ exp(self, successorGameState ,0 , depth-1)/ len(agentActions)


            if eval2<minEval:
                minEval= eval2


        return eval2


#python autograder.py -q q5 --no-graphics

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"

    if currentGameState.isWin() :
        return 9999
    elif  currentGameState.isLose():
        return -9999
    else:
        pos = currentGameState.getPacmanPosition()
        newGhostStates = currentGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
        temp=0
        temp+= newScaredTimes[0]
        badStates= currentGameState.getGhostPositions()
        for i in badStates :
            dis=manhattanDistance(pos,i)
            if (newScaredTimes[0]>0 )and dis <=2:
                temp=5*temp+3* dis
            elif dis <= 2:
                temp=0.5*temp -3*dis
            else:
                temp+=dis


        return temp/(currentGameState.getNumFood())


















# Abbreviation
better = betterEvaluationFunction
