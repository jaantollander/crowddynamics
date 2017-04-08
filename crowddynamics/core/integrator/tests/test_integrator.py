import pytest
from hypothesis import given, assume

from crowddynamics.core.integrator import adaptive_timestep, \
    euler_integration, velocity_verlet
from crowddynamics.testing import real


@given(dt_min=real(min_value=0, max_value=10.0, exclude_zero='near'),
       dt_max=real(min_value=0, max_value=10.0, exclude_zero='near'))
def test_adaptive_timestep1(agents_circular, dt_min, dt_max):
    assume(0 < dt_min < dt_max)
    dt = adaptive_timestep(agents_circular.array, dt_min, dt_max)
    assert 0 < dt_min <= dt <= dt_max


@given(dt_min=real(min_value=0, max_value=10.0, exclude_zero='near'),
       dt_max=real(min_value=0, max_value=10.0, exclude_zero='near'))
def test_adaptive_timestep2(agents_three_circle, dt_min, dt_max):
    assume(0 < dt_min < dt_max)
    dt = adaptive_timestep(agents_three_circle.array, dt_min, dt_max)
    assert 0 < dt_min <= dt <= dt_max


@given(dt_min=real(min_value=0, max_value=10.0, exclude_zero='near'),
       dt_max=real(min_value=0, max_value=10.0, exclude_zero='near'))
def test_euler_integration1(agents_circular, dt_min, dt_max):
    assume(0 < dt_min < dt_max)
    dt = euler_integration(agents_circular.array, dt_min, dt_max)
    assert 0 < dt_min <= dt <= dt_max


@given(dt_min=real(min_value=0, max_value=10.0, exclude_zero='near'),
       dt_max=real(min_value=0, max_value=10.0, exclude_zero='near'))
def test_euler_integration2(agents_three_circle, dt_min, dt_max):
    assume(0 < dt_min < dt_max)
    dt = euler_integration(agents_three_circle.array, dt_min, dt_max)
    assert 0 < dt_min <= dt <= dt_max


@pytest.mark.skip
@given(dt_min=real(min_value=0, max_value=10.0),
       dt_max=real(min_value=0, max_value=10.0))
def test_velocity_verlet(agents, dt_min, dt_max):
    assume(0 < dt_min < dt_max)
    integrator = velocity_verlet(agents, dt_min, dt_max)
    for _, dt in zip(range(10), integrator):
        assert 0 < dt_min <= dt <= dt_max
