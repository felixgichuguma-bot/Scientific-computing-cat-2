"""Case B (Task 3): VAT on one million retail transactions (vectorized)."""
import numpy as np

rng = np.random.default_rng(1)
gross = rng.uniform(50, 20000, 1_000_000)   # KES, VAT-inclusive
net = gross / 1.16
vat = gross - net
print(f"Total gross: KES {gross.sum():,.2f}")
print(f"Total net (ex-VAT): KES {net.sum():,.2f}")
print(f"Total VAT: KES {vat.sum():,.2f}")
print(f"VAT share of gross: {vat.sum() / gross.sum():.4%}")
