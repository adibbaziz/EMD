import numpy as np
from EMD import EMD


def generate_normal(m,mu):
	P_points = np.random.multivariate_normal(mu, np.eye(len(mu)), m)

	P_weights = np.random.uniform(low=0, high=10, size=m)

	return P_points, P_weights


def generate_mixture_gaussians(k):
	X = []
	for i in range(k):
		x,y = np.random.randint(10), np.random.randint(10)
		C,_ = generate_normal(20, [x,y])
		X += list(C)
	return np.array(X)


def compare_kmeans(C1, C2, unif):
	"""
	C1 and C2 are obtained from the attribute kmeans.labels_
	"""
	N = len(C1)
	K, J = max(C1)+1, max(C2)+1

	zeta = np.zeros((N,K))
	gamma = np.zeros((N, J))
	for i in range(N):
		zeta[i, C1[i]] = 1
		gamma[i, C2[i]] = 1
	zeta = zeta.T
	gamma = gamma.T
	if unif:
		alpha = [1./K for _ in range(K)]
		beta = [1./J for _ in range(J)]
	else:
		alpha = [len(np.where(C1 == j)[0]) for j in range(K)]
		beta = [len(np.where(C2 == j)[0]) for j in range(J)]

	# compute EMD

	d = lambda x,y: np.linalg.norm(x-y, ord=1)
	emd = EMD(zip(zeta, alpha), zip(gamma, beta), d)
	emd.write_lp_problem('emd_pb.lp')
	emd.solve_lp()
	return emd.distance








