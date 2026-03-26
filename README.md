# My High School Graduation Project: Concept for a Tournament-based Neuroevolution algorithm via Tic-Tac-Toe

This is my High School Graduation project (мк: Проектна за матура). I was mentored by Martin Dinev, who was my professor for the subjct "Intelegent Systems" at my high shool.

I made this project because I wanted to explore if you can train AI agents by making them play against each-other, instead of a classical fitness function, which would be usefull for games that aren't solved (an optimal solution isn't known). Natrually, the easiest option was a two player game that plays mostly simetrically and Tic-Tac-Toe came to mind. Additionally it is short and simple so it's good for testing the concept.

The project includes implementation in Python as well as a few Experiments to determine if it works, and what parameters produce the best results.

## Algorithn outline
### The "Evolution" aspect
The algorithm roughly works like this:
1. A generation of agents is initialised
2. The agents are sorted where '<' means A got fewer points than B. Points are gained by winning, and lost by losing and attempting illegal moves. The sorting was done in two seperate ways:
  -The default, correct sorting algoirithm in python
  -An "aproximation" soring algorithm, which resembles a bracket that isn't complete. This was done to introduce some fuzzyness into the selection process.
3. The top agents are seleted, crossovered and mutated, and placed in the next generation, as well as some newly generated ones.
4. Repeat untill happy

### The "Neuro" aspect
Each agent is a neural network with two secret layers. The input layer are 9 neurons all representing if their cell is empty, has their symbol, or has the opponent's symbol. The output layer represents how "sure" it is that cell should be slected. The highest ranked legal move is chosen (the agent is penalised if it attempts an illegal move).

### The "Neuroevolution" aspect
The weights of the neural network are represented in the genome. Their value is the thing that gets mutated, crossovered, and so on.

