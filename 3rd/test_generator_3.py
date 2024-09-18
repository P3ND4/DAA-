import random as rnd
import json
from heap import MinHeap

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def permutations(text: str, k: int) -> tuple[bool, str]:
  contain = set()
  return permutations_rec(text, contain, '', k)

def permutations_rec(text: str, contain: set, carry: str, k: int) -> None:
  if text == '':
    if not carry in contain:
      contain.add(carry)
      result = validator(carry, k) 
      return result
    return (False, carry)
  
  for i in range(len(text)):
    perm = permutations_rec(text[:i] + f"{text[i + 1:] if i + 1 < len(text) else ''}", contain, f'{carry}{text[i]}', k)
    if perm[0]: return perm
  return perm
#print(permutations('1113'))

def validator(query, k):
    query = query[-1::-1]
    freq = [0]*len(alphabet)
    maxim = 0
    heap = MinHeap()
    for i in range(0, len(query)):
        pos = alphabet.index(query[i])
        freq[pos] += 1
        maxim = max(maxim, freq[pos])
        heap.insert(alphabet[pos], freq[pos])
        minim = heap.peek() 
        while(freq[alphabet.index(minim[0])] != minim[1]):
            heap.extract_min()
            minim = heap.peek()
        if(maxim - minim[1] > k):
           return False, query[-1::-1]
    return True, query[-1::-1]
               
def organize_string(input_string):
    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Ordenar los caracteres alfabéticamente y luego por frecuencia
    sorted_chars = sorted(char_count.items(), 
                          key=lambda x: (x[0].lower(), -x[1]))
    
    return ''.join(char * count for char, count in sorted_chars)
        






def generate_cases(case = 100):
    cases = []
    while(case):
        boolean_mask = [False]*len(alphabet)
        str_len = rnd.randint(1, 15)
        str_case = ''
        symbols_set = []
        for i in range (0, str_len):
            pos = rnd.randint(0, len(alphabet)-1)
            str_case += alphabet[pos]
            if not boolean_mask[pos]:
                symbols_set.append(alphabet[pos])
                boolean_mask[pos] = True
        print(str_case)
        print(symbols_set)
        query = organize_string(str_case)
        k = rnd.randint(1, len(str_case))
        ans = permutations(query, k)
        ans = ans[1] if ans[0] else -1
        test_case = {'id': f'{case}',
                    'word': f'{str_case}',
                    'alph': [ symbol for symbol in symbols_set],
                    "k": f'{k}',
                    'ans': f'{ans}'}
        cases.append(test_case)
        case = case -1

    with open('test_cases.json', 'w') as f:
        json.dump(cases, f, indent=2)

print(permutations('jwjmgcrj', 1))
#generate_cases()



