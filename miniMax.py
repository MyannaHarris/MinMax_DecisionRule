# AI
# 
# Myanna Harris, Jasmine Jans, and Carol Joplin (mharris5@gonzaga.zagmail.edu submitter)
# 4-19-17
#
# mini-max with best-first search and alpha-beta pruning
#
# To run: python miniMax.py
#
# To change graph:
#   Change the nodes in the graph in main and set the
#       connecting nodes in the list of associated values
#   Change the heuristic below in the global variable "heuristic"
#       Set the list of leaf values for each leaf
#
# Note: This code is designed for values to only be attached to
#           leaf nodes.

# Heuristic values on leaves
'''heuristic = { 'D' : [2, 3],
              'E' : [5, 100],
              'F' : [0, 42],
              'X' : [2, 1],
              'Z' : [9, 11]}'''

heuristic = {'P' : [2, 3],
             'B' : [5, 100],
             'R' : [0],
             'T' : [2, 1],
             'V' : [9, 11]}

# Alpha-beta pruning
# player =  True max
#           False min
def alpha_beta(G, node, a, b, player):
    if G[node] == []:
        # Return value
        if node in heuristic.keys():
            if player:
                return max(heuristic[node])
            else:
                return min(heuristic[node])
        else:
            return 0

    if player:
        # max
        v = -float("inf")
        for child in G[node]:
            v = max(v, alpha_beta(G, child, a, b, False))
            a = max(a, v)
            if b <= a:
                break
        return v
    else:
        # min
        v = float("inf")
        for child in G[node]:
            v = min(v, alpha_beta(G, child, a, b, True))
            b = min(b, v)
            if b <= a:
                break
        return v

# mini max with best first search
def mini_max(G, start):
    visited = []
    pQueue = [start]
    pQueueV = [0]
    player = False
    
    while pQueue: #returns true if list has items, false otherwise
        vertex = pQueue.pop(0) #remove the most recently added item
        pQueueV.pop(0)

        # For stopping at best path
        '''if len(G[vertex]) < 1:
            visited.append(vertex)
            return visited'''
        
        if vertex not in visited:
            visited.append(vertex)
            children = G[vertex]
            
            vals = []
            for child in children:
                vals.append(
                    alpha_beta(G, child, -float("inf"), float("inf"), player))


            tempQ = []
            tempQVals = []
            for i in range(0, len(vals)):
                currV = vals[i]

                if ((len(tempQVals) == 0) or ((len(tempQVals) > 0) and
                    ((not player and currV <= tempQVals[0]) or
                     (player and currV >= tempQVals[0])))):
                    if len(tempQ) < 1:
                        tempQ.append(children[i])
                        tempQVals.append(currV)
                    else:
                        # Order temp list based on min or max
                        if not player:
                            for x in range(0, len(tempQ)):
                                if currV > tempQVals[x]:
                                    tempQ.insert(x, children[i])
                                    tempQVals.insert(x, currV)
                                    break
                                elif x == len(tempQ) - 1:
                                    tempQ.append(children[i])
                                    tempQVals.append(currV)
                        else:
                            for x in range(0, len(tempQ)):
                                if currV < tempQVals[x]:
                                    tempQ.insert(x, children[i])
                                    tempQVals.insert(x, currV)
                                    break
                                elif x == len(tempQ) - 1:
                                    tempQ.append(children[i])
                                    tempQVals.append(currV)


            # Add ordered nodes to priority queue                                          
            pQueue = tempQ + pQueue
            pQueueV = tempQVals + pQueueV
            player = not player

    return visited

def main():
    # Make graph
    '''graph = {'A' : ['B', 'C', 'Q'],
        'B' : ['F'],
        'C' : ['D','E'],
        'D' : [],
        'E' : [],
        'F' : [],
        'Q' : ['R'],
        'R' : ['X','Z'],
        'X' : [],
        'Z' : []}
    visited = mini_max(graph, 'A')'''

    graph = { 'C' : ['A', 'D', 'E'],
              'A' : ['P', 'B'],
              'P' : [],
              'B' : [],
              'D' : ['R'],
              'R' : [],
              'E' : ['T', 'V'],
              'T' : [],
              'V' : []}
    visited = mini_max(graph, 'C')
    
    print ("Visited: ")
    print (visited)

if __name__ == '__main__':
    main()
