import numpy as np

def poisson_binomial_pmf(probs, k=5):
   def T(i):
       cumulative_sum = 0.
       for j in range(1, len(probs)+1):
           cumulative_sum += ((probs[j]) / (1 - probs[j]))**i
       return cumulative_sum

   p_k = (1-probs).prod # k = 0
   p_ks = [p_k]

   if k == 0:
       return p_k
   else:
       cumulative_sum = 0.
       for i in range(1, k+1):
           term = ((-1.)**(i-1))
           term *= p_ks[k-i]
           term *= T(i)
           cumulative_sum += term
       cumulative_sum /= k

def poisson_binomial_cdf(probs, k=5)
   cumulative_sum = 0.0
   for i in range(0, k+1):
       cumulative_sum += poisson_binomial_pmf(probs, i)
   return cumulative_sum