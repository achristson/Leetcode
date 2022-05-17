"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

idea:
prims algorithm
build the graph based on points
we will start from point 0 and try to visit each point
add point to in our min heap
    we will be popping from the min heap
    if we have not visited the point yet then add the distance to the total min cost, mark the point as visited and add its neighbors to the min heap
    look at all neighbors and add the minimum distance to our total min cost
once we have visited each point then we should have the min_cost

let n be the number of points in points
Time: O(n^2logn)
Space: O(n^2)

"""

def minCostConnectPoints(self, points: List[List[int]]) -> int:
    num_points = len(points)
    graph = {point: [] for point in range(num_points)}

    for i in range(num_points):
        x1, y1 = points[i]
        for j in range(i + 1, num_points):
            x2, y2 = points[j]
            distance = abs(x1 - x2) + abs(y1 - y2)
            graph[i].append((distance, j))
            graph[j].append((distance, i))

    total_min_cost = 0
    visited = set()
    min_heap = [(0, 0)]

    while len(visited) < num_points:
        cost, point = heapq.heappop(min_heap)
        if point not in visited:
            total_min_cost += cost
            visited.add(point)
            for distance, neighbor in graph[point]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (distance, neighbor))
    return total_min_cost
