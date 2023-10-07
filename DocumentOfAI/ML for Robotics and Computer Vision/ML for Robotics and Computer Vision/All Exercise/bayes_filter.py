import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec


def normal_pdf(x, mu, var):
    return np.exp(-0.5 * (x-mu)**2 / var) /  np.sqrt(2*np.pi*var)


def arbitrary_action_pdf(x, x_prev, v, dt, var_action):
    mu_action = x_prev + v*dt
    return normal_pdf(x, mu_action, var_action)


def arbitrary_measurement_pdf(x, mu, var_sensor):
    return normal_pdf(x, mu, var_sensor)


def my_subplot(x, y, color, legend, ylabel, gs, sp_iter):
    fig = plt.figure(1)
    ax = fig.add_subplot(gs[sp_iter.__next__()])
    ax.plot(x, y, lw=2, color=color, label=legend)
    plt.legend()
    plt.ylabel(ylabel)
    plt.draw()
    return ax


def main():
    x_start, x_end, num_points = 0, 5, 200
    x_space = np.linspace(x_start, x_end, num_points)
    dx = (x_space[-1] - x_space[0]) / len(x_space)

    z = np.array([1.2, 1.6, 2.5])
    sigma_sensor, sigma_action = 0.3, 0.1
    var_sensor, var_action = sigma_sensor**2, sigma_action**2
    velocity = 1

    t_start, t_end, dt = 1, 3, 1
    time_steps = range(t_start, t_end+1, dt)
    belief = np.zeros_like(x_space)

    # We know that x=0 at time t=0
    x_known = 0
    idx_0 = int((x_known - x_start) / dx)
    belief[idx_0] = 1/dx  
    
    # Initialize plots
    np.set_printoptions(precision=4, suppress=True)
    fig = plt.figure(1)
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.title('Markov Localization with Bayes Filter', fontsize=18, fontweight='bold')
    plt.xlim(x_start, x_end)
    num_subplots = len(time_steps) * 3 + 1
    sp_iter = iter(range(num_subplots))
    gs = gridspec.GridSpec(nrows=num_subplots, ncols=1)
    
    my_subplot(x_space, belief, 'b', 'initial belief', 'bel(x0)', gs, sp_iter)

    for t in time_steps:
        belief_prev = belief  # Save previous belief
        belief_after_action = np.zeros_like(belief)

        # Action update (prediction) - convolution
        for i_x, x in enumerate(x_space):
            p_move = [arbitrary_action_pdf(x, x_prev, velocity, dt, var_action) for x_prev in x_space]
            belief_after_action[i_x] = np.dot(p_move, belief_prev)

        belief = belief_after_action
        my_subplot(x_space, belief, 'm', 'prior belief', 'bel~(x%d)' % t, gs, sp_iter)

        # Sensor update (correction)
        p_sense = [arbitrary_measurement_pdf(x_cur, z[t-1], var_sensor) for x_cur in x_space] # 1 x num_states
        belief = p_sense * belief

        my_subplot(x_space, p_sense, 'g', 'sensor measurement', 'p(z%d|x%d)' % (t,t), gs, sp_iter)

        # Normalize
        η = 1/sum(belief)
        belief *= η

        my_subplot(x_space, belief, 'b', 'posterior belief', 'bel(x%d)' % t, gs, sp_iter)


    location_mean = np.dot(belief, x_space)
    variances = (x_space - location_mean)**2
    location_variance = np.dot(belief, variances)
    location_std = np.sqrt(location_variance)

    print('The mean and variance of the belief are %.4f and %.4f respectively.' % (location_mean,
                                                                            location_variance))
    plt.minorticks_on()
    plt.show()

    
if __name__ == "__main__":
    main()