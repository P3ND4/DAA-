def sufix_balance(chain: str, k: int) -> str | int:
  frec_list = frec(chain)
  
  if not validate(chain, frec_list, k):
    return -1
  
  return fix_balance(k, frec_list)
        
def validate(chain: str, l: list[tuple], k: int) -> bool:
  max = 0
  min = len(chain) 
  
  for tuple in l:
    if tuple[1] >= max:
      max = tuple[1]
    
    if tuple[1] <= min:
      min = tuple[1]
  
  return max - min <= k
      
def fix_balance(k: int, frec: list) -> str:
  del_nodes = 0
  result = ''
  round1 = False
  
  while del_nodes < len(frec):
    max_space = 1 if round1 else k + 1
    first_node_space = 2 if not round1 else 1
    
    for i in range(len(frec)):
      if i == 0:
        for j in range(max_space):
          if frec[i][1] == 0:
            break
          
          frec[i] = (frec[i][0], frec[i][1] - 1, frec[i][2])
          result += frec[i][0]

          if frec[i][1] == 0:
            del_nodes += 1 

      elif i < len(frec) - 1:
        rest = frec[i][1] - frec[frec[i][2]][1]
        
        for j in range(max_space):
          if frec[i][1] == 0:
            break
          
          frec[i] = (frec[i][0], frec[i][1] - 1, frec[i][2])
          result += frec[i][0]
          rest -= 1
          
          if frec[i][1] == 0:
            del_nodes += 1 
            
          if rest <= 0:
            break
        
      else:
        for j in range(first_node_space):
          if frec[i][1] == 0:
            break
        
          frec[i] = (frec[i][0], frec[i][1] - 1, frec[i][2])
          result += frec[i][0]
          
          if frec[i][1] == 0:
            del_nodes += 1 
    
    round1 = True
            
  return result[-1::-1]
          
def frec(chain: str) -> list:
  frec = {}
  temp = []
  result = []
  
  for char in chain:
    try:
      frec[char] += 1
    
    except:
      frec[char] = 1
  
  for key in frec:
    temp.append((key, frec[key]))
  
  temp = sorted(temp, key=lambda x:x[0])[-1::-1]
  
  max = 0
  index = 0
  result.append((temp[0][0], temp[0][1], 0))
  
  for i in range(1, len(temp)):
    if temp[i][1] > max:
      max = temp[i][1]
      result.append((temp[i][0],temp[i][1], index))
      index = i
    
    else:
      result.append((temp[i][0],temp[i][1], index))
      
  return result
