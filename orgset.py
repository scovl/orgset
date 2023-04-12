import os
import json
import jinja2

class OrgSet:
    def __init__(self):
        self.os_type = None
        self.m2_path = None

    def check_os(self):
        if os.name == "posix":
            self.os_type = "Linux"
            self.m2_path = os.path.expanduser("~/.m2")
        elif os.name == "nt":
            self.os_type = "Windows"
            self.m2_path = os.path.join(os.environ['USERPROFILE'], ".m2")

    def config_maven_settings(self):
        if not os.path.exists(self.m2_path):
            os.makedirs(self.m2_path)
        settings_path = os.path.join(self.m2_path, "settings.xml")
        
        # Copia o template do arquivo settings.xml e renderiza utilizando Jinja2
        env = jinja2.Environment(loader=jinja2.PackageLoader(__name__, 'templates'))
        template = env.get_template('settings.xml.j2')
        rendered_template = template.render(os_type=self.os_type)
        
        # Grava o arquivo settings.xml na pasta .m2
        with open(settings_path, "w") as f:
            f.write(rendered_template)

    def config_http_proxy(self):
        if self.os_type == "Linux":
            bash_profile_path = os.path.expanduser("~/.bash_profile")
            with open(bash_profile_path, "a") as f:
                f.write("\n# Configuração do Proxy HTTP\n")
                f.write("export HTTP_PROXY=xablau:8080\n")
            os.system("source ~/.bash_profile")
            print("Configuração do Proxy HTTP realizada com sucesso!")
        else:
            print("Esta função só está disponível para sistemas Linux.")


        # Configuração do Proxy HTTP no arquivo settings.json do VSCode
        vscode_path = "/usr/share/code/"
        if os.path.isdir(vscode_path):
            for root, dirs, files in os.walk(vscode_path):
                if "settings.json" in files:
                    settings_path = os.path.join(root, "settings.json")
                    with open(settings_path, "r+") as f:
                        settings_data = json.load(f)
                        http_proxy = {"http.proxy": "xablau:8080"}
                        http_proxy_auth = {"http.proxyAuthorization": None}
                        if http_proxy_auth in settings_data.get("httpSettings", []):
                            settings_data["httpSettings"].insert(settings_data["httpSettings"].index(http_proxy_auth), http_proxy)
                        else:
                            settings_data["httpSettings"].append(http_proxy)
                        f.seek(0)
                        json.dump(settings_data, f, indent=4)
                        f.truncate()
                    print("Configuração do Proxy HTTP no VSCode realizada com sucesso!")
                    break
        else:
            print("Esta função só está disponível para sistemas Linux.")
