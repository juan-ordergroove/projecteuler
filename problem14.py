max_chain = 0
max_starter = 1
chain_map = {1: 1}
for starter in range(2, 10**6+1):
# for starter in range(2,5):
    chain_count = 1
    tmp = starter
    while tmp != 1:
        if chain_map.get(tmp):
            chain_count += chain_map.get(tmp)
            break
        chain_count+=1
        if tmp % 2 == 0: tmp/=2
        else: tmp = 3*tmp+1
    chain_map[starter] = chain_count
    if chain_count > max_chain:
        max_chain = chain_count
        max_starter = starter
print max_starter