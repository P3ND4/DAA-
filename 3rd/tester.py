import json
import os

def solve(query, alph, k):
    pass

with open("3rd/test_cases.json") as file:
    data = json.load(file)

for item in data:
    result = solve(item['word'], item["alph"], item["k"])
    try:
        assert result == item['ans']
        case = item['id']
        print(f"Case {case} ======== OK")
    except:
        case = item['id']
        ans = item['ans']
        print(f'case {case} ================================================= ERROR, Ans {result} != {ans}')
