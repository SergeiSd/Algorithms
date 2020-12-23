def KnapSack(K, item_weights, item_values, n, table, things, i, j): 

    for i in range(n + 1): 
        for w in range(K + 1): 

            if i == 0 or w == 0: 
                table[i][w] = 0

            elif item_weights[i-1] <= w: 
                table[i][w] = max(item_values[i-1] + table[i-1][w-item_weights[i-1]], table[i-1][w]) 

            else: 
                table[i][w] = table[i-1][w] 

    while True:

        if table[i][j] != table[i-1][j]:
            things.append(i-1)
            j = K - item_weights[i-1]

        i -= 1
        if i == 0:
            break

    things.sort()

    print("\nThe best option would be to take things like this:\n")

    for id, thing in enumerate(things):
        print(str(id + 1) + '. Item: ' + str(thing + 1) + ", cost = " + str(item_values[thing]), ", weight = " + str(item_weights[thing]))

    print("\nTheir total cost = ", table[n][K])
  
# Input data
item_values = [16, 19, 23,28] 
item_weights = [2, 3, 4, 5] 

K = 7 # total weight capacity
n = len(item_values)

table = [[0 for i in range(K + 1)] for j in range(n + 1)] 
things = list()
i, j = n, K

print('All items:\n\n', '  Cost', ' Weight')
for x in range(len(item_values)):
    print(str(x+1) + '.', item_values[x], '\t', item_weights[x])
    
KnapSack(K, item_weights, item_values, n, table, things, i, j)