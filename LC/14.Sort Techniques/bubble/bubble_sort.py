#https://www.udemy.com/course/datastructurescncpp/learn/lecture/13190984#overview
#A 8 5 7 3 2
# Make it vertically 
'''
8 | Compare 5           5            5           5
5 |         8 | Compare 7            7           7 4
7           7 |         8 | Compare  3           3  
3           3           3 |          8 | Compare 2 
2           2           2            2 |         8   
'''
# 8 is sorted in first pass 
#Same way for other passes 
#1 pass = Compare 4 and Swap = 4
#2 pass => Compare 3 and Swap = 3
#3 pass => Compare 2 and swap = 2
#4 pass => Compare 1 and swa = 1 

# for n elements total passes required => (n -1) =(5-1) = 4
# Total comparisions = 1 +2 +3 + 4 > 1+2+3+4 ---- n = n * (n -1)/2 > O(n2)
# Total sawaps = 1 +2 +3 + 4 > 1+2+3+4 ---- n = n * (n -1)/2 > O(n2)




