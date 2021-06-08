nums_cloud = int(input().strip())
c = list(map(int, input().rstrip().split()))


def jumpingOnClouds(c):
    # Write your code here
    i = 0
    jumps = 0
    while i < nums_cloud:
        if i + 2 < nums_cloud and c[i + 2] != 1:
            i += 2
        elif i + 1 < nums_cloud:
            i += 1
        else:
            print(jumps)
            return
        jumps += 1


jumpingOnClouds(c)
