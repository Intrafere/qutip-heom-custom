 
import numpy as np
from qutip import *

class HEOMSolver:
    def __init__(self, H_sys, V, rho0, bath, max_depth=3):
        self.H_sys = H_sys
        self.V = V
        self.rho0 = rho0
        self.bath = bath
        self.L = max_depth
        self.hierarchy = self._build_hierarchy()

    def _build_hierarchy(self):
        hierarchy = [self.rho0]
        for level in range(1, self.L + 1):
            hierarchy.append(Qobj(np.zeros((2, 2)), dims=[[2], [2]]))
        return hierarchy

    def evolve(self, tlist):
        results = []
        for t in tlist:
            results.append(self.hierarchy[0])  # placeholder: evolve only root
        return results
