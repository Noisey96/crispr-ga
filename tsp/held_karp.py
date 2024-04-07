def cost_of_tour(graph, tour):
    cost = 0
    for i in range(0, len(tour)):
        if i == len(tour) - 1:
            cost += graph[tour[i]][tour[0]]
        else:
            cost += graph[tour[i]][tour[i+1]]
    return cost

def held_karp_rec(graph, cache, curr_tour_vertices, remaining_vertices):
    # cache
    key = curr_tour_vertices[len(curr_tour_vertices) - 1:]
    key.extend(remaining_vertices)
    if tuple(key) in cache:
        return cache[tuple(key)]

    # base case
    if len(curr_tour_vertices) == len(graph):
        return graph[curr_tour_vertices[len(curr_tour_vertices) - 1]][curr_tour_vertices[0]]
    
    min_cost = float("inf")
    for vertex in remaining_vertices:
        next_tour_vertices = curr_tour_vertices.copy()
        next_tour_vertices.append(vertex)
        next_remaining_vertices = remaining_vertices.copy()
        next_remaining_vertices.remove(vertex)
        next_edge_cost = graph[curr_tour_vertices[len(curr_tour_vertices) - 1]][vertex]
        next_remaining_cost = held_karp_rec(graph, cache, next_tour_vertices, next_remaining_vertices)
        total_cost = next_edge_cost + next_remaining_cost
        if total_cost < min_cost:
            min_cost = total_cost
    cache[tuple(key)] = min_cost
    return min_cost

def held_karp(graph):
    return held_karp_rec(graph, {}, [0], list(range(1, len(graph))))