"""
This class implements the computation of the Earth mover's distance
given two sets of weighted points
P = [(p_i, v_i) for i in range(m)]
Q = [(q_j, w_j) for j in range(n)]
"""


import numpy as np




class EMD():

	def __init__(self, P, Q, d):
		self.P = P
		self.Q = Q
		self.WP = sum([v for (_, v) in self.P])
		self.WQ = sum([w for (_, w) in self.Q])
		self.D = np.array([[d(np.array(p),np.array(q)) for (q,_) in Q] for (p,_) in P])