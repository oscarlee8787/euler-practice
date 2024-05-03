with open('resources/0067_triangle.txt') as file:
    text = file.read().splitlines()
    text.reverse()
    length = len(text)
    num = 0

    for idx, ele in enumerate(text):
        if len(ele) == 1:
            num += ele[0]
            print(num)
        for i in range(len(idx+1)):
            num +=



    # pos = 0
    # ans = 0
    # left = 0
    # right = left + 1
    # for i in range(length):
    #     if text[i+1][left] >
    #     new_num = max(text[i+1][left], text[i+1][right])
    #     ans += new_num
    #     pos =
    print(text[-1])
