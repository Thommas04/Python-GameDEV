def linear_scaling(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


print(linear_scaling(50, 0, 200, 0.66, 0.9))
print(linear_scaling(55, 0, 200, 0.66, 0.9))
