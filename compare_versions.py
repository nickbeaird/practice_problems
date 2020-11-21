# Nick Beaird
# 11/20/2020
# Compare two strings of versions and return 1 if the first is greater else 0.

def is_version_greater_simple(version1, version2) -> int:
    """Returns 1 if the first version is equal to or greater than the second version else returns 0."""

    if not isinstance(version1, str) or not isinstance(version2, str):
        raise TypeError("version1 and version2 must be strings.")

    if len(version1) == 0 or len(version2) == 0:
        raise ValueError("version1 and version2 must contain string values.")

    # Increase in space used by O(n)
    version1_values = [int(num) for num in version1.split('.')]
    version2_values = [int(num) for num in version2.split('.')]
    len_a = len(version1_values)
    len_b = len(version2_values)
    len_of_shorter = min(len_a, len_b)
    is_index_exhausted = len_of_shorter - 1

    for i in range(len_of_shorter):
        v1, v2 = version1_values[i], version2_values[i]

        if v1 > v2:
            return 1
        elif v1 < v2:
            return 0

        # Assume remainder of values are equals.
        if i == is_index_exhausted:
            # Decision point: Do we return 1 for values that are the same?
            if len_b == len_a:
                return 1
            elif len_a > len_b:
                return 1
            else:
                return 0
