# Using a 1D heat transfer model to practice ML

Current step: Making a simulation of heat transfer for a 1D metal rod using the Forward-Time Centred-Space method on the PDE. This is using an array of values that develop over time due to initial and boundary conditions of the rod.
For this step my reading has been:
- [text](https://ocw.mit.edu/courses/18-303-linear-partial-differential-equations-fall-2006/d11b374a85c3fde55ec971fe587f8a50_heateqni.pdf)
    Taught me the Heat equation
- [text](https://nu-cem.github.io/Computational_Physics/notebooks/FTCS_method.html) 
    Taught me what FTCS is and how to build it, though I made sure to write all the code myself and not use theirs so that I woulc understand it better while debugging
    - From this, I understand how numpy array manipulation can do pretty powerful things in a single line, literally the whole FTCS loop at once.
