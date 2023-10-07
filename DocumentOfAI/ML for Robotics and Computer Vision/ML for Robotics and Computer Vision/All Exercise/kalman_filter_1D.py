import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

def normal_pdf(x, mu, var):
    return np.exp(-0.5 * (x-mu)**2 / var) /  np.sqrt(2*np.pi*var)


def measurement_update(mu1, var1, mu2, var2):
    new_mean = (var2*mu1 + var1*mu2) / (var1 + var2)
    new_var = 1 / (1/var1 + 1/var2)
    return new_mean, new_var


def action_update(mu1, var1, mu2, var2):
    new_mean = mu1 + mu2
    new_var = var1 + var2
    return new_mean, new_var


def my_subplot(x, y, color, legend, ylabel, gs, sp_iter):
    fig = plt.figure(1)
    ax = fig.add_subplot(gs[sp_iter.__next__()])
    ax.plot(x, y, lw=2, color=color, label=legend)
    plt.legend()
    plt.ylabel(ylabel)
    plt.draw()
    return ax


def main():
    movements = np.array([1, 1, 1])
    measurements = np.array([1.2, 1.6, 2.5])
    sigma_sensor, sigma_action = 0.3, 0.1
    var_sensor, var_action = sigma_sensor**2, sigma_action**2
    velocity, dt = 1, 1
    time_steps = range(1, 4)
    # We know that x=0 at time t=0
    x_mu, x_var = 0, 0  
    
    # Initialize plots
    np.set_printoptions(precision=4, suppress=True)
    fig = plt.figure(1)
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.title('1-D Localization with Kalman Filter', fontsize=18, fontweight='bold')
    plt.xlim(0, 5)
    num_subplots = len(time_steps) * 3 + 1
    sp_iter = iter(range(num_subplots))
    gs = gridspec.GridSpec(nrows=num_subplots, ncols=1)
    
    x_space = np.linspace(0, 5, 200)
    belief = np.zeros_like(x_space)
    dx = (x_space[-1] - x_space[0]) / len(x_space)
    belief[0] = 1 / dx
    my_subplot(x_space, belief, 'b', 'initial belief', 'bel(x0)', gs, sp_iter)
    
    for t in time_steps:
        # Action update (prediction) - convolution
        [x_mu, x_var] = action_update(x_mu, x_var, velocity*dt, var_action)
        belief = np.array( [normal_pdf(x, x_mu, x_var) for x in x_space] )
        my_subplot(x_space, belief, 'm', 'prior belief', 'bel~(x%d)' % t, gs, sp_iter)

        # Measurement update (correction)
        z = measurements[t-1]
        p_sense = np.array([normal_pdf(x, z, var_sensor) for x in x_space] )
        my_subplot(x_space, p_sense, 'g', 'sensor measurement', 'p(z%d|x%d)' % (t,t), gs, sp_iter)

        [x_mu, x_var] = measurement_update(x_mu, x_var, z, var_sensor)
        belief = np.array( [normal_pdf(x, x_mu, x_var) for x in x_space] )

        # Normalize
        η = 1/sum(belief)
        belief *= η
        ax = my_subplot(x_space, belief, 'b', 'posterior belief', 'bel(x%d)' % t, gs, sp_iter)


    print('The mean and variance of the belief are %.4f and %.4f respectively.' % (x_mu, x_var), gs, sp_iter)
    plt.minorticks_on()
    plt.show()
    
    
if __name__ == "__main__":
    main()