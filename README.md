<h2>Grid.py</h2>
<p>
<tb>Grid.py contains a class(Grid) that represents an interactable Tic-Tac-Toe grid with keeps track of the turn, gamestate, and winner,
and has methods to transcribe the grid into input for the neural network.  
</p>
<h2>Agent.py</h2>
<p>
Agent.py has a class(Agent) that contains a gene, which can be randomly generated. The Gene contains weights for a neural network that takes the grid values as 
input and outputs 9 neurons representing which tile it thinks is best. 
</p>
<h2>Match.py</h2>
<p>
Match.py includes two classes: Match and Tournament. Match represents a "match".
</p> 
<p> It takes two agents and a grid and plays 3(could be changed) games of Tic-Tac-Toe 
between the agents and calculates their score(Needs little adjusting). It's output is made to work well with the other class, Tournament. </p>
<p>
Tournament takes a power-of-two agents and recursevly plays a bracket tournament after which it calculates a ranking list
</p>
<h2>To Do:</h2>
<ul>
<li>Implement reproduction (Mix, Selection, Mutation)</li>
<li>Do proper testing</li>
</ul>
