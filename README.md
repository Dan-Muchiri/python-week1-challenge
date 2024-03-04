# Code Challenge Solutions

## Python Challenge 1: Bricks in Boxes
Given an array representing the number of bricks in each box, the task is to find the minimum number of moves required to have exactly 10 bricks in each box. Each move involves transferring one brick from one box to its adjacent box.

### Approach:
- Calculate the target number of bricks per box.
- Iterate through each box and redistribute the bricks to make the number of bricks in each box equal to the target.
- Count the number of moves required to achieve the target configuration.

## Python Challenge 2: Maximum Sum of Numbers with Equal Digit Sums
Given an array of numbers, the task is to find the maximum sum of two numbers whose digits add up to the same sum.

### Approach:
- Define a function to calculate the sum of digits of a number.
- Iterate through all pairs of numbers in the array.
- Check if the sum of digits of both numbers is equal and find the maximum sum among them.

## Python Challenge 3: Equal Occurrences of Lowercase Letters
Given an integer N, the task is to construct a string of length N containing as many different lowercase letters ('a' to 'z') as possible, with each letter occurring an equal number of times.

### Approach:
- If N is less than or equal to 26, use all the lowercase letters once until N.
- If N is greater than 26, repeat the sequence of lowercase letters enough times to cover N. If there's a remainder after the repetition, append the required number of letters to the result string.

Each solution provides the required functionality and has been tested with provided test cases.
