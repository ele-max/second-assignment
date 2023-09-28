def calculate_expected_offspring(couples):
    A, B, C, D, E, F = couples

    expected_offspring = 2 * (
        A * 1 +
        B * 1 +
        C * 1 +
        D * 0.75 +
        E * 0.5
    )

    return expected_offspring



couples = [18757, 16461, 17487, 18110, 19474, 19588]  # Replace with the actual number of couples for each genotype pairing
expected_offspring = calculate_expected_offspring(couples)
print(expected_offspring)
