OK_FORMAT = True
test = {   'name': 'q1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> res_q1.shape == (9, 1)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> "group by" not in query_q1.lower()\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> sorted(list(res_q1.iloc[:,0])) == ['movie', 'short', 'tvEpisode', 'tvMiniSeries', 'tvMovie', 'tvSeries', 'tvSpecial', 'video', 'videoGame']\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
