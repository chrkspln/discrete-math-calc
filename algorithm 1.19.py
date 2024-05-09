def print_partition(block, n):
    partition = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        partition[block[i]].append(i)
    partition = [p for p in partition if p]
    
    for i in partition:
        print("(", end="")
        for element in i:
            print(element, end="")
        print(")", end=" ")
    print()


def number_partitions(n):
    block = [1] * (n + 1)
    next = [0] * (n + 1)
    prev = [0] * (n + 1)
    moving_forward = [True] * (n + 1)

    next[1] = 0
    print_partition(block, n)
    j = n

    while j > 1:
        k = block[j]

        if moving_forward[j]:
            if next[k] == 0:
                next[k] = j
                prev[j] = k
                next[j] = 0

            if next[k] > j:
                prev[j] = k
                next[j] = next[k]
                prev[next[j]] = j
                next[k] = j

            block[j] = next[k]
        else:
            block[j] = prev[k]

            if k == j:
                if next[k] == 0:
                    next[prev[k]] = 0
                else:
                    next[prev[k]] = next[k]
                    prev[next[k]] = prev[k]
        print_partition(block, n)
        j = n
        while j > 1 and ((moving_forward[j] and block[j] == j)
                         or (not moving_forward[j] and block[j] == 1)):
            moving_forward[j] = not moving_forward[j]
            j -= 1


# Main function
if __name__ == "__main__":
    number_partitions(4)
