from solution import min_path
import json

def deserialize(serialized: list[list[str]]):
    return [[int(x) for x in y] for y in serialized]

def solve(adj: list[list[int]], edges: list[list[int]]):
    g = []
    
    for i in range(len(adj)):
        g.append(list(map(lambda x: (x, edges[i][x]), adj[i])))

    return min_path(g)

def validate(solution: list[list[int]], correct: list[list[int]]):
    if len(solution) != len(correct): return False
    for i in range(0, len(solution)):
        if len(solution[i]) != len(correct[i]): return False
        for j in range(0, len(solution)):
            if correct[j] != solution[j]: return False
    
    return True



with open("Second/test_cases_2.json") as file:
    data = json.load(file)

for item in data:
    result = solve(deserialize(item['adj']), deserialize(item["edges"]))
    case = item['test_case']
    print()
    try:
        assert result == [int(x) for x in case]  #validate(dist, deserialize(item['result']))
        print(f"Case {case} ======== OK")
    except:
        ans = item['result']
        print(f'case {case} ================================================= ERROR')


def deserialize(serialized: list[list[str]]):
    return [[int(x) for x in y] for y in serialized]