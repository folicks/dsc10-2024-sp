test = {   'name': 'q1_6',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> len(model_proportions) == 2\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(np.unique(model_proportions)) == 1 and sum(model_proportions) == 1\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> 0 <= one_simulated_test_stat <= 0.2\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(one_simulated_test_stat, np.abs(0.5 - simulation_proportion))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
