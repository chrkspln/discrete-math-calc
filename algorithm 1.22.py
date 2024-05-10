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
    