import matplotlib.pyplot as plt

from merton import *
S = 100     # current stock price
K = 110
T = 1   # time to maturity
r = 0.05    # risk free rate
sigma = 0.15    # annaul standard deviation , for weiner process

m = -1.08   # meean of jump size
v = 0.4     # standard deviation of jump
lam = 0.1   # intensity of jump i.e. number of jumps per annum
steps = 100     # time steps
Npaths = 200     # number of paths to simulate


np.random.seed(3)
j = merton_jump_paths(S, T, r, sigma, lam, m, v, steps, Npaths) #generate jump diffusion paths

mcprice = np.maximum(j[-1]-K,0).mean() * np.exp(-r*T) # calculate value of call

cf_price =  merton_jump_call(S, K, T, r, sigma, np.exp(m+v**2*0.5) , v, lam)

print('Merton Price =', cf_price)
print('Monte Carlo Merton Price =', mcprice)
print('Black Scholes Price =', BS_CALL(S,K,T,r, sigma))
# Merton Price = 6.61603600280417
# Monte Carlo Merton Price = 8.817532208920749
# Black Scholes Price = 4.075865972892551

j = merton_jump_paths(S, T, r, sigma, lam, m, v, steps, Npaths)
plt.plot(j)
plt.xlabel('Days')
plt.ylabel('Stock Price')
plt.title('Jump Diffusion Process')
plt.show()