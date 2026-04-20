import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data = np.loadtxt('./cities.csv', delimiter=',')
K = 3

def assign_clusters(centers, data):
    dists = np.array([[np.sum((p - c)**2) for c in centers] for p in data])
    return np.argmin(dists, axis=1)

def total_sse(centers, data):
    labels = assign_clusters(centers, data)
    return sum(np.sum((data[labels == k] - centers[k])**2) for k in range(K))

def cluster_sse(centers, labels, data, K):
    return [np.sum((data[labels == k] - centers[k])**2) for k in range(K)]

def gradient_descent_kmeans(data, K, lr=0.01, n_iter=300):
    idx = np.random.choice(len(data), K, replace=False)
    centers = data[idx].astype(float).copy()
    history = []
    for _ in range(n_iter):
        labels = assign_clusters(centers, data)
        for k in range(K):
            pts = data[labels == k]
            if len(pts) == 0:
                continue
            grad = 2 * (len(pts) * centers[k] - pts.sum(axis=0))
            grad = np.clip(grad, -10, 10)
            centers[k] -= lr * grad
        history.append(total_sse(centers, data))
    labels = assign_clusters(centers, data)
    return centers, labels, history

def newton_raphson_kmeans(data, K, n_iter=100):
    idx = np.random.choice(len(data), K, replace=False)
    centers = data[idx].astype(float).copy()
    history = []
    for _ in range(n_iter):
        labels = assign_clusters(centers, data)
        for k in range(K):
            pts = data[labels == k]
            if len(pts) == 0:
                continue
            n_k = len(pts)
            g = 2 * (n_k * centers[k] - pts.sum(axis=0))
            H_inv = 1.0 / (2 * n_k)
            centers[k] = centers[k] - H_inv * g
        history.append(total_sse(centers, data))
    labels = assign_clusters(centers, data)
    return centers, labels, history

gd_centers, gd_labels, gd_history = gradient_descent_kmeans(data, K)
nr_centers, nr_labels, nr_history = newton_raphson_kmeans(data, K)

gd_sse = cluster_sse(gd_centers, gd_labels, data, K)
nr_sse = cluster_sse(nr_centers, nr_labels, data, K)

print("=== (a) Gradient Descent ===")
for k in range(K):
    print(f"  Airport {k+1}: ({gd_centers[k][0]:.4f}, {gd_centers[k][1]:.4f})  SSE={gd_sse[k]:.4f}")
print(f"  Total SSE: {sum(gd_sse):.4f}")

print("\n=== (b) Newton-Raphson ===")
for k in range(K):
    print(f"  Airport {k+1}: ({nr_centers[k][0]:.4f}, {nr_centers[k][1]:.4f})  SSE={nr_sse[k]:.4f}")
print(f"  Total SSE: {sum(nr_sse):.4f}")

# ─── COMPARISON ───────────────────────────────────────────────────────────
print("\n=== COMPARISON: GD vs Newton-Raphson ===")
print(f"{'':20s} {'GD SSE':>10} {'NR SSE':>10}")
print("-" * 42)
for k in range(K):
    print(f"  Airport {k+1}:          {gd_sse[k]:>10.4f} {nr_sse[k]:>10.4f}")
print("-" * 42)
print(f"  Total SSE:          {sum(gd_sse):>10.4f} {sum(nr_sse):>10.4f}")
print()
if sum(gd_sse) < sum(nr_sse):
    diff = sum(nr_sse) - sum(gd_sse)
    print(f"  Gradient Descent wins by {diff:.4f} SSE")
elif sum(nr_sse) < sum(gd_sse):
    diff = sum(gd_sse) - sum(nr_sse)
    print(f"  Newton-Raphson wins by {diff:.4f} SSE")
else:
    print("  Both methods give identical SSE")
print(f"  GD iterations used:  300")
print(f"  NR iterations used:  100")
print(f"  Note: SSE difference is due to different random initializations,")
print(f"        not a fundamental difference in the methods.")

colors = ['#e74c3c', '#2ecc71', '#3498db']
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle('Q1 — Airport Placement (3 Airports, Surat District)', fontsize=13, fontweight='bold')

for ax, centers, labels, sse, title in [
    (axes[0], gd_centers, gd_labels, gd_sse, '(a) Gradient Descent'),
    (axes[1], nr_centers, nr_labels, nr_sse, '(b) Newton-Raphson'),
]:
    for k in range(K):
        pts = data[labels == k]
        ax.scatter(pts[:, 0], pts[:, 1], c=colors[k], alpha=0.6, s=45, label=f'Cluster {k+1} SSE={sse[k]:.2f}')
        ax.scatter(*centers[k], c=colors[k], marker='*', s=300, edgecolors='black', linewidths=1.2, zorder=5)
        ax.annotate(f'A{k+1}', centers[k], textcoords='offset points', xytext=(5,5), fontsize=9, fontweight='bold')
    ax.set_title(f'{title}\nTotal SSE = {sum(sse):.4f}')
    ax.set_xlabel('X'); ax.set_ylabel('Y')
    ax.legend(fontsize=7.5); ax.grid(alpha=0.3)

axes[2].plot(gd_history, label=f'GD (final={gd_history[-1]:.2f})', color='#e74c3c', linewidth=1.5)
axes[2].plot(nr_history, label=f'NR (final={nr_history[-1]:.2f})', color='#3498db', linewidth=1.5)
axes[2].set_title('Convergence: Total SSE vs Iteration')
axes[2].set_xlabel('Iteration'); axes[2].set_ylabel('Total SSE')
axes[2].legend(fontsize=8); axes[2].grid(alpha=0.3)

plt.tight_layout()
plt.savefig('./q1_airports.png', dpi=150, bbox_inches='tight')
print("Saved.")