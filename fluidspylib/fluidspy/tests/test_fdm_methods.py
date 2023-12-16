import os
import numpy as np
from matplotlib import animation, pyplot as plt
from fluidspy.numerical.pde.fem import Explicit

METHODS_TO_BE_TESTED = set(["ftcs", "btcs"])

VALIDATION_DIR = set(os.listdir("fluidspylib/fluidspy/tests/validations"))

FILTER_METHODS = set(METHODS_TO_BE_TESTED - VALIDATION_DIR)


def animate_solution(method, states_matrix):
    fig, ax = plt.subplots()
    scat = ax.scatter(np.arange(len(states_matrix[0])), states_matrix[0], c="b", s=10)

    def update(frame):
        scat.set_offsets(np.column_stack((np.arange(len(states_matrix[frame])), states_matrix[frame])))
        return (scat,)

    ani = animation.FuncAnimation(fig, update, frames=len(states_matrix), interval=100, repeat=False)
    ani.save(f"fluidspylib/fluidspy/tests/validations/{method}.gif", writer="pillow", fps=1000)


def run_method_to_be_checked(method):
    explicit = Explicit(logging=False)
    initial_state = [6, 5, 5, -5, -6]

    delta_t, delta_x = 0.01, 0.01
    step = [delta_t, delta_x]
    alpha, num_steps = 33e-6, 1000
    solution = explicit(method, num_steps, initial_state, step, alpha)
    animate_solution(method, solution)


run_method_to_be_checked("ftcs")
