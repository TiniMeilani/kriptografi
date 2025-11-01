# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
from collections import Counter

text = 'NVKDGZKDOCSC'
count = Counter(text)

for k, v in sorted(count.items()):
    print(f"{k}: {v/len(text):.2f}")

# %%
from collections import Counter
import matplotlib.pyplot as plt

text = 'NVKDGZKDOCSC'
count = Counter(text)
letters = sorted(count.keys())
frequencies = [count[k] / len(text) for k in letters]

plt.bar(letters, frequencies)
plt.title('Letter Frequency in Ciphertext')
plt.xlabel('Letters')
plt.ylabel('Frequency')

plt.show()
