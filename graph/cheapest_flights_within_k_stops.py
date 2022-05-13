"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
 

Example 1:

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.


idea:
we will maintain a prices and temp prices array
all indices will be set to inf except the source index which will be 0
we will iterate through the flights array k + 1 times 
in each iteration we will update the temp prices array with the price it takes to reach the destination
if the price for the current source is inf then we skip that source because it will take more stops to reach the destination than the current k we are trying for
if it is not inf we can take the min of sum of the price from the last iteration and the price from the source and the current price
at the end of that k we copy the values from temp prices to prices 
in the end we can return the value of dst in prices if it is not inf else we return -1

Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
let e be the number of edges in the graph
let k be the minimum number of stops
let n be the number of cities
Time: O(e * k)
Space: O(e + n)
"""


def findCheapestPrice(n, flights, src, dst, k):
    prices = [float("inf")] * n
    prices[src] = 0

    for _ in range(k + 1):
        temp_prices = prices[:]

        for source, dest, price in flights:
            if prices[source] == float("inf"):
                continue
            temp_prices[dest] = min(prices[source] + price, temp_prices[dest])
        prices = temp_prices

    return prices[dst] if prices[dst] != float("inf") else -1
