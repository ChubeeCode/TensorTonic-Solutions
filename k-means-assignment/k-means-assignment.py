def k_means_assignment(points: list, centroids: list) -> list:
    """
    Returns the nearest-centroid index for every point.
    """
    # Write code here
    def cost(point: list, centroid: list) -> float:
        n = len(point)
        res = 0.0
        for j in range(n):
            res += (point[j] - centroid[j])**2
        return res
    
    m = len(points)
    k = len(centroids)
    index = [0 for i in range(m)]
    for i in range(m):
        dist = cost(points[i], centroids[0])        
        for j in range(1, k):
            dist_j = cost(points[i], centroids[j])
            if dist > dist_j:
                index[i] = j
                dist = dist_j

    return index