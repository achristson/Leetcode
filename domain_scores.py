"""
Let's say you are given a list of domain names (e.g. "www.google.com") and 
associated with each an integer that's called a "score". Write a program that 
calculates for each domain its "total score" which is the sum of its score 
AND all its ancestor domain scores.

Example:
www.google.com  10
google.com  20
com  -5
mail.google.com 20
facebook.com 30
mail.facebook.com -10

Output should be:
www.google.com  10 + 20 - 5 = 25
google.com  20 - 5 = 15
com  -5
mail.google.com 20 + 20 - 5 = 35
facebook.com 30 - 5 = 25
mail.facebook.com -10 + 30 - 5 = 15

Idea:
Store each domain into a hash map with the score as the value
go through the list
for each domain we split on the '.' and then reverse iterate through the new list
create previous and current variables to store the previous string we checked and the current string we are checking
add the current string to previous string with a dot between them if the previous string is not empty
update the score with the new value
once we iterate through the string we store the final score along with the completed string in a list

Example:

given the list:
[
    ("www.google.com", 10),
    ("google.com", 20),
    ("com", -5),
    ("mail.google.com", 20),
    ("facebook.com", 30),
    ("mail.facebook.com", -10)
]
hash_map = {
    "www.google.com": 10,
    "google.com": 20,
    "com": -5,
    "mail.google.com": 20,
    "facebook.com": 30,
    "mail.facebook.com": -10
    }
["www", "google", "com"] <- "www.google.com"

prev = "googlecom"
current = "www"
current + prev = "www.google.com"
score = 25
result = [("www.google.com", 25)]

"""


def domain_scores(domains):
    scores = {domain[0]: domain[1] for domain in domains}
    result = []
    for domain, score in domains:
        prev = ""
        score = 0
        for i in range(len(domain.split("."))-1, -1, -1):
            current = domain.split(".")[i]
            new_string = ""
            if prev:
                new_string = current + "." + prev
            else:
                new_string = current + prev
            score += scores[new_string]
            prev = new_string
        result.append((prev, score))
    return result


domains = [
    ("www.google.com", 10),
    ("google.com", 20),
    ("com", -5),
    ("mail.google.com", 20),
    ("facebook.com", 30),
    ("mail.facebook.com", -10)
]
# print(domains)
print(domain_scores(domains))

"""
let n = length of domains
let k = length of a particular domain
Time: O(n * k)
Space: O(n)
"""
