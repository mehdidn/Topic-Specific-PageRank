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
    adj = [[] for i in range(number_of_vertices)]

    start_line_of_edges = 4

    # for each line in data
    for i in range(number_of_Edges):

        # Current line
        line = lines[i + start_line_of_edges]

        # each line is in format u v and
        # means u has an edge to v so u->v
        # in each line: u=line[0] and v=line[2]
        # add v to adj[u]
        try:
            adj[int(line[0]) - 1].append(int(line[2]) - 1)
        except:
            pass

    # Getting beta from data
    # split one line before the last line
    parts = lines[len(lines) - 2].split()

    # floating number of beta is the
    # last part from parts
    beta = float(parts[len(parts) - 1])

    # Getting teleport set from data
    # split last line
    parts = lines[len(lines) - 1].split()

    # Ignore two first indices
    # first index is 'S'
    # second index is '='
    start = 2

    # Handle data input for {x,y,z}
    if len(parts) == 3:
        parts = parts[start].split(',')
        start = 0

    # Set teleport set
    S = []
    for i in range(start, len(parts)):

        # at start the format is '{x'
        if i == start:
            S.append(int(parts[i][1]))

        # others are in format 'x...'
        else:
            S.append(int(parts[i][0]))

    return number_of_vertices, number_of_Edges, adj, beta, S
