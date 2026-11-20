"""BIT 2118 - Task 2: NumPy arrays and numerical computation.

Input : 24 hourly temperatures (deg C).
Maths : mean = sum(t)/24, min, max and the vectorized conversion F = 1.8C + 32.
"""
import numpy as np

temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 20.7, 22.8, 25.0, 26.7, 28.1, 29.1,
    29.4, 29.3, 28.8, 27.8, 26.4, 24.9, 23.6, 22.4, 21.4, 20.6, 19.9, 19.3])


def summarise(temps):
    print(f"Daily mean temperature: {temps.mean():.2f} C")
    print(f"Minimum temperature: {temps.min():.2f} C")
    print(f"Maximum temperature: {temps.max():.2f} C")


print("--- Base program ---")
summarise(temperatures_c)
temperatures_f = 1.8 * temperatures_c + 32
print("First six Fahrenheit readings:", temperatures_f[:6])

print("\n--- Changed parameter: every reading raised by 5 C ---")
shifted = temperatures_c + 5
print(f"Mean after +5 C offset: {shifted.mean():.2f} C "
      f"(min {shifted.min():.2f}, max {shifted.max():.2f})")
print(f"Mean in F: {(1.8 * shifted + 32).mean():.2f} F")
