metro_graph = {"admiralteyskaya":
                   {"sadovaya": 4},
               "sadovaya":
                   {"admiralteyskaya": 4,
                    "sennaya ploshad": 3,
                    "spasskaya": 3,
                    "zvenigorodskaya": 5},
               "sennaya ploshad":
                   {"sadovaya": 3,
                    "spasskaya": 3},
               "spasskaya":
                   {"sadovaya": 3,
                    "sennaya ploshad": 3,
                    "dostoyevskaya": 4},
               "dostoyevskaya":
                   {"spasskaya": 4,
                    "vladimirskaya": 3},
               "vladimirskaya":
                   {"dostoyevskaya": 3,
                    "pushkinskaya": 4},
               "pushkinskaya":
                   {"vladimirskaya": 4,
                    "zvenigorodskaya": 3},
               "zvenigorodskaya":
                   {"sadovaya": 5,
                    "pushkinskaya": 3}}

distance = {point: 100 for point in metro_graph.keys()}

start_point = "admiralteyskaya"
distance[start_point] = 0

accounted_points = {point: False for point in metro_graph.keys()}
previous = {point: None for point in metro_graph.keys()}

for _ in range(len(distance)):
    closest_point = min([point for point in accounted_points.keys() if not accounted_points[point]],
                        key=lambda x: distance[x])

    for all_nearby in metro_graph[closest_point].keys():
        if distance[all_nearby] > distance[closest_point] + metro_graph[closest_point][all_nearby]:
           distance[all_nearby] = distance[closest_point] + metro_graph[closest_point][all_nearby]
           previous[all_nearby] = closest_point
    accounted_points[closest_point] = True

end_point = 'vladimirskaya'
while end_point is not None:
    print(end_point)
    end_point = previous[end_point]

