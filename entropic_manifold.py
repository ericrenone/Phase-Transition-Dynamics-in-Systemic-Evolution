import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import cm
from scipy.stats import entropy

# ────────────────────────────────────────────────
# 1. Configuration & Canonical Setup
# ────────────────────────────────────────────────
np.random.seed(42)
N = 12  # Number of semantic concepts
iterations = 100
gamma = 0.15 # Learning rate
beta = 0.85  # Gating bottleneck

concepts = [
    "Intelligence", "Entropy", "Manifold", "Curvature", 
    "Inference", "Substrate", "Gating", "Symmetry",
    "Topology", "Evolution", "Logic", "Information"
]

# State Initializations
S1 = np.random.dirichlet(np.ones(N)) # Inference Primitive
S2 = np.random.dirichlet(np.ones(N)) # Persistence Substrate
latent_coords = np.random.randn(N, 2) * 0.3

# ────────────────────────────────────────────────
# 2. Mathematical Engines
# ────────────────────────────────────────────────
def expmap0(v):
    v_norm = np.linalg.norm(v, axis=-1, keepdims=True)
    return np.tanh(v_norm) * v / (v_norm + 1e-15)

def canonical_step(s1, s2):
    # Phase Alpha: Entropy-driven inference
    h = entropy(s1)
    grad_h = -np.log(s1 + 1e-12) - h
    s1_new = np.clip(s1 + gamma * grad_h, 1e-12, None)
    s1_new /= s1_new.sum()
    
    # Phase Beta: Relaxation and Gating
    transported = np.sqrt(s2) * (s1_new / (np.sqrt(s1_new) + 1e-12))
    gated = transported**beta
    s2_new = s2 + gamma * (gated/gated.sum() - s2)
    s2_new /= s2_new.sum()
    
    return s1_new, s2_new

# ────────────────────────────────────────────────
# 3. Integrated Real-Time Simulation
# ────────────────────────────────────────────────
fig = plt.figure(figsize=(16, 9), facecolor='#0a0a0a')
ax_map = plt.subplot2grid((2, 2), (0, 0), rowspan=2, facecolor='#0a0a0a')
ax_ent = plt.subplot2grid((2, 2), (0, 1), facecolor='#0a0a0a')
ax_sys = plt.subplot2grid((2, 2), (1, 1), facecolor='#0a0a0a')

# Setup Manifold UI
ax_map.add_artist(plt.Circle((0, 0), 1, color='#1a1a1a', fill=True))
ax_map.add_artist(plt.Circle((0, 0), 1, color='#00ffcc', fill=False, ls='--', alpha=0.3))
sc = ax_map.scatter([], [], s=[], c=[], cmap='magma', edgecolors='white', zorder=3)
ax_map.set_xlim(-1.1, 1.1); ax_map.set_ylim(-1.1, 1.1); ax_map.axis('off')

# Setup Entropy UI
ent_line, = ax_ent.plot([], [], color='#00ffcc', label='S1 Entropy (Inference)')
ax_ent.set_title("Information Dynamics", color='white')
ax_ent.set_xlim(0, iterations); ax_ent.set_ylim(1.5, 3.0)
ax_ent.tick_params(colors='white')

# Data History
h_s1_ent = []

def update(frame):
    global S1, S2, latent_coords
    
    # Evolve the System
    S1, S2 = canonical_step(S1, S2)
    h_s1_ent.append(entropy(S1))
    
    # Map to Hyperbolic Space
    # We use S2 (Persistence) to drive the "spread" of the concepts
    expansion = 1.0 + (frame / iterations) 
    hyp_pos = expmap0(latent_coords * expansion)
    
    # Update Manifold Visuals
    sc.set_offsets(hyp_pos)
    sc.set_array(S1) # Color determined by current inference focus
    sc.set_sizes(S2 * 5000) # Size determined by substrate persistence
    
    # Update Entropy Plot
    ent_line.set_data(range(len(h_s1_ent)), h_s1_ent)
    
    return sc, ent_line

ani = FuncAnimation(fig, update, frames=iterations, interval=50, blit=True)
plt.tight_layout()
plt.show()