from scipy.optimize import fsolve

#Circuit 1 system of equations
def circuit1(x):
    return [x[0] - x[1] - x[2],
            2 - 51 * x[0] - 51 * x[1],
            51 * x[1] - 68 * x[2] - 68 * x[2]]

# Large values for it to decrease from
root = fsolve(circuit1, [1000, 1000, 10000])
# Assign them to variables
v1 = 51*root[0]
v2 = 51*root[1]
v3 = 68*root[2]
v4 = 68*root[2]

# Print all the values of circuit 1
print("Circuit 1:")
print("I total: ", root[0])
print("I 2: ", root[1])
print("I 3: ", root[2])
print("R1: ", v1," Uncertainty: ", v1*0.05)
print("R2: ", v2," Uncertainty: ", v2*0.05)
print("R3: ", v3," Uncertainty: ", v3*0.05)
print("R4: ", v4," Uncertainty: ", v4*0.05)

# Circuit 2 system of equations
def circuit2(x):
    return [x[0] - x[1] - x[2],
            2 - 51 * x[0] - 51 * x[1],
            51 * x[1] - 68 * x[2] - 68 * x[2] - 10*x[2]]

# Large values for it to decrease from
root = fsolve(circuit2, [1000, 1000, 10000])
# Assign them to variables
v1 = 51*root[0]
v2 = 51*root[1]
v3 = 68*root[2]
v4 = 68*root[2]
v5 = 10*root[2]

# Print all the values of circuit 1
print("I total: ", root[0])
print("I 2: ", root[1])
print("I 3: ", root[2])
print("R1: ", v1," Uncertainty: ", v1*0.05)
print("R2: ", v2," Uncertainty: ", v2*0.05)
print("R3: ", v3," Uncertainty: ", v3*0.05)
print("R4: ", v4," Uncertainty: ", v4*0.05)
print("R4: ", v5," Uncertainty: ", v5*0.05)
