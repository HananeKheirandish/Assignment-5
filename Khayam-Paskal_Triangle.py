def khayam_paskal_triangle(n):
    list = [[0 for i in range(n+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(i):
            if i == j or j == 0:
                list[i][j] = 1
            else:
                list[i][j] = list[i-1][j-1] + list[i-1][j]
    for i in range(n+1):
        for j in range(i):
            print(list[i][j] , end = ' ')
        print()
        
n = int(input('please enter number: '))
khayam_paskal_triangle(n)