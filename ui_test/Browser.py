from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Yolo:
    __MAP = {}

    @staticmethod
    def __get_caller():
        import threading
        return threading.current_thread()

    @staticmethod
    def get_target(target, **kwargs):
        """
        When you call Yolo.get_target() initially, the object created from the target argument gets mapped to the
        thread and then returned, any subsequent calls to Yolo
        to get the same object from the same thread will return the exact same instance of the object. However, if the
        call is made from a different thread, the object will be created again for that specific thread.
        Yolo was created to solve a primary use case for creating Page Objects so that you never have to manage and
        pass the driver instance from Page Object to Page Object. It means that you can just ask for a driver from
        any of the Page Object and be sure that a valid instance of the driver will be returned to you even when
        you are creating many instances of the same page in any of your tests and running them in parallel.
        :param target: Runnable FUNCTION/METHOD. Must returns an instance of an object when executed.
        :param kwargs: Any KWARGS that you want to pass in to your :param target: or any other properties
                       you want to support
        :return: Object created by the :param target:()
        """
        caller_thread = Yolo.__get_caller()
        if caller_thread not in Yolo.__MAP:
            Yolo.__MAP.update({caller_thread: {target: target(**kwargs)}})
        elif target not in Yolo.__MAP[caller_thread]:
            Yolo.__MAP[caller_thread].update({target: target(**kwargs)})
        return Yolo.__MAP[caller_thread][target]

    @staticmethod
    def remove_target(target):
        """
        Remove any previously mapped target
        :param target: Runnable FUNCTION/METHOD. Must returns an instance of an object when executed.
        :return: BOOLEAN, True/False depending on if the target was removed
        """
        caller_thread = Yolo.__get_caller()
        if caller_thread in Yolo.__MAP and target in Yolo.__MAP[caller_thread]:
            Yolo.__MAP[caller_thread].pop(target)
            return True
        return False


class Browser:
    @staticmethod
    def __chrome(**kwargs):
        options = webdriver.ChromeOptions()
        if kwargs.get("proxy_port"):
            options.add_argument('--proxy-server={proxy}'.format(proxy=kwargs.get("proxy_port")))
        if kwargs.get("headless"):
            options.add_argument('headless=True')
        if kwargs.get("no_sandbox"):
            options.add_argument('--no-sandbox')
        if kwargs.get("disable_shm"):
            options.add_argument('--disable-dev-shm-usage')
        if kwargs.get("disable_notifications"):
            options.add_argument('--disable-notifications')
        if kwargs.get("window_size"):
            options.add_argument('--window-size={}'.format(kwargs.get("window_size")))
        if kwargs.get("dev_tools_port"):
            options.add_argument('--remote-debugging-port={port}'.format(port=kwargs.get("dev_tools_port")))

        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        driver.set_page_load_timeout(kwargs.get("page_load_timeout", 200))
        return driver

    @staticmethod
    def get_driver(**kwargs):
        return Yolo.get_target(target=getattr(Browser, kwargs.get("target", "_Browser__chrome")),
                               freak_mode=kwargs.get("freak_mode", False),
                               **kwargs)

    @staticmethod
    def shutdown(**kwargs):
        Browser.get_driver().quit()
        Yolo.remove_target(target=getattr(Browser, kwargs.get("target", "_Browser__chrome")))

    @staticmethod
    def back():
        Browser.get_driver().back()

    @staticmethod
    def maximize():
        Browser.get_driver().maximize()

    @staticmethod
    def forward():
        Browser.get_driver().forward()

    @staticmethod
    def open_new_tab():
        Browser.get_driver().find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

    @staticmethod
    def switch_to_window(window):
        Browser.get_driver().switch_to_window(window)

    @staticmethod
    def switch_to_latest_active_window():
        windows = Browser.get_driver().window_handles
        if len(windows) == 1:
            Browser.get_driver().switch_to_window(windows[0])
            return
        for index in range(1, len(windows)):
            Browser.get_driver().switch_to_window(windows[-index])
            return

    @staticmethod
    def close_current_active_window():
        windows = Browser.get_driver().window_handles
        if len(windows) == 1:
            return
        for index in range(1, len(windows)):
            Browser.get_driver().close()
            Browser.switch_to_latest_active_window()
            return
