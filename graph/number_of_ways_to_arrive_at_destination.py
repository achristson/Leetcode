"""
You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

Example 1:

Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

Example 2:

Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.

idea:
we will use dijkstra since this is a weighted graph problem
generate an undirected graph based on roads
keep the time it takes to get to each node
keep the number of ways to get to each node
when we reach a node in a shorter time than it previously took we will update the time it takes to reach the node and the number of ways to reach it
this will be based on the number of ways it took to reach the node we are coming from
when we reach a node in the same time as it previously took, then we will keep the time and update the number of ways to reach it
this will be based on the sum of the number of ways to reach the node we are coming from and the number of ways it took the node previously

Link: https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
let e = number of edges in the graph 
let n = number of nodes in the graph
Time: O(elogn)
Space: O(n + e)
"""


def countPaths(n, roads):
        graph = {node: [] for node in range(n)}
        
        for u, v, t in roads:
            graph[u].append((t, v))
            graph[v].append((t, u))
        
        times = [float("inf")] * n
        times[0] = 0
        
        ways = [0] * n 
        ways[0] = 1
        
        min_heap = [(0, 0)]
        
        while min_heap:
            time, node = heapq.heappop(min_heap)
            
            for new_time, neighbor in graph[node]:
                new_time += time
                if new_time < times[neighbor]:
                    heapq.heappush(min_heap, (new_time, neighbor))
                    times[neighbor] = new_time
                    ways[neighbor] = ways[node]
                elif new_time == times[neighbor]:
                    ways[neighbor] += ways[node]
        return ways[-1] % (10**9+7)
