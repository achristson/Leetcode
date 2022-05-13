"""
You are given a network of n nodes, labeled from 1 to n. 
You are also given times, a list of travel times as directed edges 
times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. 
Return the time it takes for all the n nodes to receive the signal. 
If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1

idea:
generate a graph using the times array
each node will map to a neighbor and the weight tuple
since this is a weighted shortest path problem we can use dijkstra
we will keep a min heap which will start with source node
we will also keep the time it takes to send the signal as the max of the sum of each source to node path
we will also have a set to prevent infinite looping
while the min heap is not empty we will pop from it and check to see if the node we got has been visited
if it has we can skip it
if it hasn't then we add it to visited and then update our time
then we can add our neighbors to the min heap
if we were able to visit each node the we can return the time
if not we can return -1

Link: https://leetcode.com/problems/network-delay-time/
Time: O(n + elogn)
Space: O(n + e)

"""


def network_delay_time(times, n, k):
    graph = {x: [] for x in range(1, n + 1)}

    for u, v, w in times:
        graph[u].append((w, v))

    min_heap = [(0, k)]
    time = 0
    visited = set()

    while min_heap:
        weight, node = heapq.heappop(min_heap)
        if node not in visited:
            visited.add(node)
            time = max(time, weight)

            for neighbor_weight, neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (neighbor_weight + weight, neighbor))
    return time if len(visited) == n else -1
