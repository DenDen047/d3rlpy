# d3rlpy: A data-driven deep reinforcement learning library as an out-of-the-box tool

[![PyPI version](https://badge.fury.io/py/d3rlpy.svg)](https://badge.fury.io/py/d3rlpy)
![format check](https://github.com/takuseno/d3rlpy/workflows/format%20check/badge.svg)
![test](https://github.com/takuseno/d3rlpy/workflows/test/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/d3rlpy/badge/?version=latest)](https://d3rlpy.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/takuseno/d3rlpy/branch/master/graph/badge.svg?token=AQ02USKN6Y)](https://codecov.io/gh/takuseno/d3rlpy)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/takuseno/d3rlpy.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/takuseno/d3rlpy/context:python)
![MIT](https://img.shields.io/badge/license-MIT-blue)

d3rlpy is a data-driven deep reinforcement learning library as an out-of-the-box tool.

```py
from d3rlpy.dataset import MDPDataset
from d3rlpy.algos import CQL

# MDPDataset takes arrays of state transitions
dataset = MDPDataset(observations, actions, rewards, terminals)

# train data-driven deep RL
cql = CQL()
cql.fit(dataset.episodes)

# ready to control
actions = cql.predict(x)
```

Documentation: https://d3rlpy.readthedocs.io

Chat: [![Gitter](https://img.shields.io/gitter/room/d3rlpy/d3rlpy)](https://gitter.im/d3rlpy/d3rlpy)

## key features

### :zap: Designed for Data-Driven Deep Reinforcement Learning
d3rlpy is designed for data-driven deep reinforcement learning algorithms
where the algorithm finds the good policy within the given dataset,
which is suitable to tasks where online interaction is not feasible.
d3rlpy also supports the conventional online training paradigm to fit in with any cases.

### :beginner: Easy-To-Use API
d3rlpy provides state-of-the-art algorithms through scikit-learn style APIs
without compromising flexibility that provides detailed configurations for professional users.
Moreoever, d3rlpy is not just designed like scikit-learn, but also fully compatible with scikit-learn utilites.

### :rocket: Beyond State-Of-The-Art
d3rlpy provides further tweeks to improve performance of state-of-the-art
algorithms potentially beyond their original papers.
Therefore, d3rlpy enables every user to achieve professional-level
performance just in a few lines of codes.

## installation
```
$ pip install d3rlpy
```

## supported algorithms
| algorithm | discrete control | continuous control | data-driven RL? |
|:-|:-:|:-:|:-:|
| Behavior Cloning (supervised learning) | :white_check_mark: | :white_check_mark: | |
| [Deep Q-Network (DQN)](https://www.nature.com/articles/nature14236) | :white_check_mark: | :no_entry: | |
| [Double DQN](https://arxiv.org/abs/1509.06461) | :white_check_mark: | :no_entry: | |
| [Deep Deterministic Policy Gradients (DDPG)](https://arxiv.org/abs/1509.02971) | :no_entry: | :white_check_mark: | |
| [Twin Delayed Deep Deterministic Policy Gradients (TD3)](https://arxiv.org/abs/1802.09477) | :no_entry: | :white_check_mark: | |
| [Soft Actor-Critic (SAC)](https://arxiv.org/abs/1812.05905) | :no_entry: | :white_check_mark: | |
| [Random Ensemble Mixture (REM)](https://arxiv.org/abs/1907.04543) | :construction: | :no_entry: | :white_check_mark: |
| [Batch Constrained Q-learning (BCQ)](https://arxiv.org/abs/1812.02900) | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Bootstrapping Error Accumulation Reduction (BEAR)](https://arxiv.org/abs/1906.00949) | :no_entry: | :white_check_mark: | :white_check_mark: |
| [Advantage-Weighted Regression (AWR)](https://arxiv.org/abs/1910.00177) | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Advantage-weighted Behavior Model (ABM)](https://arxiv.org/abs/2002.08396) | :construction: | :construction: | :white_check_mark: |
| [Conservative Q-Learning (CQL)](https://arxiv.org/abs/2006.04779) (recommended) | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| [Advantage Weighted Actor-Critic (AWAC)](https://arxiv.org/abs/2006.09359) | :no_entry: | :white_check_mark: | :white_check_mark: |

## supported Q functions
- [x] standard Q function
- [x] [Quantile Regression](https://arxiv.org/abs/1710.10044)
- [x] [Implicit Quantile Network](https://arxiv.org/abs/1806.06923)
- [x] [Fully parametrized Quantile Function](https://arxiv.org/abs/1911.02140) (experimental)

## other features
Basically, all features are available with every algorithm.

- [x] evaluation metrics in a scikit-learn scorer function style
- [x] embedded preprocessors
- [x] export greedy-policy as TorchScript or ONNX
- [x] ensemble Q function with bootstrapping
- [x] [delayed policy updates](https://arxiv.org/abs/1802.09477)
- [x] parallel cross validation with multiple GPU
- [x] online training
- [x] [data augmentation](https://arxiv.org/abs/2004.13649)
- [x] [model-based algorithm](https://arxiv.org/abs/2005.13239)
- [ ] user-defined custom network

## scikit-learn compatibility
This library is designed as if born from scikit-learn.
You can fully utilize scikit-learn's utilities to increase your productivity.
```py
from sklearn.model_selection import train_test_split
from d3rlpy.metrics.scorer import td_error_scorer

train_episodes, test_episodes = train_test_split(dataset)

cql.fit(train_episodes,
        eval_episodes=test_episodes,
        scorers={'td_error': td_error_scorer})
```

You can naturally perform cross-validation.
```py
from sklearn.model_selection import cross_validate

scores = cross_validate(cql, dataset, scoring={'td_error': td_error_scorer})
```

And more.
```py
from sklearn.model_selection import GridSearchCV

gscv = GridSearchCV(estimator=cql,
                    param_grid={'actor_learning_rate': [3e-3, 3e-4, 3e-5]},
                    scoring={'td_error': td_error_scorer},
                    refit=False)
gscv.fit(train_episodes)
```

## MDPDataset
d3rlpy introduces `MDPDataset`, a convenient data structure for reinforcement
learning.
`MDPDataset` splits sequential data into transitions that includes a tuple of
data observed at `t` and `t+1`, which is usually used for training.

```py
from d3rlpy.dataset import MDPDataset

# offline data
observations = np.random.random((100000, 100)).astype('f4') # 100-dim feature observations
actions = np.random.random((100000, 4)) # 4-dim continuous actions
rewards = np.random.random(100000)
terminals = np.random.randint(2, size=100000)

# builds MDPDataset from offline data
dataset = MDPDataset(observations, actions, rewards, terminals)

# splits offline data into episodes
dataset.episodes[0].observations

# splits episodes into transitions
dataset.episodes[0].transitions[0].observation
dataset.episodes[0].transitions[0].action
dataset.episodes[0].transitions[0].next_reward
dataset.episodes[0].transitions[0].next_observation
dataset.episodes[0].transitions[0].terminal
```

`TransitionMiniBatch` is also a convenient class to make a mini-batch of
sampled transitions.
And, memory copies done in `TransitionMiniBatch` are implemented with Cython,
which provides extremely fast computation.

```py
from random import sample
from d3rlpy.dataset import TransitionMiniBatch

transitions = sample(dataset.episodes[0].transitions, 100)

# fast batching up with efficient-memory copy
batch = TransitionMiniBatch(transitions)

batch.observations.shape == (100, 100)
```

One more interesting feature in the dataset structure is that each transition
has pointers to its next and previous transition.
This feature enables JIT frame stacking just as serveral works do with Atari
tasks, which is also implemented with Cython for reducing bottlenecks.

```py
observations = np.random.randint(256, size=(100000, 1, 84, 84), dtype=np.uint8) # 1x84x84 pixel images
actions = np.random.randint(4, size=100000) # discrete actions with 4 options
rewards = np.random.random(100000)
terminals = np.random.randint(2, size=100000)

# builds MDPDataset from offline data
dataset = MDPDataset(observations, actions, rewards, terminals, discrete_action=True)

# samples transitions
transitions = sample(dataset.episodes[0].transitions, 32)

# makes mini-batch with frame stacking
batch = TransitionMiniBatch(transitions, n_frames=4)

batch.observations.shape == (32, 4, 84, 84)
```

## Docker
d3prl can be run on docker container with [nvidia-docker](https://github.com/NVIDIA/nvidia-docker).

Now use the docker command directly to build the image.
```sh
$ IMAGE_NAME="d3rlpy"
$ docker build -t ${IMAGE_NAME} "$(pwd)"/docker
```

Now run the new image and test it
```sh
$ docker run -it --rm \
             --gpus 0 \
             -v "$(pwd)":/workdir \
             -w /workdir \
             ${IMAGE_NAME} \
             /bin/bash -c "python examples/atari/train_cql.py"
```

## examples
### Atari 2600
```py
from d3rlpy.datasets import get_atari
from d3rlpy.algos import DiscreteCQL
from d3rlpy.metrics.scorer import evaluate_on_environment
from d3rlpy.metrics.scorer import discounted_sum_of_advantage_scorer
from sklearn.model_selection import train_test_split

# get data-driven RL dataset
dataset, env = get_atari('breakout-expert-v0')

# split dataset
train_episodes, test_episodes = train_test_split(dataset, test_size=0.2)

# setup algorithm
cql = DiscreteCQL(n_frames=4,
                  n_critics=3,
                  bootstrap=True,
                  q_func_type='qr',
                  scaler='pixel',
                  use_gpu=True)

# start training
cql.fit(train_episodes,
        eval_episodes=test_episodes,
        n_epochs=100,
        scorers={
            'environment': evaluate_on_environment(env),
            'advantage': discounted_sum_of_advantage_scorer
        })
```
| performance | demo |
|:-:|:-:|
|![breakout](assets/breakout.png)|![breakout](assets/breakout.gif)|

See more Atari datasets at [d4rl-atari](https://github.com/takuseno/d4rl-atari).

### PyBullet
```py
from d3rlpy.datasets import get_pybullet
from d3rlpy.algos import CQL
from d3rlpy.metrics.scorer import evaluate_on_environment
from d3rlpy.metrics.scorer import discounted_sum_of_advantage_scorer
from sklearn.model_selection import train_test_split

# get data-driven RL dataset
dataset, env = get_pybullet('hopper-bullet-mixed-v0')

# split dataset
train_episodes, test_episodes = train_test_split(dataset, test_size=0.2)

# setup algorithm
cql = CQL(actor_learning_rate=1e-3,
          critic_learning_rate=1e-3,
          temp_learning_rate=1e-3,
          alpha_learning_rate=1e-3,
          n_critics=10,
          bootstrap=True,
          update_actor_interval=2,
          q_func_type='qr',
          use_gpu=True)

# start training
cql.fit(train_episodes,
        eval_episodes=test_episodes,
        n_epochs=300,
        scorers={
            'environment': evaluate_on_environment(env),
            'advantage': discounted_sum_of_advantage_scorer
        })
```
| performance | demo |
|:-:|:-:|
|![hopper](assets/hopper.png)|![hopper](assets/hopper.gif)|


See more PyBullet datasets at [d4rl-pybullet](https://github.com/takuseno/d4rl-pybullet).

### Online Training
```py
import gym

from d3rlpy.algos import SAC
from d3rlpy.online.buffers import ReplayBuffer

# setup environment
env = gym.make('HopperBulletEnv-v0')
eval_env = gym.make('HopperBulletEnv-v0')

# setup algorithm
sac = SAC(use_gpu=True)

# setup replay buffer
buffer = ReplayBuffer(maxlen=1000000, env=env)

# start training
sac.fit_online(env, buffer, n_epochs=100, eval_env=eval_env)
```

## tutorials
Try a cartpole example on Google Colaboratory!

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/takuseno/d3rlpy/blob/master/tutorials/cartpole.ipynb)


## contributions
### coding style
This library is fully formatted with [yapf](https://github.com/google/yapf).
You can format the entire scripts as follows:
```
$ ./scripts/format
```

### test
The unit tests are provided as much as possible.
This repository is using `pytest-cov` instead of `pytest`.
You can run the entire tests as follows:
```
$ ./scripts/test
```

If you give `-p` option, the performance tests with toy tasks are also run
(this will take minutes).
```
$ ./scripts/test -p
```

## acknowledgement
This work is supported by Information-technology Promotion Agency, Japan
(IPA), Exploratory IT Human Resources Project (MITOU Program) in the fiscal
year 2020.
