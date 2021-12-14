from test_junkie.runner import Runner
from test.suites.NavigationSuite import NavigationSuite

runner = Runner(suites=[NavigationSuite])
runner.run(test_multithreading_limit=6, suite_multithreading_limit=2)
