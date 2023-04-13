import os
import jinja2
import configparser
from check_os import checkOs


class OrgSet:
    def __init__(self):
        self.m2_path = None

        # Lê o arquivo config.cfg para obter o valor do m2_path
        config = configparser.ConfigParser()
        config.read('config.cfg')

        self.m2_path = config.get('Config', 'm2_path')
        self.http_proxy = config.get('Config', 'HTTP_PROXY')
        self.https_proxy = config.get('Config', 'HTTPS_PROXY')
        self.vscode_path = config.get('Config', 'vscode_settings_path')
        self.intellij_settings_path = config.get('Config', 'intellij_settings_path')

    def config_maven_settings(self):
        # Copia o template do arquivo settings.xml e renderiza utilizando Jinja2
        env = jinja2.Environment(loader=jinja2.PackageLoader(__name__, 'templates'))
        template = env.get_template('settings.xml.j2')
        rendered_template = template.render(checkOs.detect_os())

        # copia o arquivo settings.xml.j2 renderizado acima em self.m2_path
        settings_path = os.path.join(self.m2_path, "settings.xml")
        with open(settings_path, "w") as f:
            f.write(rendered_template)

        
    def config_http_proxy(self):
        if checkOs.detect_os() == "Linux" or checkOs.detect_os() == "Darwin":
            bash_profile_path = os.path.expanduser("~/.bash_profile")
            with open(bash_profile_path, "a") as f:
                f.write("\n# Configuração do Proxy HTTP\n")
                f.write("export HTTP_PROXY=" + self.http_proxy + "\n")
                f.write("export HTTPS_PROXY=" + self.https_proxy + "\n")
            os.system("source ~/.bash_profile")
            print("Configuração do Proxy HTTP realizada com sucesso!")

    def config_vscode_proxy(self):
        # Copia o template do arquivo settings.json e renderiza utilizando Jinja2
        env = jinja2.Environment(loader=jinja2.PackageLoader(__name__, 'templates'))
        template = env.get_template('settings.json.j2')
        rendered_template = template.render(checkOs.detect_os())

        # copia o arquivo settings.json.j2 renderizado acima em self.vscode_path
        settings_path = os.path.join(self.vscode_path, "settings.json")
        with open(settings_path, "w") as f:
            f.write(rendered_template)

    def config_intellij_proxy(self):
        # Copia o template do arquivo idea.properties e renderiza utilizando Jinja2
        env = jinja2.Environment(loader=jinja2.PackageLoader(__name__, 'templates'))
        template = env.get_template('idea.properties.j2')
        rendered_template = template.render(checkOs.detect_os())

        # copia o arquivo idea.properties.j2 renderizado acima em self.intellij_settings_path
        settings_path = os.path.join(self.intellij_settings_path, "idea.properties")
        with open(settings_path, "w") as f:
            f.write(rendered_template)


# chamada da classe OrgSet
orgset = OrgSet()
orgset.config_maven_settings()
orgset.config_http_proxy()
orgset.config_vscode_proxy()
orgset.config_intellij_proxy()
