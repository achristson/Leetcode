"""

Let's say you are trying to exchange currencies
Each currency is represented by three upper case letters like USD or CAD or EUR etc.
Let's say you have a list of exchage rates 
Don't assume that rates are inverse exactly
If an exchange rate between two pairs isn't provided assume it's not possible to trade them

USD CAD 1.25 (this means you can sell 1.0 USD and buy 1.25 CAD)
CAD USD 0.80 
CAD EUR 0.60
USD EUR 0.70
EUR USD 1.50

Problem is given the exchange rate list and a source currency and a target one find the best 
exchange rate between and the list of trades that are needed to achieve it. 
If it's possible to perform arbitrage then print ARBITRAGE and output the cycle.
    1.25->
USD  <->  CAD
| | <-0.80  \ 0.60
|  <-----------EUR 
|       1.50    ^ 
----------------|
        0.70

USD -> EUR 1.25 * 0.60 = 0.75
[USD, CAD, EUR]
[1, 1.25, 0.70]
[[USD], [USD, CAD],[USD, CAD, EUR]]

idea:
bellman-ford
we will iterate through all the edges for the same number of times as there are currencies
in each iteration we will update the exchange rate and record the path if we find a better one 
if we find a better exchange rate and the currency we are currently on is already in the path then we have discovered arbitage and we can stop 
if not we can make the update, record the path and continue
at the end we should have the best exchange rate and the path to get it

let v be the number of vertices in the graph
let e be the number of edges in the graph
Time: O(v * e)
Space: O(v + e)
"""
rates = [
    ["USD", "CAD", 1.25],
    ["CAD", "USD", 0.80],
    ["CAD", "EUR", 0.60],
    ["USD", "EUR", 0.70]
]


def currency_exchange_rate(rates, source, target):
    graph = {}

    for src, dest, rate in rates:
        if src not in graph:
            graph[src] = []
        if dest not in graph:
            graph[dest] = []
        graph[src].append((dest, rate))

    exchanges = {currency: -float("inf") for currency in graph}
    exchanges[source] = 1

    paths = {currency: [] for currency in graph}
    paths[source].append(source)

    for _ in range(len(graph)):
        for currency in graph:
            for edge, rate in graph[currency]:
                if exchanges[currency] * rate > exchanges[edge]:
                    if edge in paths[currency]:
                        print("arbitage")
                        print(paths[currency] + [edge])
                        return 
                    else:
                        exchanges[edge] = exchanges[currency] * rate
                        paths[edge] = paths[currency] + [edge]
    return exchanges[target], paths[target]
