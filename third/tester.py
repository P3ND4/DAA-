from third.solution import sufix_balance
import json

def solve(query: str, alph: list, k: int):
    return sufix_balance(query, k)

with open("test_cases.json") as file:
    data = json.load(file)

for item in data:
    result = solve(item['word'], item["alph"], int(item["k"]))
    try:
        assert result == item['ans']
        case = item['id']
        print(f"Case {case} ======== OK")
    except:
        case = item['id']
        ans = item['ans']
        print(f'case {case} ================================================= ERROR, Ans {result} != {ans}')
