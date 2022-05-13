
def product(A, B):
    results = []
    for a in A:
        for b in B:
            results.append((a, b))
    for result in results:
        yield result


for prod in product(["Peter", "Mark", "Mary"], ["Paul", "Jane", "Mark", "Mary"]):
    print(prod)
