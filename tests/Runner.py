from test_junkie.runner import Runner
from tests.suites.NavigationSuite import NavigationSuite

runner = Runner(suites=[NavigationSuite])
runner.run()
