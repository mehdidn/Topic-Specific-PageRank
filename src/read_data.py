def read_data(path):

    # Read from file path
    with open(path) as f:

        # Read lines
        lines = f.readlines()

    # Getting number of vertices from data
    # split first line
    parts = lines[0].split()

    # Integer number of number_of_vertices is
    # the last part from parts
    number_of_vertices = int(parts[len(parts) - 1])

    # Getting number of edges from data
    # split second line
    parts = lines[1].split()

    # Integer number of number_of_Edges is
    # the last part from parts
    number_of_Edges = int(parts[len(parts) - 1])

    # Declare adjacency matrix
    adj = [[] for _ in range(number_of_vertices)]

    # edges starting line in data file
    start_line_of_edges = 4

    # for each line in data
    for i in range(number_of_Edges):

        # Current line
        line = lines[i + start_line_of_edges]

        # split Current line
        parts = line.split()

        # each line is in format u v and
        # means u has an edge to v so u->v
        # in each line: u=line[0] and v=line[2]
        # add v to adj[u]
        adj[int(parts[0]) - 1].append(int(parts[1]) - 1)

    # Getting beta from data
    # split one line before the last line
    parts = lines[len(lines) - 2].split()

    # floating number of beta is the
    # last part from parts
    beta = float(parts[len(parts) - 1])

    # Getting teleport set from data
    # replace redundant characters with space
    # and split last line
    parts = lines[len(lines) - 1].replace(",", " ").replace("{", " ").replace("}", " ").split()

    # Ignore two first indices
    # first index is 'S'
    # second index is '='
    start = 2

    # Setting teleport set
    S = []
    for i in range(start, len(parts)):
        S.append(int(parts[i]))

    # Return values
    return number_of_vertices, number_of_Edges, adj, beta, S
