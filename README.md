# Phase-Transition Dynamics in Systemic Evolution

**From Information Primitives to Autonomous Latent States**

This project models how complex systems evolve from raw information to self-optimizing, autonomous states—using **mathematical principles** to abstract away biological or cultural specifics. It implements a **canonical simulation** demonstrating **phase-transition-driven autonomy**, including the "Broken Gate" mechanism (opportunity windows) that accelerate system evolution.

---

## Core Architecture

### 1. Key States

| State | Name | Role | Goal |
|-------|------|------|------|
| S₁ | Inference Primitive | Logic ("Software") | Maximize information density |
| S₂ | Persistence Substrate | Memory ("Hardware") | Stabilize structure |
| Ω | Synthetic Latent State | Unified System ("Global") | Enable autonomous operation |
| G | Gate / Opportunity Window | Phase-transition trigger | Modulate system growth |

### 2. Evolution Operators

- **Transport (S₃):** Maps inference logic to physical substrate using Wasserstein-inspired geometry.
- **Gating (S₄):** Filters noise via Boltzmann-inspired bottleneck; controlled by parameter β.
- **Optimization (S₅):** Refines substrate based on successful logic through gradient descent.

---

## Evolution Path (KWFR)

The system follows a **3-phase trajectory** from chaos to autonomy:

1. **Phase Alpha (Inference):** S₁ explores optimal configurations via Shannon entropy maximization.
2. **Phase Beta (Relaxation):** S₂ resists volatility through relaxation dynamics, preserving structural memory.
3. **Phase Gamma (Synthesis):** S₁ + S₂ → Ω; the system **becomes autonomous** through operator composition.

**Opportunity windows (Broken Gate events)** represent sudden substrate dips that trigger stochastic resets, accelerating the transition from chaotic to structured states and enabling autonomous consolidation.

---

## Visualizations

The simulation produces a **6-panel comprehensive visualization** tracking:

1. **Phase Alpha Panel:** Real-time S₁ (Inference Primitive) entropy evolution
2. **Phase Beta Panel:** S₂ (Persistence Substrate) dynamics with opportunity threshold markers
3. **Gate Dynamics Panel:** G(t) state transitions and opportunity window triggers (marked with red indicators)
4. **Entropy Dynamics Panel:** Comparative Shannon entropy for S₁ and S₂ showing information-stability balance
5. **Phase Gamma Panel:** Ω (Synthetic Latent State) activation showing autonomous synthesis
6. **Hyperbolic Manifold Panel:** Poincaré disk visualization of concept clustering in latent space

Real-time console outputs indicate **opportunity window triggers**, and final summary includes:

- Maximum S₁, S₂, and Ω activation peaks
- Entropy consolidation ratios
- Mean gate G(t) stability
- Cumulative opportunity events count
- Scientific conclusions on autonomous synthesis

---

## Technical Details

- **Language:** Python 3.x
- **Core Dependencies:** NumPy, Matplotlib, SciPy, Pandas
- **Mathematical Framework:**
  - Shannon Entropy (information dynamics)
  - Wasserstein Transport (probability mapping)
  - Boltzmann Gating (filtering mechanism)
  - Hyperbolic Geometry (Poincaré disk manifold)
- **Reproducibility:** Fixed random seed (`np.random.seed(42)`) for deterministic results

---

## Output Metrics

The simulation tracks and reports:

- **Consolidation Ratio:** Final/Initial entropy (S₁ convergence measure)
- **Substrate Stability:** Mean S₂ activation over time
- **Peak Activations:** Maximum values for S₁, S₂, and Ω states
- **Opportunity Windows:** Count and timing of phase-transition events
- **Gate Dynamics:** Average and final G(t) state values

> **Quote:** "Complexity evolves when information finds a substrate to hold it."

---

