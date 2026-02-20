import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_matrix(d1, d2=None, hover=False):
    def validate(d):
        if len(d) not in [2, 3]:
            raise ValueError(
            "Matrix must be 2×n or 3×n."
            )
        n = len(d[0])
        for row in d:
            if len(row) != n:
                raise ValueError(
                "All rows must have same length."
                )
        return len(d), n

    dim1, n1 = validate(d1)
    if dim1 is None: return

    if d2 is not None:
        dim2, n2 = validate(d2)
        if dim2 is None or dim1 != dim2:
            print("Both matrices must have same dimension.")
            return

    # ---------- 2D ----------
    if dim1 == 2:
        plt.figure()
        x1, y1 = d1[0], d1[1]

        # Insert origin between points if there are at least 2 points
        plot_x1 = [x1[0], 0, x1[1]] if len(x1) >= 2 else x1
        plot_y1 = [y1[0], 0, y1[1]] if len(y1) >= 2 else y1

        # Small offset so lines/points on axes are visible
        epsilon = 0.005
        plot_x1 = [x + epsilon if x == 0 else x for x in plot_x1]
        plot_y1 = [y + epsilon if y == 0 else y for y in plot_y1]

        plt.plot(plot_x1, plot_y1, marker='o', color='magenta', alpha=0.8, label='New')

        max_val = max(max(map(abs, plot_x1)), max(map(abs, plot_y1)))
        if d2 is not None:
            x2, y2 = d2[0], d2[1]
            # Insert origin between points for d2 (same logic as d1)
            plot_x2 = [x2[0], 0, x2[1]] if len(x2) >= 2 else x2
            plot_y2 = [y2[0], 0, y2[1]] if len(y2) >= 2 else y2

            # Apply same offset for visibility
            plot_x2 = [x + epsilon if x == 0 else x for x in plot_x2]
            plot_y2 = [y + epsilon if y == 0 else y for y in plot_y2]

            # Use the new arrays when plotting!
            plt.plot(plot_x2, plot_y2, marker='o', color='red', alpha=0.5, label='Old')
            max_val = max(max_val, max(map(abs, plot_x2)), max(map(abs, plot_y2)))

        # Axes and origin
        plt.axhline(0, color='black', linewidth=1, alpha=0.5, linestyle='-')
        plt.axvline(0, color='black', linewidth=1, alpha=0.5, linestyle='-')
        plt.scatter(0, 0, color='pink', s=100, zorder=5)
        plt.gca().set_aspect('equal')
        plt.xlim(-max_val, max_val)
        plt.ylim(-max_val, max_val)
        plt.grid(True, color='gray', linestyle='--', linewidth=1, alpha=0.3)
        plt.legend()

        # Label points with rounding
        for xi, yi in zip(x1, y1):
            plt.text(xi, yi, f"({round(xi,3)},{round(yi,3)})", color='black', fontsize=9)
        if d2 is not None:
            for xi, yi in zip(x2, y2):
                plt.text(xi, yi, f"({round(xi,3)},{round(yi,3)})", color='darkred', fontsize=9)

        plt.show()

    # ---------- 3D ----------
    else:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x1, y1, z1 = d1[0], d1[1], d1[2]
        ax.plot(x1, y1, z1, marker='o', color='yellow', alpha=0.4, label='Old')

        max_val = max(max(map(abs, x1)), max(map(abs, y1)), max(map(abs, z1)))
        if d2 is not None:
            x2, y2, z2 = d2[0], d2[1], d2[2]
            ax.plot(x2, y2, z2, marker='o', color='magenta',alpha=0.8, label='New')
            max_val = max(max_val, max(map(abs, x2)), max(map(abs, y2)), max(map(abs, z2)))
        max_val += 1

        ax.set_xlim([-max_val, max_val])
        ax.set_ylim([-max_val, max_val])
        ax.set_zlim([-max_val, max_val])

        # Origin
        ax.scatter(0, 0, 0, color='pink', s=150)

        # Draw X, Y, Z axes
        ax.quiver(0, 0, 0, 1, 0, 0, color='red', length=max_val, arrow_length_ratio=0.05, linewidth=2, alpha=0.2)
        ax.quiver(0, 0, 0, 0, 1, 0, color='green', length=max_val, arrow_length_ratio=0.05, linewidth=2, alpha=0.2)
        ax.quiver(0, 0, 0, 0, 0, 1, color='blue', length=max_val, arrow_length_ratio=0.05, linewidth=2, alpha=0.2)

        # Label axes
        ax.text(max_val, 0, 0, "X", color='red', fontsize=12, alpha=0.2)
        ax.text(0, max_val, 0, "Y", color='green', fontsize=12, alpha=0.2)
        ax.text(0, 0, max_val, "Z", color='blue', fontsize=12, alpha=0.2)

        plt.legend()
        # Label points with rounding
        for xi, yi, zi in zip(x1, y1, z1):
            ax.text(xi, yi, zi, f"({round(xi,3)},{round(yi,3)},{round(zi,3)})", color='black', fontsize=9)
        if d2 is not None:
            for xi, yi, zi in zip(x2, y2, z2):
                ax.text(xi, yi, zi, f"({round(xi,3)},{round(yi,3)},{round(zi,3)})", color='darkred', fontsize=9)

        plt.show()