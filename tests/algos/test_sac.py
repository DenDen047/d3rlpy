import pytest

from skbrl.algos.sac import SAC
from tests import performance_test
from .algo_test import algo_tester, algo_update_tester, algo_pendulum_tester


@pytest.mark.parametrize('observation_shape', [(100, ), (4, 84, 84)])
@pytest.mark.parametrize('action_size', [2])
@pytest.mark.parametrize('q_func_type', ['mean', 'qr', 'iqn'])
def test_sac(observation_shape, action_size, q_func_type):
    sac = SAC(q_func_type=q_func_type)
    algo_tester(sac)
    algo_update_tester(sac, observation_shape, action_size)


@performance_test
@pytest.mark.parametrize('q_func_type', ['mean', 'qr', 'iqn'])
def test_sac_performance(q_func_type):
    if q_func_type == 'iqn':
        pytest.skip('IQN is computationally expensive')

    sac = SAC(n_epochs=5, q_func_type=q_func_type)
    algo_pendulum_tester(sac, n_trials=3)