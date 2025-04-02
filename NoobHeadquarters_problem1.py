m = int(input("Enter m: "))
n = int(input("Enter n: "))
a = []
count = 1

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    row = []
for i in range(n):
    for j in range(m):
        
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
        

