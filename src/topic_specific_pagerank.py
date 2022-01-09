import numpy as np


# Calculate page ranks
def topic_specific_pagerank(M, beta, S, e):

    # Transpose the M matrix
    M = M.transpose()

    # r_0 = 1 / n for each vertex
    r0 = np.array(len(M) * [[1 / len(M)]])

    # Print iteration 0 for r_0
    print_ranks("iteration 0", r0)

    # Convert teleport set S to
    # vector s that has 1 for the
    # components in S
    s = [[0] for _ in range(len(M))]
    for i in S:
        s[i - 1] = [1]
    s = np.array(s)

    teleport = round((1 - beta) / len(S), 2)  # 1-beta/|S|

    # A = beta*M + (1-beta)/|S|     if i is in S
    # A = beta*M + 0                otherwise
    A = np.multiply(M, beta)                  # beta*M
    A = A + np.multiply(s, teleport)          # beta*M + (1-beta)/|S|

    # Initialize difference
    diff = 1

    # Start iterations
    iteration = 1

    # Iteration 1
    # r_1 = A*r_0
    r_old = r0
    r_new = A.dot(r_old)

    # while the difference between r_new and
    # r_old is above threshold
    while diff > e:

        # r_new = A*r_old
        r_new = A.dot(r_old)

        # Print ranks in each iteration
        print_ranks("iteration " + str(iteration),
                    r_new)

        # Calculate difference between r_new and r_old
        # and check with threshold
        diff = difference(r_new, r_old)

        # If the difference is above threshold
        if diff > e:

            # r_old is the previous r that
            # will be used to calculate next rNew
            # then Current r_new will be the r_old
            r_old = r_new

        # Next iteration
        iteration = iteration + 1

    return r_new


# Print page ranks
def print_ranks(current_iteration, x):

    # Print current iteration
    print(current_iteration + ":")

    # print rank for each vertex
    # in current iteration
    vertex = 1
    for row in x:
        print(vertex, end=': ')
        print(' '.join(map(lambda x: "{:.3f}".format(x), row)))
        vertex += 1
    print()


# Calculate difference
# between r_new and r_old
def difference(r_new, r_old):

    # for each row in r_new and r_old
    # calculate difference and add them
    # to the sum
    sum = 0.0
    for i in range(len(r_new)):
        d = abs(r_new[i] - r_old[i])
        sum += d

    # sum = |r_new - r_old|
    return sum
