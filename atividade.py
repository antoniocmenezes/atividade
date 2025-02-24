import sympy as sp

print('resolução numérica: ', sp.sqrt(10))


from sympy importsymbols, pprint
x,y,z = symbols('x y z')
solution = x + 2*y + z*x
pprint(solution)
solution2 = solution * x
pprint(solution2)


from sympy.abc import x, y
from sympy import solve

solution = solve(x**2 - y, x, dict=True)
pprint(solution)


from sympy import solve
from sympy.abc import x, y, z

solution = solve([x**2 + y - 2*z, y + 4*z], x, y, dict=True)
pprint(solution)


from sympy import pprint, sin, solveset
from sympy.abc import x

solution = solveset(sin(x), x)
pprint(solution)


from sympy import S, solveset
from sympy.abc import x

solveset(x**4 - 256, x, domain=S.Reals)


from sympy import *

solution = diff(sin(x) * exp(x), x)
pprint(solution)


from sympy import *

solution = integrate(sin(x**2), (x, -oo, oo))
pprint(solution)


from sympy import init_printing
init_printing(use_unicode=True)

from sympy import symbols
from sympy.matrices import Matrix

c, d, e = symbols("c, d, e")
A = Matrix([[c, d], [1, -e]])


from sympy import init_printing
init_printing(use_unicode=True)

from sympy import diff, symbols, exp

x = symbols("x")
sympy_tanh = (exp(x) - exp(-x)) / (exp(x) + exp(-x))
sympy_tanh
