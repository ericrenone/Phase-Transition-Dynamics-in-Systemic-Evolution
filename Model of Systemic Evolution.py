#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Grand Canonical Model of Systemic Evolution
High-Fidelity Visualization & Summary
Author: Eric Ren
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy

# ================================
# CONFIGURATION
# ================================
N = 50         # Dimensionality of the system (reduced for clarity)
tau = 0.05     # Relaxation time for S2
gamma = 0.1    # Gradient step for S1 inference
beta = 0.9     # Gating bottleneck coefficient
iterations = 200

np.random.seed(42)

# ================================
# INITIAL STATES
# ================================
S1 = np.random.rand(N)
S1 /= S1.sum()

S2 = np.random.rand(N)
S2 /= S2.sum()

# ================================
# OPERATORS
# ================================
def transport(S1, S2):
    sqrt_S2 = np.sqrt(S2)
    return sqrt_S2 * (S1 / (np.sqrt(S1) + 1e-12))

def gating(S, capacity=beta):
    S_new = S ** capacity
    return S_new / S_new.sum()

def optimize(S_target, S_current, gamma=gamma):
    delta = S_target - S_current
    S_new = S_current + gamma * delta
    S_new = np.clip(S_new, 1e-12, None)
    return S_new / S_new.sum()

# ================================
# SIMULATION HISTORIES
# ================================
history_S1 = []
history_S2 = []
history_Omega = []
history_entropy_S1 = []
history_entropy_S2 = []

for t in range(iterations):
    # Phase Alpha: S1 inference updates
    H = entropy(S1)
    grad_H = -np.log(S1 + 1e-12) - H
    S1 = S1 + gamma * grad_H
    S1 = np.clip(S1, 1e-12, None)
    S1 /= S1.sum()

    # Phase Beta: S2 relaxation
    S2 = S2 + tau * (S2.mean() - S2)
    S2 = np.clip(S2, 1e-12, None)
    S2 /= S2.sum()

    # Phase Gamma: Operators
    transported = transport(S1, S2)
    gated = gating(transported, beta)
    S2 = optimize(gated, S2, gamma=gamma)

    Omega = (S1 + S2) / 2

    # Record histories
    history_S1.append(S1.copy())
    history_S2.append(S2.copy())
    history_Omega.append(Omega.copy())
    history_entropy_S1.append(entropy(S1))
    history_entropy_S2.append(entropy(S2))

history_S1 = np.array(history_S1)
history_S2 = np.array(history_S2)
history_Omega = np.array(history_Omega)
history_entropy_S1 = np.array(history_entropy_S1)
history_entropy_S2 = np.array(history_entropy_S2)

# ================================
# TRANSITION MATRIX
# ================================
transition_matrix = np.diag(history_Omega[-1] / (history_S2[-1] + 1e-12))

# ================================
# HIGH-FIDELITY MULTI-PANEL PLOT
# ================================
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# 1. S1 Evolution
for i in range(min(10, N)):
    axes[0, 0].plot(history_S1[:, i], label=f"S1_dim{i}", linestyle='--')
axes[0, 0].set_title("Phase Alpha: S1 (Inference Primitive) Evolution")
axes[0, 0].set_xlabel("Iteration")
axes[0, 0].set_ylabel("Probability / Activation")
axes[0, 0].legend(fontsize=7, loc='upper right')

# 2. S2 Evolution
for i in range(min(10, N)):
    axes[0, 1].plot(history_S2[:, i], label=f"S2_dim{i}", linestyle='-')
axes[0, 1].set_title("Phase Beta: S2 (Persistence Substrate) Evolution")
axes[0, 1].set_xlabel("Iteration")
axes[0, 1].set_ylabel("Probability / Activation")
axes[0, 1].legend(fontsize=7, loc='upper right')

# 3. Ω Evolution
for i in range(min(10, N)):
    axes[1, 0].plot(history_Omega[:, i], label=f"Ω_dim{i}", linestyle=':')
axes[1, 0].set_title("Phase Gamma: Ω (Synthetic Latent State) Evolution")
axes[1, 0].set_xlabel("Iteration")
axes[1, 0].set_ylabel("Probability / Activation")
axes[1, 0].legend(fontsize=7, loc='upper right')

# 4. Entropy Summary (Operators Effect)
axes[1, 1].plot(history_entropy_S1, label="Entropy S1 (Logic)")
axes[1, 1].plot(history_entropy_S2, label="Entropy S2 (Substrate)")
axes[1, 1].set_title("Entropy Dynamics: Information & Substrate Coherence")
axes[1, 1].set_xlabel("Iteration")
axes[1, 1].set_ylabel("Shannon Entropy")
axes[1, 1].legend(fontsize=10)

plt.tight_layout()
plt.show()

# ================================
# SUMMARY OUTPUTS
# ================================
np.set_printoptions(precision=4, suppress=True)
print("=== Canonical Transition Matrix S2 -> Ω ===")
print(transition_matrix)

print("\n=== Final System State Summary ===")
print(f"Final Entropy S1: {history_entropy_S1[-1]:.4f}")
print(f"Final Entropy S2: {history_entropy_S2[-1]:.4f}")
print(f"Max S1 Activation: {history_S1[-1].max():.4f}")
print(f"Max S2 Activation: {history_S2[-1].max():.4f}")
print(f"Max Ω Activation: {history_Omega[-1].max():.4f}")
