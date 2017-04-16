import numba
import numpy as np
from numba import f8, void, typeof

from crowddynamics.core.structures.agents import agent_type_three_circle, \
    agent_type_circular, shoulders, front
from crowddynamics.core.vector.vector2D import wrap_to_pi, length


@numba.jit([f8(typeof(agent_type_circular)[:], f8, f8),
            f8(typeof(agent_type_three_circle)[:], f8, f8)],
           nopython=True, nogil=True, cache=True)
def adaptive_timestep(agents, dt_min, dt_max):
    r"""
    Timestep is selected from interval :math:`[\Delta t_{min}, \Delta t_{max}]`
    by bounding the maximum step size :math:`\Delta x` an agent can take per
    iteration cycle, obtained from

    .. math::
       \Delta x = c \Delta t_{max} \max_{i\in A} v_i^0 \\

    where

    - :math:`c > 0` is scaling coefficient
    - :math:`v_i^0` is agent's target velocity
    - :math:`\max_{i\in A} v_i^0` is the maximum of all target velocities

    Timestep is then obtained from

    .. math::
       \Delta t_{mid} &= \frac{\Delta x}{\max_{i \in A} v_i} \\
       \Delta t &=
       \begin{cases}
       \Delta t_{min} & \Delta t_{mid} < \Delta t_{min} \\
       \Delta t_{mid} &  \\
       \Delta t_{max} & \Delta t_{mid} > \Delta t_{max} \\
       \end{cases}

    where

    - :math:`v_i` is agent's current velocity


    Args:
        dt_min:
            Minimum timestep :math:`\Delta x_{min}` for adaptive integration.

        dt_max:
            Maximum timestep :math:`\Delta x_{max}` for adaptive integration.

        velocity:

        target_velocity:

    Returns:
        float:

    References

    https://en.wikipedia.org/wiki/Adaptive_stepsize
    """
    v_max = 0.0
    for agent in agents:
        l = length(agent['velocity'])
        if l > v_max:
            v_max = l

    if v_max == 0.0:
        return dt_max
    c = 1.1
    dx_max = c * np.max(agents[:]['target_velocity']) * dt_max
    dt = dx_max / v_max
    if dt > dt_max:
        return dt_max
    elif dt < dt_min:
        return dt_min
    else:
        return dt


@numba.jit([void(typeof(agent_type_circular)[:], f8),
            void(typeof(agent_type_three_circle)[:], f8)],
           nopython=True, nogil=True, cache=True)
def translational_euler(agents, dt):
    """Update translational motion using Eulers's method"""
    for agent in agents:
        acceleration = agent['force'] / agent['mass']
        agent['position'][:] += agent['velocity'] * dt + \
                                acceleration / 2 * dt ** 2
        agent['velocity'][:] += acceleration * dt


@numba.jit(void(typeof(agent_type_three_circle)[:], f8),
           nopython=True, nogil=True, cache=True)
def rotational_euler(agents, dt):
    """Update rotational motion using Euler's method"""
    for agent in agents:
        angular_acceleration = agent['torque'] / agent['inertia_rot']
        agent['orientation'] += agent['angular_velocity'] * dt + \
                                angular_acceleration / 2 * dt ** 2
        agent['angular_velocity'] += angular_acceleration * dt
        agent['orientation'] = wrap_to_pi(agent['orientation'])
    shoulders(agents)
    front(agents)


def euler_integration(agents, dt_min, dt_max):
    r"""
    Differential system is integrated using numerical integration scheme using
    discrete adaptive timestep :math:`\Delta t`.

    Acceleration on an agent

    .. math::
       a_{k} &= \mathbf{f}_{k} / m \\
       \mathbf{x}_{k+1} &= \mathbf{x}_{k} + \mathbf{v}_{k} \Delta t + \frac{1}{2} a_{k} \Delta t^{2} \\
       \mathbf{v}_{k+1} &= \mathbf{v}_{k} + a_{k} \Delta t \\

    Angular acceleration

    .. math::
       \alpha_{k} &= M_{k} / I \\
       \varphi_{k+1} &= \varphi_{k} + \omega_{k} \Delta t + \frac{1}{2} \alpha_{k} \Delta t^{2} \\
       \omega_{k+1} &= \omega_{k} + \alpha_{k} \Delta t \\

    Args:
        agents (Agent):

        dt_min (float):
            Minimum timestep :math:`\Delta x_{min}` for adaptive integration.

        dt_max (float):
            Maximum timestep :math:`\Delta x_{max}` for adaptive integration.

    Returns:
        float: Timestep :math:`\Delta t` that was used for integration.

    """
    dt = adaptive_timestep(agents, dt_min, dt_max)
    translational_euler(agents, dt)
    if agents.dtype is agent_type_three_circle:
        rotational_euler(agents, dt)
    return dt


def translational_verlet(agents, dt):
    """Translational motion using velocity verlet method"""
    for agent in agents:
        old_acceleration = agent['force_prev'] / agent['mass']
        new_acceleration = agent['force'] / agent['mass']
        agents['velocity'] += (old_acceleration + new_acceleration) / 2 * dt
        agents['position'] += agents['velocity'] * dt + \
                              new_acceleration / 2 * dt ** 2

        # save old force for next iteration
        agent['force_prev'] = agent['force']


def velocity_verlet(agents, dt_min, dt_max):
    r"""Velocity verlet

    .. math::
        \mathbf{v}_{k+1/2} &= \mathbf{v}_{k} + \frac{1}{2} a_{k} \Delta t \\
        \mathbf{x}_{k+1} &= \mathbf{x}_{k} + \mathbf{v}_{k+1/2} \Delta t \\
        a_{k+1} &= \mathbf{f}_{k+1} / m \\
        \mathbf{v}_{k+1} &= \mathbf{v}_{k+1/2} + \frac{1}{2} a_{k+1} \Delta t

    Args:
        agents (Agent):

        dt_min (float):
            Minimum timestep :math:`\Delta x_{min}` for adaptive integration.

        dt_max (float):
            Maximum timestep :math:`\Delta x_{max}` for adaptive integration.

    Yields:
        float: Timestep :math:`\Delta t` that was used for integration.

    References
        - https://en.wikipedia.org/wiki/Verlet_integration#Velocity_Verlet
    """
    dt = adaptive_timestep(agents, dt_min, dt_max)
    translational_euler(agents, dt)

    for agent in agents:
        agent['force_prev'][:] = agent['force'][:]

    yield dt

    while True:
        dt = adaptive_timestep(dt_min, dt_max, agents['velocity'], agents['target_velocity'])
        translational_verlet(agents, dt)
        yield dt
