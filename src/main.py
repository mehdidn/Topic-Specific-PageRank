import numpy as np
from topic_specific_pagerank import topic_specific_pagerank
from topic_specific_pagerank import print_ranks

# Main function
if __name__ == '__main__':

    # Read data
    with open('../Data/data1.txt') as f:

        # Read lines
        lines = f.readlines()

    # First line of data is
    # the number of vertices
    n = int(lines[0])

    # Declare adjacency matrix
    adj = [[] for i in range(n)]

    # for each line in data
    for line in lines:

        # each line is in format u v
        # then u=line[0] and v=line[2]
        try:
            adj[int(line[0]) - 1].append(int(line[2]) - 1)
        except:
            pass

    # Declare M matrix
    M = [[0] * n for i in range(n)]

    # For each vertex
    # calculate each row of M
    for u in range(n):

        # Number of adjacent vertices of u
        number_of_adjacent = 0

        # For each vertex v in adjacency list of u
        for v in adj[u]:

            # Increase number of adjacent vertices of u by one
            number_of_adjacent += 1

        # For each vertex v in adjacency list of u
        for v in adj[u]:

            # M_uv = 1 / number of adjacent vertices of u
            M[u][v] = 1 / number_of_adjacent

    # Create np array
    M = np.array(M)

    # Beta
    beta = 0.8

    # Teleport set
    S = [1]

    # Stop threshold
    e = 0.0001

    # Calculate page ranks
    # and print for each iteration
    final_pr = topic_specific_pagerank(M, beta, S, e)

    # Print final page ranks
    print_ranks("Final PR", final_pr)
