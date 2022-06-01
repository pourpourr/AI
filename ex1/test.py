# Collect legal moves and successor states
legalMoves = gameState.getLegalActions()

# Choose one of the best actions
scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
bestScore = max(scores)
bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
chosenIndex = random.choice(bestIndices) # Pick randomly among the best
# Useful information you can extract from a GameState (pacman.py)
successorGameState = currentGameState.generatePacmanSuccessor(action)
#    print(successorGameState)

newPos = successorGameState.getPacmanPosition()
newFood = successorGameState.getFood().asList()
newGhostStates = successorGameState.getGhostStates()
newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
temp=0;
for i in newFood:
    temp+=1/(manhattanDistance(i,newPos))
