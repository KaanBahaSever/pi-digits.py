def pi_spigot():
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4 * q + r - t < n * t:
            yield n
            q, r, t, k, n, l = (
                10 * q,
                10 * (r - n * t),
                t,
                k,
                (10 * (3 * q + r)) // t - 10 * n,
                l,
            )
        else:
            q, r, t, k, n, l = (
                q * k,
                (2 * q + r) * l,
                t * l,
                k + 1,
                (q * (7 * k + 2) + r * l) // (t * l),
                l + 2,
            )


# Generator to get pi digits
def generate_pi_digits(limit):
    pi_digits = pi_spigot()
    pi_str = ""
    count = 0
    for digit in pi_digits:
        if count == limit:
            break
        pi_str += str(digit)
        count += 1
    return pi_str


# Example usage: Generate the first 100 digits of Pi
print(generate_pi_digits(100))
