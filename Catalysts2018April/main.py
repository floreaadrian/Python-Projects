start = int(input())
end = int(input())
nrImg = int(input())
timeStamp = []
for t in range(nrImg):
    time = int(input())
    row = int(input())
    col = int(input())
    matrix = [[0 for x in range(row)] for y in range(col)]
    for i in range(row):
        for j in range(col):
            matrix[row][col] = int(input())
