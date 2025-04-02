m = int(input("Enter m "))
n = int(input("Enter n "))
a = []
count = 1
for i in range(n):
    a.append(input("Enter grids"))
for i in range(1,m):
    for j in range(n):
        
        if a[i][j] == 1:
            if i == m-1:
                if a[i-1][j] == 1:
                    break
                else:
                    count += 1
            if a[i-1][j] == 1 or a[i+1][j] == 1:
                break
            else:
                count += 1
                
print(count)
        

