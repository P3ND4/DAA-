import json

def solve(query: str, alph: list, k: int):
    '''
        Query: cadena de texto que deseamos consultar 
        \n
        Alph: symbolos involucarados en query
        \n
        k: la onstante que define cuando es buena la cadena de texto
    '''
    raise NotImplementedError('Realiza la llamada a la solucion desde aqui')

with open("3rd/test_cases.json") as file:
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
