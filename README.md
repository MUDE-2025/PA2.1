# Programming Assignment 2.1: A Classy PDE

*Due: Friday, November 14th.*

You can preview this assignment on https://mude.citg.tudelft.nl/workbook-2025/assignments/PA2.1/README.html. After the deadline, this link will include solutions. The preview of the assignment version is shared here: https://mude.citg.tudelft.nl/workbook-2025/no_solutions/assignments/PA2.1/README.html. You can obtain your personal repository for submission on: https://classroom.github.com/a/jogcPuwd. If you don't want to make this assignment as part of a grade, access the assignment here: https://github.com/MUDE-2025/PA2.1.

Before you can start this assignment, read the theory pages in the book chapter [Object-oriented programming](https://mude.citg.tudelft.nl/book/2025/programming/week_2_1.html):
- [Classes and Object-Oriented Programming in Python](https://mude.citg.tudelft.nl/book/2025/_git/github.com_TeachBooks_learn-programming/mude-2025/book/python/oop/intro.html)
- [What are classes?](https://mude.citg.tudelft.nl/book/2025/_git/github.com_TeachBooks_learn-programming/mude-2025/book/python/oop/classes.html)
- [Encapsulation](https://mude.citg.tudelft.nl/book/2025/_git/github.com_TeachBooks_learn-programming/mude-2025/book/python/oop/encapsulation.html)
- [Inheritance](https://mude.citg.tudelft.nl/book/2025/_git/github.com_TeachBooks_learn-programming/mude-2025/book/python/oop/Inheritance.html)
- [Polymorphism](https://mude.citg.tudelft.nl/book/2025/_git/github.com_TeachBooks_learn-programming/mude-2025/book/python/oop/Polymorphism.html)
- [Exercise](https://mude.citg.tudelft.nl/book/2025/_git/github.com_TeachBooks_learn-programming/mude-2025/book/python/oop/exercise.html)

This assignment will help you understand more about Object Oriented Programming (OOP) in Python and why OOP is an attractive programming paradigm in many applications. In Python, OOP is done through classes, so to show you how it can make you think and code differently we will **code a simple PDE solver twice, with and without OOP**.

We will be looking at a simple solver for the diffusion PDE in 1D:

$$
\frac{\partial T}{\partial t} = \kappa\frac{\partial^2 T}{\partial x^2}
$$

And use it to model heat conduction in a 1D bar of length $L$ and thermal diffusivity $\kappa$. Initially the whole bar is at a temperature $T_\mathrm{init}$ and we heat the left of the bar such that its temperature is held at a value $T_\mathrm{left}$. We also fix the heat flux at the right-end of the bar to a value $h_\mathrm{right}$. 

This can be translated to the following initial and boundary conditions:

$$
T(x,0) = T_\mathrm{init},\quad x\in[0,L]
$$

$$
T(0,t) = T_\mathrm{left},\quad t>0
$$

$$
\frac{\partial T}{\partial x}(L,t) = h_\mathrm{right},\quad t>0
$$

We will use **Finite Differences** to solve this problem for $t\in[0,t_\mathrm{end}]$ with a time step $\Delta t$. This is part of this week's content, so if you are not yet familiar with the it, the basic algorithm to obtain an approximate solution $T(x,t)$ to this problem is:

- We will solve the problem on a grid over $x$ with $M$ points and spacing $\Delta x$
- Set the initial temperature $T=T_\mathrm{init}$ at every point $m\in{1,...,M}$
- Go through each time step in sequence. 
- At time $t=(n+1)\Delta t$:, set the temperature on the left:

$$T^{n+1}_1 = T_\mathrm{left}$$

- At time $t=(n+1)\Delta t$:, at each interior point $m\in{1,...,M-1}$, set:

$$T^{n+1}_m = T^n_m + \kappa\frac{\Delta t}{\Delta x^2}\left(T^n_{m+1}-2T^n_m+T^n_{m-1}\right)$$

- At time $t=(n+1)\Delta t$:, set the flux on the right:

$$T^{n+1}_M = T^n_M + 2\kappa\frac{\Delta t}{\Delta x^2}\left(T^n_{M-1}-T^n_M+h_\mathrm{right}\Delta x\right)$$
    
- Go through every time step and return a time sequence of grid values $T(x,t)$ for plotting

You'll solve this using functional programming and objective-oriented programming in two parts:

1. [Functional programming](./1_functional.ipynb)
2. [Object-oriented programming](./2_oop.ipynb)

You pass this PA if you:
- For both your `Diffusion` as `MyDiffusion` class in the OOP part:
  - It doesn't crash during setup
  - The boundary conditions are present at step 0
  - The solver doesn't give the correct results

> By Iuri Rocha, Marcel Zijlema, Delft University of Technology. CC BY 4.0, more info [on the Credits page of Workbook](https://mude.citg.tudelft.nl/workbook-2025/credits.html).
