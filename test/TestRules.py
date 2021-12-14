from test_junkie.rules import Rules
from ui_test.Browser import Browser

class TestRules(Rules):
    def after_test(self, **kwargs):
        log_msgs = Browser.get_driver().get_log("browser")
        errors = []
        if log_msgs:
            for msg in log_msgs:
                errors.append(msg.get('message', None))
        if errors:
            raise AssertionError("{} Errors/Warnings in console logs :: {}".format(len(errors), errors))
        Browser.shutdown()  # moved from suite's afterTest() to here
