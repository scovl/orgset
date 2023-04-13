import unittest
from orgset import OrgSet

class TestOrgSet(unittest.TestCase):

    def setUp(self):
        self.orgset = OrgSet()
        self.orgset.check_os()
        self.orgset.config_maven_settings()
        self.orgset.config_http_proxy()
        self.orgset.config_vscode_proxy()
        self.orgset.config_intellij_proxy()

    def test_check_os(self):
        self.assertIsNotNone(self.orgset.os_type)

    def test_config_maven_settings(self):
        maven_settings_path = self.orgset.m2_path + "/settings.xml"
        with open(maven_settings_path, "r") as f:
            contents = f.read()
            self.assertIn("mirror", contents)

    def test_config_http_proxy(self):
        if self.orgset.os_type in ["Linux", "MacOS"]:
            bash_profile_path = os.path.expanduser("~/.bash_profile")
            with open(bash_profile_path, "r") as f:
                contents = f.read()
                self.assertIn("HTTP_PROXY", contents)
                self.assertIn("HTTPS_PROXY", contents)

    def test_config_vscode_proxy(self):
        vscode_settings_path = self.orgset.vscode_path + "/settings.json"
        with open(vscode_settings_path, "r") as f:
            contents = f.read()
            self.assertIn("http.proxy", contents)

    def test_config_intellij_proxy(self):
        intellij_settings_path = self.orgset.intellij_settings_path + "/idea.properties"
        with open(intellij_settings_path, "r") as f:
            contents = f.read()
            self.assertIn("http.proxy", contents)

if __name__ == '__main__':
    unittest.main()
