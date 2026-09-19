def k_means_centroid_update(points: list, assignments: list, k: int) -> list:
    """
    Returns one updated centroid for each cluster.
    """
    # Write code here
    n = len(points[0])
    m = len(points)
    centroids = []
    for i in range(k):
        list_points = [points[j] for j in range(m) if assignments[j] == i]
        point = [0 for j in range(n)]
        for each_point in list_points:
            for j in range(n): point[j] += each_point[j]
        if len(list_points) > 0:
            for j in range(n):
                point[j] = point[j] / len(list_points)
        centroids.append(point)

    return centroids