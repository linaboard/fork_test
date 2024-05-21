#test
num_vertices = 5 #정점 개수
num_edges = 6    #간선 개수

b = [[0 for j in range(3)] for i in range(num_edges + 1)] #3x(간선개수+1)의 리스트 형성
a = [[0 for j in range(num_vertices + 1)] for i in range(num_vertices + 1)]
#정점개수x정점개수의 리스트형성
#print("b",b) b는 [0,0,0]인 리스트를 간선개수 + 1개 가지고있는 리스트이다
#print("a",a) a는 [0,0,0,0,0,0]인 리스트를 정점개수 + 1개 가지고있는 리스트이다
#a[i][j] 는 정점i 정점j가 연결되었는지 여부를 반환한다

order = [0 for i in range(num_vertices + 1)] #정점의 번호는 1 2 3 4 5로 1부터 시작하므로
deg = [0 for i in range(num_vertices + 1)] #i번쨰 정점의 가중치를 저장
col = [0 for i in range(num_vertices + 1)]

print("정점 5개를 가진 평면 그래프입니다.")
print("관계를 1 2 와 같은 순서쌍으로 6개 입력하시오.")
#정점의 번호는 1부터 시작하므로 i도 1부터 시작한다
for i in range(1, num_edges + 1): #간선개수만큼 입력받으며 연결된 두 정점으로 입력받음
    values = input().strip().split()
    b[i][1] = int(values[0])# i번째 입력에 대해서 b의 1번인덱스는 첫 정점
    b[i][2] = int(values[1])# i번째 입력에 대해서 b의 2번 인덱스는 두번째 정점
    a[b[i][1]][b[i][2]] = 1 # a[첫정점][두번째정점] = 1로 초기화
    a[b[i][2]][b[i][1]] = 1 # a[두번째정점][첫정점] = 1로 초기화

print("\n---------------------------")
print("edge matrix")
for i in range(1, num_edges + 1):
    print("(%d,%d)" %(b[i][1], b[i][2])) #연결된 정점들을 출력한다
print("---------------------------")

for i in range(1, num_vertices + 1):
    for j in range(1, num_vertices + 1):
        if a[i][j] != 0: #정점i와 정점j가 연결되어있으면
            deg[i] = deg[i] + 1 #정점의 가중치 1증가

print("\n---------------------------")
print("degree of vertex")

for i in range(1, num_vertices + 1):
    print("deg[%d] = %d"%(i, deg[i])) #정점의 가중치 출력
print("---------------------------")

for i in range(1, num_vertices + 1):
    order[i] = i

for i in range(1, num_vertices): #order에는 각 정점deg가 내림차순이 되도록 인덱스를 정렬하여 저장한다
    for j in range(i + 1, num_vertices):
        if deg[order[i]] < deg[order[j]]:
            temp = order[i]
            order[i] = order[j]
            order[j] = temp
# for i in range(1, num_vertices + 1):
#     print("test %d" %(order[i]))


#구현해야하는 부분
#col[i]에는 i번째 노드에 몇번의 색깔이 사용되었는지 저장한다
color = 0
for i in order:
    if (i == 0): #i가 0인 경우는 넘긴다
        continue
    elif (col[i] == 0): #현재 정점이 채색되어있지 않으면
        color = color + 1 #색번호를 증가시킨다
        col[i] = color #현재 정점에 채색한다
        for j in order: #j를 탐색하며 i노드와 인접하지 않은 노드도 채색해야한다
            if (j == 0 or col[j] > 0): #j가 0이거나 이미 채색된 정점이면 패스한다
                continue
            elif (a[i][j] == 0): #i와 j가 연결되지 않은 정점이면
                col[j] = color #j를 현재 노드의 색으로 칠한다
                for k in order: #i와 연결되지 않은 j번째 정점들을 채색하였는데, j번째 정점들중 인접한 정점이 존재하는지 검사해야한다
                    if (k == 0 or j == k): #0번 정점이거나 현재검토중인 정점과 같은 정점은 패스한다
                        continue
                    elif (j != k and a[j][k] == 1 and col[k] == color): #이번회차에 이미 채색한 노드와 인접하면
                        col[j] = 0 #색을 다시 지운다
                        break

# for i in range(1, num_vertices + 1): #order[i]가 현재 탐색하는 정점의 번호 #a[i][j] 가 i노드와 j노드가 연결되었는지를 확인하므로 이용한다
#     if (col[order[i]] == 0):
#         color = color + 1
#         col[order[i]] = color
#     temp_node = [0 for i in range(num_vertices + 1)] #temp노드를 생성해서 이번회차에 색칠한 노드번호를 저장한다 temp_node[i] = 1이면 i번째 노드가 이번탐색에서 색칠된것
#     for j in range(1, num_vertices + 1):
#         if (a[order[i]][order[j]] == 1): #i노드와 j노드가 연결되어있으면 #order[i] == order[j]인 경우도 체크해봐야한다
#             continue
#         elif(i != j and a[order[i]][order[j]] == 0 and col[order[j] == 0]): #현재 탐색중인 노드와 연결되어있지 않고, order[j]노드가 색칠되어있지 않으면
#             col[order[j]] = color #현재노드를 색칠한다
#             temp_node[order[j]] = color #temp_node에도 기록한다
#             print(order[i], order[j]) #여기로 안들어온다
#             for k in range(1, num_vertices + 1):
#                 if (j != k and temp_node[order[k]] == color and a[order[j][order[k]]] == 1): #이번회차에 칠한 노드와 연결되어있으면
#                     col[order[j]] = 0 #현재노드를 지운다
#                     temp_node[order[j]] = 0 #temp_node에서도 지운다


#
#구현
#1 2
#2 3
#3 4
#4 5
#1 3
#3 5





print("\n---------------------------")
print("vertex coloring")
for i in range(1, num_vertices + 1):
    print("color(v%d)=%d" %(i, col[i]))
print("---------------------------")
for i in range(1, num_vertices):
    if col[i] > col[i + 1]:
        col[i + 1] = col[i]
print("\n이 그래프는 %d색 가능합니다."%col[i + 1]);