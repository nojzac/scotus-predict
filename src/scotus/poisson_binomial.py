import numpy as np

def poisson_binomial_pmf(probs, k):
    def C():
        return np.exp(2.j*np.pi/(len(probs)+1))
    p = 0.
    for l in range(0, len(probs)+1):
        p += (C()**(-l*k))*((1+(C()**l-1)*probs).prod())
    p /= (len(probs)+1)
    return np.real(p)

def poisson_binomial_cdf(probs, k):
    cumulative_sum = 0.0
    for i in range(0, k+1):
        cumulative_sum += poisson_binomial_pmf(probs, i)
    return cumulative_sum

if __name__ == '__main__':
    probs = np.array([.5, .5, .5])
    print poisson_binomial_cdf(probs, 3)