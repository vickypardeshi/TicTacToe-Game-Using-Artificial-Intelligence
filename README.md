# TicTacToe-Game-Using-Artificial-Intelligence

Run Program :-
	python3 TicTacToe.py


Process for Solve Tic Tac Toe Problem :- I am used minimax algorithm to solve tic tac toe problem.


1) In the first step, the algorithm generates the entire game-tree and apply the utility function to get the utility values for the terminal states. Suppose maximizer takes first turn which has worst-case initial value =- infinity, and minimizer will take next turn which has worst-case initial value = +infinity.

2) Now, first we find the utilities value for the Maximizer, its initial value is -∞, so we will compare each value in terminal state with initial value of Maximizer and determines the higher nodes values. It will find the maximum among the all.

3)In the next step, it's a turn for minimizer, so it will compare all nodes value with +∞, and will find the 3rd layer node values.

4) Now it's a turn for Maximizer, and it will again choose the maximum of all nodes value and find the maximum value for the root node.

5)That was the complete workflow of the minimax two player game in Tic-Tac-Toe.



Time Complexity :-  O(b^m) ,   where b is branching factor of the game-tree, and m is the maximum depth of the tree.

Space Complexity :- O(bm)
