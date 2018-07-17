def eight_queens(a):
    lista=[]
    listb=[]
    
    for i in range(len(a)):
        lista.append(a[i][0])

    for j in range(len(a)):
        listb.append(a[j][1])

    if len(lista)==len(set(lista)) and len(listb)==len(set(listb)):

        listc=[]
        for k in range(len(a)):
            listc.append(int(a[k][1]-a[k][0]))
        if len(listc)==len(set(listc)):
            return True
        else:
            return False
    else:
        return False

print(eight_queens([[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]]))