# SONAR SWEEP

# Part One

input = 'data/day1_input'
measurements = [int(l.strip()) for l in open(input).readlines()]
increases = [measurements[i+1] > measurements[i] for i in range(len(measurements)-1)]
res = sum(increases)
print(res)


# Part Two

window_size = 3 # the size of the scanning window
measurement_groups = [measurements[i:i+window_size] for i in range(len(measurements)-(window_size-1))]
increases = [sum(measurement_groups[i+1]) > sum(measurement_groups[i]) for i in range(len(measurement_groups)-1)]
res = sum(increases)
print(res)