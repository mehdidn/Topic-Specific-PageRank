import numpy as np
from topic_specific_pagerank import topic_specific_pagerank
from topic_specific_pagerank import print_ranks
from read_data import read_data

# Main function
if __name__ == '__main__':

    # Read data and store values
    number_of_vertices, number_of_Edges, adj, beta, S = read_data('../Data/data6.txt')

    # Stop threshold
    e = 0.0001

    # Declare M matrix
    M = [[0] * number_of_vertices for i in range(number_of_vertices)]

    # For each vertex
    # calculate each row of M
    for u in range(number_of_vertices):

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

    # Calculate page ranks
    # and print for each iteration
    final_pr = topic_specific_pagerank(M, beta, S, e)

    # Print final page ranks
    print_ranks("Final PR", final_pr)
