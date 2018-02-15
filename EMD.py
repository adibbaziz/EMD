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
		self.P = P
		self.Q = Q
		self.WP = sum([v for (_, v) in self.P])
		self.WQ = sum([w for (_, w) in self.Q])
		self.D = np.array([[d(np.array(p),np.array(q)) for (q,_) in Q] for (p,_) in P])

	def write_lp_problem():
		emd_lp = lpsolve('make_lp', 0, len(emd.D.flatten()))
		lpsolve('set_verbose', emd_lp, IMPORTANT)
		lpsolve('set_obj_fn', emd_lp, list(emd.D.flatten()))
		for i in range(len(emd.P)):
		    for j in range(len(emd.Q)):
		        Eij = np.zeros((len(emd.P),len(emd.Q)))
		        Eij[i,j] += 1
		        lpsolve('add_constraint', emd_lp, list(Eij.flatten()), GE, 0)
		for i in range(len(emd.P)):
		    Ei = np.zeros((len(emd.P),len(emd.Q)))
		    Ei[i,:] += 1
		    lpsolve('add_constraint', emd_lp, list(Ei.flatten()), LE, emd.P[i][1])
		for j in range(len(emd.Q)):
		    Ej = np.zeros((len(emd.P),len(emd.Q)))
		    Ej[:,j] += 1
		    lpsolve('add_constraint', emd_lp, list(Ej.flatten()), LE, emd.Q[j][1])
		lpsolve('add_constraint', emd_lp, list(np.ones((len(emd.P), len(emd.Q))).flatten()), EQ, min(emd.WP, emd.WQ))
		lpsolve('write_lp', emd_lp, 'emd_pb.lp')