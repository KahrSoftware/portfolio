## Electron Visualization

This is a simulation I made for a physics class project. The program creates a 3D visualization of the probability density field of a single electron around a hydrogen atom. It features several different possible configurations of the quantum numbers describing the electron's orbit, represented by functions with different versions of Schrödinger's wave equation. The program then graphs a set of randomized points corresponding to the calculated probability field. It is written in python and uses the VPython package for visuals.


This program was originally written in a Jupyter notebook over multiple cells, so the easiest user input was to simply uncomment and comment lines, selecting which function to use. Additionally, efficiency was not a major concern as I was running the program on powerful university lab computers. I did not improve the O(n<sup>3</sup>) runtime complexity as there was no need at the time of writing.

Below are some images of the visualization in several configurations.

![Screenshot1]
(EVscreenshot1.png)

![Screenshot2]
(EVscreenshot2.png)

![Screenshot3]
(EVscreenshot3.png)

To run the project:

- Ensure you have python installed.
- From the `ElectronVisualization` directory:
- Run `python ElectronVisualization.py`.
- You can uncomment one of lines 54-58 of `ElectronVisualization.py` to change the electron's orbital configuration.