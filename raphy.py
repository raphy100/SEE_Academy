import cmath  # To handle complex square roots

# Step 1: Get coefficients from user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Step 2: Calculate the discriminant
discriminant = cmath.sqrt(b**2 - 4*a*c)

# Step 3: Calculate two solutions
x1 = (-b + discriminant) / (2*a)
x2 = (-b - discriminant) / (2*a)

# Step 4: Print the results
print("The solutions to the quadratic equation are:")
print(f"x₁ = {x1}")
print(f"x₂ = {x2}")
