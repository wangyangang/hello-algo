def back_track(row, n, state, res, cols, angles1, angles2):
    if row == n:
        res.append([list(row) for row in state])
        return

    for col in range(n):
        angle1 = row - col + n - 1
        angle2 = row + col
        if not cols[col] and not angles1[angle1] and not angles2[angle2]:
            state[row][col] = 'Q'

            cols[col] = angles1[angle1] = angles2[angle2] = True
            back_track(row + 1, n, state, res, cols, angles1, angles2)
            state[row][col] = '#'
            cols[col] = angles1[angle1] = angles2[angle2] = False


def n_queens(n):
    res = []
    cols = [False for _ in range(n)]
    angles1 = [False for _ in range(2 * n - 1)]
    angles2 = [False for _ in range(2 * n - 1)]
    state = [['#' for _ in range(n)] for _ in range(n)]
    back_track(0, n, state, res, cols, angles1, angles2)
    return res


if __name__ == '__main__':
    res = n_queens(5)
    for item in res:
        for row in item:
            print(row)
        print('-' * 16)