

# Mechanical Engineering Project 1
# Stress and Strain Calculator

print("STRESS AND STRAIN CALCULATOR")
print("----------------------------")

# Input values
force = float(input("Enter applied force (N): "))
area = float(input("Enter cross-sectional area (mm^2): "))
original_length = float(input("Enter original length (mm): "))
extension = float(input("Enter extension (mm): "))

# Calculate stress
stress = force / area

# Calculate strain
strain = extension / original_length

# Display results
print("\n--- RESULTS ---")
print(f"Stress = {stress:.2f} MPa")
print(f"Strain = {strain:.6f}")
print(f"Strain percentage = {strain * 100:.4f}%")

