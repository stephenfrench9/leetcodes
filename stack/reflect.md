# Stacks

### Eat back into the stack. (peaking) 
It seems like at some point, you have to eat back into the stack. With the [parens problem](https://leetcode.com/problems/valid-parentheses/), you know when that time has come because you have a closing parens, and the stack better just have the right answer for you. No peaking required. you pop no matter what. 

With the [sum of minimums problem](https://leetcode.com/problems/sum-of-subarray-minimums/), you eat back into the stack to find the first time there is a smaller number. Sort of like you would do naively with a while loop. But with the stack, it means that for later elements, you don't have to redo the comparisons. 




