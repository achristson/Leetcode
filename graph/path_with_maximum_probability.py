"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:

Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.

idea:
build a graph with the edges and succProb information
we will use dijkstra for this problem since we have weighted edges
since we want the maximum probability we will use a max heap
we can start by adding the starting node to the max heap with a probability of 1
while our max heap is not empty we will pop from it 
if we are at our end node we will update the max probability 
if not we will add all our neighbors to the max heap with our probability times their probability as their new probability
in the end we can return the max probability if we see our end node in the visited set
else we return 0 as we were not able to reach it

Link: https://leetcode.com/problems/path-with-maximum-probability/
let n = number of nodes in the graph
let e = number of connections in edges
Time: O(elogn)
Space: O(n)
"""

def maxProbability(n, edges, succProb, start, end):
    graph = {node:[] for node in range(n)}

    for i, edge in enumerate(edges):
        graph[edge[0]].append((succProb[i], edge[1]))
        graph[edge[1]].append((succProb[i], edge[0]))

    max_heap = [(1, start)]
    visited = set()
    max_prob = 0.0

    while max_heap:
        prob, node = heapq.heappop(max_heap)
        if node == end:
            max_prob = min(max_prob, prob)
        if node not in visited:
            visited.add(node)
            for new_prob, neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(max_heap, (-1 * abs(new_prob * prob), neighbor))
    return -max_prob if end in visited else 0
