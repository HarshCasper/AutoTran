"""
Set the desired capabilities while running the test on a remote platform
"""

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from datetime import datetime

class Remote_Options():
    "Class contains methods for various remote options for browserstack and saucelab"

    def firefox(browser_version):
        "Set web browser as firefox"

        desired_capabilities = DesiredCapabilities.FIREFOX
        desired_capabilities['browser_version'] = browser_version
        return desired_capabilities
    
    def explorer(browser_version):
        "Set web browser as Explorer"

        desired_capabilities = DesiredCapabilities.INTERNETEXPLORER
        desired_capabilities['browser_version'] = browser_version
        return desired_capabilities
    
    def chrome(browser_version):
        "Set web browser as Chrome"

        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities['browser_version'] = browser_version
        return desired_capabilities

    def opera(browser_version):
        "Set web_browser as Opera"

        desired_capabilities = DesiredCapabilities.OPERA
        desired_capabilities['browser_version'] = browser_version
        return desired_capabilities

    def safari(browser_version):
        "Set web browser as Safari"

        desired_capabilities = DesiredCapabilities.SAFARI
        desired_capabilities['browser_version'] = browser_version
        return desired_capabilities

    def edge(browser_version):
        "Set web browser as Edge"

        desired_capabilities = DesiredCapabilities.EDGE
        desired_capabilities['browser_version'] = browser_version
        return desired_capabilities

    def set_os(desired_capabilities, os_name, os_version):
        "Set os name and os_version"

        desired_capabilities['os'] = os_name
        desired_capabilities['os_version'] = os_version
        return desired_capabilities

    def remote_project_name(desired_capabilities, remote_project_name):
        "Set remote project name for browserstack"

        desired_capabilities['project'] = remote_project_name
        return desired_capabilities

    def remote_build_name(desired_capabilities, remote_build_name):
        "Set remote build name for browserstack"

        desired_capabilities['build'] = remote_build_name+"_"+str(datetime.now().strftime("%c"))
        return desired_capabilities

    def saucelab_platform(desired_capabilities, os_name, os_version):
        "Set platform for saucelab"

        desired_capabilities['platform']= os_name + ' '+os_version
        return desired_capabilities
