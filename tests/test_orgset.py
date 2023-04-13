import unittest
from unittest.mock import MagicMock, patch
from orgset import OrgSet


class TestOrgSet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configura o ambiente para os testes
        cls.orgset = OrgSet()

    def test_config_maven_settings(self):
        # Configura um mock para a função detect_os da classe checkOs
        with patch('check_os.checkOs.detect_os', return_value='Linux') as mock_detect_os:
            # Configura um mock para a função write do objeto file
            with patch('builtins.open', create=True) as mock_open:
                # Chama o método que será testado
                self.orgset.config_maven_settings()

                # Verifica se o mock da função detect_os foi chamado
                mock_detect_os.assert_called_once()

                # Verifica se o mock da função open foi chamado com os argumentos corretos
                mock_open.assert_called_once_with('/home/user/.m2/settings.xml', 'w')

    def test_config_http_proxy(self):
        # Configura um mock para a função detect_os da classe checkOs
        with patch('check_os.checkOs.detect_os', return_value='Linux') as mock_detect_os:
            # Configura um mock para a função write do objeto file
            with patch('builtins.open', create=True) as mock_open:
                # Chama o método que será testado
                self.orgset.config_http_proxy()

                # Verifica se o mock da função detect_os foi chamado
                mock_detect_os.assert_called_once()

                # Verifica se o mock da função open foi chamado com os argumentos corretos
                mock_open.assert_called_once_with('/home/user/.bash_profile', 'a')

    def test_config_vscode_proxy(self):
        # Configura um mock para a função detect_os da classe checkOs
        with patch('check_os.checkOs.detect_os', return_value='Linux') as mock_detect_os:
            # Configura um mock para a função write do objeto file
            with patch('builtins.open', create=True) as mock_open:
                # Chama o método que será testado
                self.orgset.config_vscode_proxy()

                # Verifica se o mock da função detect_os foi chamado
                mock_detect_os.assert_called_once()

                # Verifica se o mock da função open foi chamado com os argumentos corretos
                mock_open.assert_called_once_with('/home/user/.config/Code/User/settings.json', 'w')

    def test_config_intellij_proxy(self):
        # Configura um mock para a função detect_os da classe checkOs
        with patch('check_os.checkOs.detect_os', return_value='Linux') as mock_detect_os:
            # Configura um mock para a função write do objeto file
            with patch('builtins.open', create=True) as mock_open:
                # Chama o método que será testado
                self.orgset.config_intellij_proxy()

                # Verifica se o mock da função detect_os foi chamado
                mock_detect_os.assert_called_once()

                # Verifica se o mock da função open foi chamado com os argumentos corretos
                mock_open.assert_called_once_with('/home/user/.IntelliJIdea/config/idea.properties', 'w')


if __name__ == '__main__':
    unittest.main()
