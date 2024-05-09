"""
Partition Generation:
The partition represented by S is appended to the result list at each iteration.
The loop iterates through the elements of S from right to left (d to 0) until it finds an element greater than 1.
It sums up the elements encountered.
If all elements are 1, it reaches the end of the partition, and the current partition is added to the result list.
Otherwise, it decreases the last non-1 element by 1, and increases the next element by 1, adjusting for the sum.
The loop continues until it exhausts all possible partitions.

This code utilizes a technique known as "restricted growth strings" to generate partitions.
It's a method commonly used in combinatorial algorithms for generating partitions.
The algorithm essentially iterates through the set of all partitions in a specific order without
explicitly generating all subsets, which makes it more memory efficient compared to generating all possible subsets
and then filtering them based on partition criteria.
"""


def num_partitions(n: int) -> list[list[int]]:
    result = []
    S = [0] * n
    S[0] = n
    depth = 0
    n = 1

    while True:
        result.append(S[:depth+1].copy())
        sum_ = 0
        while depth >= 0 and S[depth] == 1:
            sum_ += S[depth]
            depth -= 1

        if depth < 0:
            for line in result:
                print(line)
            return result

        S[depth] -= 1
        sum_ += 1

        while sum_ > S[depth]:
            depth += 1
            S[depth] = S[depth - 1]
            sum_ -= S[depth]

        if sum_ > 0:
            depth += 1
            S[depth] = sum_


if __name__ == "__main__":
    num_partitions(7)
    