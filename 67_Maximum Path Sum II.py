with open('resources/0067_triangle.txt') as file:
    text = file.read().splitlines()
    triangle  = []
    for line in text:
        k = list(map(int, line.split()))
        triangle.append(k)
    # print(triangle)
    triangle.reverse()
    length = len(text)
    # print(triangle)

    for idx, ele in enumerate(triangle):
        if len(ele) == 1:
            print(ele[0])
            break
        for i in range(len(triangle[idx+1])):
            triangle[idx+1][i] += max(triangle[idx][i], triangle[idx][i+1])
