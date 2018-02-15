import numpy as np
from EMD import EMD


def generate_normal(m,n,mu1, mu2):
	P_points = np.random.multivariate_normal(mu1, np.eye(len(mu1)), m)
	Q_points = np.random.multivariate_normal(mu1, np.eye(len(mu2)), n)

	P_weights = np.random.uniform(low=0, high=10, size=m)
	Q_weights = np.random.uniform(low=0, high=10, size=n)

	P = zip(P_points, P_weights)
	Q = zip(Q_points, Q_weights)

	return (P,Q)


def compare_clusterings(C1, C2):
	d = lambda x,y: np.linalg.norm(x-y, ord=1)

	
