import json

def solve(query, alph, k):
    pass

with open("3rd/test_cases.json") as file:
    data = json.load(file)

for item in data:
    result = solve(item['word'], item["alph"], int(item["k"]))
    try:
        assert result[1] == item['ans']
        case = item['id']
        print(f"Case {case} ======== OK")
    except:
        case = item['id']
        ans = item['ans']
        print(f'case {case} ================================================= ERROR, Ans {result} != {ans}')
