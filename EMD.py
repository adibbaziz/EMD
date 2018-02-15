"""
This class implements the computation of the Earth mover's distance
given two sets of weighted points
P = [(p_i, v_i) for i in range(m)]
Q = [(q_j, w_j) for j in range(n)]
"""
import numpy as np
from lpsolve55 import *

class EMD():

	def __init__(self, P, Q, d):
		self.m = len(P)
		self.n = len(Q)
		self.P = P
		self.Q = Q
		self.WP = sum([v for (_, v) in self.P])
		self.WQ = sum([w for (_, w) in self.Q])
		self.D = np.array([[d(np.array(p),np.array(q)) for (q,_) in Q] for (p,_) in P])

	def write_lp_problem(self, filename):
		self.emd_lp = lpsolve('make_lp', 0, len(self.D.flatten()))
		lpsolve('set_verbose', self.emd_lp, IMPORTANT)
		lpsolve('set_obj_fn', self.emd_lp, list(self.D.flatten()))
		for i in range(self.m):
		    for j in range(self.n):
		        Eij = np.zeros((self.m,self.n))
		        Eij[i,j] += 1
		        lpsolve('add_constraint', self.emd_lp, list(Eij.flatten()), GE, 0)
		for i in range(self.m):
		    Ei = np.zeros((self.m,self.n))
		    Ei[i,:] += 1
		    lpsolve('add_constraint', self.emd_lp, list(Ei.flatten()), LE, self.P[i][1])
		for j in range(self.n):
		    Ej = np.zeros((self.m,self.n))
		    Ej[:,j] += 1
		    lpsolve('add_constraint', self.emd_lp, list(Ej.flatten()), LE, self.Q[j][1])
		lpsolve('add_constraint', self.emd_lp, list(np.ones((self.m, self.n)).flatten()), EQ, min(self.WP, self.WQ))
		lpsolve('write_lp', self.emd_lp, filename)
		print "Done!"


	def solve_lp(self):
		lpsolve('solve', self.emd_lp)

		self.objective = lpsolve('get_objective', self.emd_lp)
		self.flow_matrix = np.array(lpsolve('get_variables', self.emd_lp)[0]).reshape((self.m, self.n))
		self.distance = self.objective/np.sum(self.flow_matrix)

