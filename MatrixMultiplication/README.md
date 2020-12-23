## Matrix Multiplication

This directory contains a variety of neural networks which learn and classify either the XOR function or a large sudoku dataset. These programs were created as part of a project exploring different implementations of matrix operations, most notably matrix multiplication which is generally the most used and resource intensive in work with neural networks. 

There are three different schemes implemented. The first is the naive, O(n<sup>3</sup>) algorithm, written by me in `matrixmath.py`, and used in `pythonXOR.py` and `pythonSudoku.py`. The second uses matrix operations from the external Python library Numpy. Numpy's improvements come from using a low level BLAS library to optimize hardware something. See `numpyXOR.py` and `numpySudoku.py`. The third relies on NVIDIA's CUDA platforms, which allow repeated matrix multiplication to be carried out in parallel across the massive processing power of a high end GPU. I initially used TensorFlow machine learning library, but found the Keras interface easier to use. See `kerasXOR.py` and `kerasSudoku.py`.

This first graph shows time to train vs number of epochs for each of the three matrix operation systems.
![XOR Graph]
(XORGraph.png?raw=true)
This second graph shows the time per epoch vs the number of sudokus trained on. The naive python scheme has been removed for being too slow.
![Sudoku Graph]
(SudokuGraph.png?raw=true)
In the second graph, Numpy does not have a data point for size 1,000,000 dataset due to a memory overflow in the Numpy tanh function.

This set of programs were designed to run on a lab computer with a powerful GPU, and may not function correctly on all hardware. Not all of the neural nets consistently train to a level for consistent classification, as the main goal of this project was to measure training time.

To run this project:

- Ensure you have Python installed.
- Unzip `sudoku.zip` into the `MatrixMultiplication` directory.
- From the `MatrixMultiplication` directory:
- Run `python [filename].py`, where `[filename]` is any file whose name ends with `XOR.py` or `Sudoku.py`.