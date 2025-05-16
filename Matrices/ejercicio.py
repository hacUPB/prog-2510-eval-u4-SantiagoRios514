Matriz = [[1,4,6,8,3],[8,9,12,54,47],[98,45,78,3,10]]
print(Matriz)

fil = len(Matriz)
col = len(Matriz[0])

for i in range(fil):
    for j in range(col):
        print(f"{Matriz[i][j]:4}", end='  ')
    print()