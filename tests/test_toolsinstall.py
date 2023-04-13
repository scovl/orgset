import os
import unittest
from unittest.mock import patch, MagicMock, Mock
import tempfile
from tools import ToolsInstall


class TestToolsInstall(unittest.TestCase):
    def setUp(self):
        self.tools_install = ToolsInstall()
        self.tools_install.m2_path = '/opt/maven'
        self.tools_install.idea_path = '/Applications/IntelliJ IDEA CE.app'

    @patch('check_os.checkOs.detect_os', return_value='Linux')
    @patch('requests.get')
    @patch('os.makedirs')
    def test_install_maven(self, mock_makedirs, mock_get, mock_detect_os):
        mock_response = MagicMock()
        mock_response.content = b'content'
        mock_get.return_value = mock_response
        with patch('tempfile.NamedTemporaryFile', return_value=MagicMock(name='tmp_file', __enter__=MagicMock(return_value=MagicMock(name='file', write=MagicMock())))):
            with patch('tarfile.TarFile.extractall'):
                self.tools_install.install_maven()
                mock_makedirs.assert_called_once_with('/opt')
                mock_get.assert_called_once_with(
                    'https://apache.uib.no/maven/maven-3/3.8.3/binaries/apache-maven-3.8.3-bin.zip')
                mock_response.raise_for_status.assert_called_once()
                mock_response.content.assert_called_once()
                os.makedirs.assert_called_once_with('/opt/maven')

    @patch('check_os.checkOs.detect_os', return_value='Linux')
    @patch('urllib.request.urlopen')
    @patch('os.makedirs')
    @patch('shutil.rmtree')
    @patch('zipfile.ZipFile.extractall')
    @patch('os.remove')
    @patch('os.path.expanduser')
    @patch('os.system')
    
    def test_install_idea(self, mock_system, mock_expanduser, mock_remove, mock_extractall, mock_rmtree, mock_makedirs, mock_urlopen, mock_detect_os):
        # Cenário
        self.tools_install.config.set(
            'DEFAULT', 'intellij_settings_path', 'fake/path')
        mock_urlopen.return_value = Mock()
        mock_urlopen.return_value.__enter__.return_value.read.return_value = (b'conteudo do arquivo')
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(b'conteudo do arquivo')
        temp_file.close()
        mock_expanduser.return_value = os.path.expanduser('~/idea-IC')

        # Ação
        self.tools_install.install_idea()

        # Verificação
        mock_detect_os.assert_called_once()
        mock_urlopen.assert_called_once_with(
            'https://download.jetbrains.com/idea/ideaIC-latest.tar.gz')
        mock_makedirs.assert_called_once_with(os.path.expanduser('~/idea-IC'))
        mock_system.assert_called_once_with(
            f"tar -xzf {temp_file.name} -C ~/idea-IC --strip-components=1")
        mock_remove.assert_called_once_with(temp_file.name)
