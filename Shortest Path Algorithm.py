###Nodes are are data structures between a pair of elements the connection between nodes are called **edges**
###Looks like we get to use list() that will lists through something that is iterable.
###I only really had to look up step 30 for the dictionary comprehension. It took me about ten minutes to realize I did not write the for, I completly skipped that word. Note to self, sometimes it is the little issues that drive you the craziest.
# It is nice to get a quick review of the ternnary stuff it does make things much easier, and a review would be good to not get it confused with JS

# What kind of graph is this? Bing Copilot says basically the intro to lesson said but also calls it an adjacency list
# From more reading and changing the code around with throwing in some prints()
my_graph = {
    "A": [("B", 5), ("C", 3), ("E", 11)],
    "B": [("A", 5), ("C", 1), ("F", 2)],
    "C": [("A", 3), ("B", 1), ("D", 1), ("E", 5)],
    "D": [("C", 1), ("E", 9), ("F", 3)],
    "E": [("A", 11), ("C", 5), ("D", 9)],
    "F": [("B", 2), ("D", 3)],
}


def shortest_path(graph, start, target=""):
    # list() is a way to extract the keys from a dictionary without having to use loops or .keys
    unvisited = list(graph)
    # print("This is the list from graph", unvisited)
    # float("inf"), per Stackoverflow, is a way to set an unbound upper value for comparison and it is useful for finding the lowest values of something.
    # The nodes are the keyes of the dictionary
    distances = {node: 0 if node == start else float("inf") for node in graph}
    # Example outputof distances if start = 'A'
    ### {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf}
    # print("This is distances: ", distances)
    # Paths takes the node,or key, from the dictionary and gives it an empty list
    paths = {node: [] for node in graph}
    # Output example This is paths:  {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': []}
    # print("This is paths: ", paths)
    paths[start].append(start)
    while unvisited:
        # .get is in cases where the key does not exist in the dictionary and returns None instead of an error
        current = min(unvisited, key=distances.get)

        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(
            f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}'
        )

    return distances, paths


shortest_path(my_graph, "A", "F")
