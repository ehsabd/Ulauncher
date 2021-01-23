import webbrowser
from ulauncher.api.shared.action.BaseAction import BaseAction
from ulauncher.utils.Settings import Settings

class OpenUrlAction(BaseAction):
    """
    Opens URL in a default browser

    :param str url:
    """

    def __init__(self, url):
        self.url = url
        self.settings = Settings.get_instance()

    def run(self):
        browser_command = self.settings.get_property('browser-command')
        webbrowser.get(browser_command).open_new_tab(self.url)
