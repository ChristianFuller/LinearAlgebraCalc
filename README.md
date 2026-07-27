# Linear Calculator

A command-line linear algebra calculator written in Python.

This project includes multiple tools for common linear algebra tasks:
- Determinants (2x2, 3x3, 4x4)
- Matrix inverse (currently supports selected sizes)
- Vector projection, magnitude, dot product, and angle
- Orthogonal vector helper (3D)
- Matrix transformations (scale, skew/shear, rotation, orthographic projection/reflection)
- Matrix multiplication and transformation composition
- Basic eigenvalue/eigenvector workflow for 2x2 matrices

## Requirements

- Python 3.10+ (Python 3.x should work)
- matplotlib

## How To Start

No virtual environment is required.

1. Open a terminal in this project folder.
2. Install matplotlib:

	pip install matplotlib

3. Run the app:

	python MainApp.py

If your system uses py instead of python, use:

py MainApp.py

## How It Works

When you run MainApp.py, you get a main menu:
1. Determinant Calculator
2. Projection Calculator
3. Transformation Calculator
4. Eigenthings Calculator
5. Quit

Choose a section, then follow the prompts to enter matrix/vector values.

## Project Files (Quick Guide)

- MainApp.py: Entry point and top-level menu
- Calculator.py: Main feature routing and menu logic
- Determinite.py, Inverse.py: Determinants and inverse support
- projection.py, dot_product.py, magnitude.py, angle.py, v_s.py, threeD_shortcut.py: Vector operations
- rotation.py, scale_matrix.py, skew.py, orthographic_projection.py, mutiply_matrix.py: Matrix transformations
- eigenthings.py: Eigenvalue/eigenvector helper logic
- plot_vectors.py: 2D and 3D plotting utilities
- Vector_to_ArrayMatrix.py: Matrix/vector conversion helpers

## Notes

- Inputs are interactive and mostly numeric.
- Some features are partially implemented or limited to specific matrix sizes.
- Spelling in some filenames/functions is kept as-is to match the current codebase.
