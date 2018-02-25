import numpy as np
from EMD import EMD


def generate_normal(m,mu):
	P_points = np.random.multivariate_normal(mu, np.eye(len(mu)), m)

	P_weights = np.random.uniform(low=0, high=10, size=m)

	return P_points, P_weights


def generate_mixture_gaussians(m):
	


def compare_clusterings(C1, C2):
	d = lambda x,y: np.linalg.norm(x-y, ord=1)

	
