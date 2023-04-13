import os
import platform
import requests
import zipfile
import tarfile
import configparser
import shutil


class ToolsInstall:
    def __init__(self):
        self.os_type = None
        self.m2_path = None
        self.idea_path = None
        self.config = configparser.ConfigParser()
        self.config.read('config.cfg')

    def check_os(self):
        if platform.system() == "Linux":
            self.os_type = "Linux"
            self.m2_path = os.path.expanduser("~/.m2/")
            self.idea_path = os.path.expanduser("~/idea-IC")
        elif platform.system() == "Windows":
            self.os_type = "Windows"
            self.m2_path = os.path.join(os.environ["USERPROFILE"], ".m2")
            self.idea_path = os.path.expanduser("~/idea-IC")
        elif platform.system() == "Darwin":
            self.os_type = "MacOS"
            self.m2_path = os.path.expanduser("~/.m2/")
            self.idea_path = os.path.expanduser(
                "~/Applications/IntelliJ IDEA CE.app")
        else:
            print("Sistema Operacional não suportado!")
            exit(1)

    def install_maven(self):
        # Verifica se o Maven já está instalado
        if os.path.exists(self.m2_path):
            print("Maven já está instalado!")
            return

        maven_version = "apache-maven-3.8.3"
        url = f"https://apache.uib.no/maven/maven-3/3.8.3/binaries/{maven_version}-bin.zip"
        if self.os_type == "Linux":
            dest = "/opt"
        elif self.os_type == "Windows":
            dest = os.path.join(os.environ["ProgramFiles"], "Apache")
        elif self.os_type == "MacOS":
            dest = "/opt"
        else:
            print("Sistema Operacional não suportado!")
            exit(1)

        # cria a pasta de destino se não existir
        if not os.path.exists(dest):
            os.makedirs(dest)

        # faz download do maven e extrai o conteúdo
        r = requests.get(url)
        with open(f"{maven_version}.zip", "wb") as f:
            f.write(r.content)
        with zipfile.ZipFile(f"{maven_version}.zip", "r") as zip_ref:
            zip_ref.extractall(dest)

        # configura variáveis de ambiente necessárias para o maven
        if self.os_type == "Linux" or self.os_type == "MacOS":
            bash_profile_path = os.path.expanduser("~/.bash_profile")
            with open(bash_profile_path, "a") as f:
                f.write("\n# Configuração do Maven\n")
                f.write(f'export PATH=$PATH:{dest}/{maven_version}/bin\n')
                f.write(f'export M2_HOME={dest}/{maven_version}\n')
            os.system("source ~/.bash_profile")
        elif self.os_type == "Windows":
            with open(os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Microsoft",
                                   "WindowsApps", "maven.cmd"), "w") as f:
                f.write(
                    f'@echo off\nset "M2_HOME={dest}\\{maven_version}"\nset "PATH=%PATH%;%M2_HOME%\\bin"\n"%*"\n')
            os.system(f'set os.system(f'setx PATH "%PATH%;{dest}\\{maven_version}\\bin"')

    def install_idea(self):
        self.check_os()

        intellij_settings_path = self.config.get(
            'DEFAULT', 'intellij_settings_path')

        if os.path.exists(intellij_settings_path):
            print(
                f"O diretório {intellij_settings_path} já existe. O IntelliJ IDEA Community Edition não será instalado novamente.")
            return

        # Define a URL de download do IntelliJ IDEA Community Edition de acordo com o sistema operacional
        if self.os_type == "linux":
            url = "https://download.jetbrains.com/idea/ideaIC-latest.tar.gz"
        elif self.os_type == "win":
            url = "https://download.jetbrains.com/idea/ideaIC-latest.win.zip"
        elif self.os_type == "macos":
            url = "https://download.jetbrains.com/idea/ideaIC-latest.dmg"

        # Baixa o arquivo do IntelliJ IDEA Community Edition e o salva em um arquivo temporário
        with urllib.request.urlopen(url) as response, tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)

        # Descompacta o arquivo do IntelliJ IDEA Community Edition na pasta do usuário
        if self.os_type == "linux":
            idea_dir = os.path.expanduser("~/idea-IC")
            if os.path.exists(idea_dir):
                shutil.rmtree(idea_dir)
            os.makedirs(idea_dir)
            os.system(
                f"tar -xzf {tmp_file.name} -C {idea_dir} --strip-components=1")
        elif self.os_type == "win":
            idea_dir = os.path.expanduser("~/idea-IC")
            if os.path.exists(idea_dir):
                shutil.rmtree(idea_dir)
            os.makedirs(idea_dir)
            with zipfile.ZipFile(tmp_file.name, "r") as zip_ref:
                zip_ref.extractall(idea_dir)
        elif self.os_type == "macos":
            idea_dir = os.path.expanduser(
                "~/Applications/IntelliJ IDEA CE.app")
            if os.path.exists(idea_dir):
                shutil.rmtree(idea_dir)
            os.makedirs(idea_dir)
            os.system(f"hdiutil attach {tmp_file.name}")
            os.system(f"cp -R /Volumes/IntelliJ\ IDEA\ CE/* {idea_dir}")
            os.system("hdiutil detach /Volumes/IntelliJ\\ IDEA\\ CE")

        # Remove o arquivo temporário
        os.remove(tmp_file.name)

        # Cria a pasta de configurações do IntelliJ IDEA Community Edition
        if not os.path.exists(intellij_settings_path):
            os.makedirs(intellij_settings_path)
            print(f"O diretório {intellij_settings_path} foi criado.")
