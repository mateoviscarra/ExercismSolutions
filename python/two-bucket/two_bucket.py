def measure(bucket_one_capacity, bucket_two_capacity, goal, start_bucket):
    def gcd(a, b):  # Find greatest common divisor to avoid importing math
        while b:
            a, b = b, a % b
        return a
    #  Check the unsolvable cases:
    if goal > max(bucket_one_capacity, bucket_two_capacity):
        raise ValueError("Goal cannot be greater than the capacity of either bucket.")

    if goal % gcd(bucket_one_capacity, bucket_two_capacity) != 0:
        raise ValueError("Goal cannot be measured with the given bucket capacities.")

    if start_bucket not in ["one", "two"]:
        raise ValueError("Invalid start_bucket. Choose either 'one' or 'two'.")

    def simulate(start_cap, other_cap, goal, which_bucket):
        start = start_cap
        other = 0
        actions = 1  # First fill

        if other_cap == goal:
            return 2, ("one" if which_bucket == "two" else "two"), start

        while start != goal and other != goal:
            if start == 0:  # Refill the starting bucket
                start = start_cap
                actions += 1
            elif other == other_cap:  # Empty the other bucket
                other = 0
                actions += 1
            else:  # Pour from start to other
                transfer = min(start, other_cap - other)
                start -= transfer
                other += transfer
                actions += 1

        final_amount = other if start == goal else start

        if which_bucket == "one":
            return actions, ("one" if start == goal else "two"), final_amount
        else:
            return actions, ("two" if start == goal else "one"), final_amount

    if start_bucket == "one":
        return simulate(bucket_one_capacity, bucket_two_capacity, goal, start_bucket)
    else:
        return simulate(bucket_two_capacity, bucket_one_capacity, goal, start_bucket)
