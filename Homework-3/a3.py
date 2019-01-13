# ANSHUMAN SINGH
# 2017025
# Section A Group 2

from math import inf as infinity
# Input procedure
def inputpro():
	C = [];W=[]
	t = int(input())
	for i in range(0,t):
		n = int(input())
		L1 = []
		L2 = []
		for j in range(0,n):
			
			x,y = map(int, input().split())
			L1.append(int(x))
			L2.append(int(y))
			
		C.append(L1)
		W.append(L2)
	return(C,W)


# Function to return the value of the index with the minimum distance	
def minindex(dist, mark):
    min = infinity
    for i in range(len(dist)):
        if(dist[i] < min and mark[i] == False):
            min = dist[i]
            temp = i
            return temp
 
# Function to carry out the Djikstra's Algorithm      
def Djikstra(C,W,source):
	dist = []; Q = []; global mark; mark=[]  # Initializing all the lists that have to be used
	# Initializing the lists Q and dist
	for i in range(0,len(C)):
		dist.append(infinity)
		Q.append(i)
	dist[source] = 0
	# Initializing the list mark
	for i in range(0,len(dist)):
		mark.append(False)
	# Main function loop 
	while(len(Q)>0):
		# Finding the index with the minimum distance from the source
		v = minindex(dist,mark)
		if(v==None):
			break     # So that loop breaks if no connection found
		Q.remove(v)
		#Updating the mark list for the next iteration
		mark[v]=True
		# Loop to update the distance list
		for i in range(0,len(C[v])):
			u = C[v][i] # To choose the required index in the Connections list
			if(u in Q and mark[u]==False and W[v][i]!=[]): #Condition for the update of the dist list
				temp = dist[v] + W[v][i]
				if(temp < dist[u]): # Condition for the update of the minimum value
					dist[u] = temp
	return(dist) # Returning the value of the distance list as the output
	#print(dist)


# Function to carry out the BFS Algorithm
def bfs(C,W,source):
	mark=[];ans = [];dist=[] 
	#Initializing the lists that will be used
	for i in range(0,len(C)):
		mark.append(False)
		dist.append(infinity)

	Q = []
	# Storing the value of source in the Queue and updating values of the corresponding lists
	Q.append(source)
	mark[source] = True
	dist[source] = 0
	# Main function loop
	while(len(Q)!=0):
		# Removing the first element in the queue and appending it to a list that stores the nodes that have been visited
		s = Q[0]
		ans.append(s)
		Q.remove(s)
		#print(ans)
		# Loop to update the value of the Queue and the distance list
		for i in range(0,len(C[s])):
			u = C[s][i]
			if(mark[u]==False):
				Q.append(u)
				mark[u]=True
				if(dist[u]==infinity):
					dist[u]=dist[s]+W[s][i]
	return(dist)

if __name__=='__main__':
	x,y = inputpro()
	#C = [[1,2],[3],[1,3,4],[],[3]];W = [[2,1],[1],[2,1,1],[],[1]]
	
	x = bfs(C,W,0)

	print(x)
