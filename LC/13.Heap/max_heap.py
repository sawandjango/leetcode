## Create a max heap 
## A = [3,9,2,1,4,5]
'''
                      9  
                  /      \
                 /        \
                 5          4
                /  \       /
               /    \      1
              3      2
                           

'''             
# 1. Insert node at the last available place 
# 2. hepify 
# 3. You need to left node and right node
#    arr[k]
#    parent node = arr[(k-1)/2]
#    Left child = arr[(2*k)+1]
#    Right chhild = arr[(2*k)+2]
#    
class heapMax:
    def max_heapify(self,A, i):
        ## check which one is greater element
        l = self.left(i)
        r = self.right(i)
        # first get largest index of non-leaf node subtree
        # Then try to compare left node with parent and then right with parent
        if l < len(A) and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r < len(A) and A[r] > A[largest]:
            largest = r
        # Now you already decided the largest element
        # Swap now
        if largest !=i:
            print(A[i] , A[largest], "=", A[largest], A[i])                       
            A[i] , A[largest] = A[largest], A[i]      # swap       #    5=i            7          
            self.max_heapify(A, largest)                           #  /   \    --->   / \
                                                                   #  2=l  7=r       2   5
    def left(self,i): # left of k
        return 2*i + 1
    def right(self,i): # right of k
        return 2*i + 2
    def build_max_heap(self,A):
        # n/2 to n traverse last nodes# where n=total nodes 
        n = int((len(A)//2) -1)
        for i in range(n,-1,-1):
            self.max_heapify(A, i)

A = [11,6,5,0,8,2,7]
hm = heapMax()
hm.build_max_heap(A)
print(A)

'''
 Time compexity:
 Height of the tree = logn
 every time two comparasions = 2
  so time compexity is = 2logn => O(logn)
 Space compexity:
    Storing the data at each level of tree so logn
    O(logn)
''' 