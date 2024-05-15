from random import randint


def wiener(e, n):
    tmp_e = e
    tmp_n = n
    m = randint(2, n - 1)
    a = tmp_e // tmp_n
    P_prev, P_curr = 1, 0
    Q_prev, Q_curr = 0, 1
    while a * tmp_n != tmp_e:
        tmp_e, tmp_n = tmp_n, tmp_e - a * tmp_n
        a = tmp_e // tmp_n
        P_next = a * P_curr + P_prev
        Q_next = a * Q_curr + Q_prev
        P_prev, P_curr = P_curr, P_next
        Q_prev, Q_curr = Q_curr, Q_next
        if pow(pow(m, e, n), Q_next, n) == pow(m, 1, n):
            return Q_next
    return 0

