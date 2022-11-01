import sys 
  
# Returns cost of minimum cost path from (0,0) to (m, n) in mat[R][C] 
def minCost(cost, m, n): 
    if (n < 0 or m < 0): 
        print("inside here.....")
        return sys.maxsize 
    elif (m == 0 and n == 0): 
        return cost[m][n] 
    else: 
        return cost[m][n] + min( minCost(cost, m-1, n-1), 
                                minCost(cost, m-1, n), 
                                minCost(cost, m, n-1) ) 
  
#A utility function that returns minimum of 3 integers */ 
def min(x, y, z): 
    if (x < y): 
        if(x<z):
            return x
        else:
            return z
    else: 
        if(y<z):
            return y
        else:
            return z  
  
# Driver program to test above functions  
cost= [ [1, 2, 3], 
        [4, 8, 2], 
        [1, 5, 3] ] 
print(minCost(cost, 2, 2))