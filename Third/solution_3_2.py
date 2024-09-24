
from heap import MinHeap
def freq_dif(string):
    char_freq = {}
    for char in string:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    max_freq = max(char_freq.values())
    min_freq = min(char_freq.values())
    return max_freq - min_freq

def greedy_sufix(text: str, symb: list, k: int):
    if freq_dif(text) > k: return '-1'
    
    freq = {}
    symbol_set = sorted(symb)
    in_heap = {}
    sorted_text = sorted(text)
    max_freq = MinHeap()
    for char in sorted_text:
        freq[char] = 1 if char not in freq else freq[char] + 1

    for symbol in freq:
        max_freq.insert(symbol, -freq[symbol])
        in_heap[symbol] = 0
    result = ''
    for _ in text:
        while(in_heap[max_freq.peek()[0]]):
            max_freq.extract_min()
        for symbol in symbol_set:
            if((-max_freq.peek()[1] - freq[symbol] + 1 <= k and freq[symbol] > 1) or freq[symbol] == 1):
                result += symbol
                freq[symbol] -= 1
                if max_freq.peek()[0] == symbol:
                    max_freq.extract_min() 
                max_freq.insert(symbol, -freq[symbol])
                break
    return result         
            
        

        
        
print(greedy_sufix("bbikkpprs", ["p", "b", "s", "k", "i", "r"], 1) )


    

    