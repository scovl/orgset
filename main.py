# Importa a classe OrgSet
from orgset import OrgSet

# Cria um novo objeto da classe OrgSet
orgset = OrgSet()

# Chama o método check_os para verificar o sistema operacional
orgset.check_os()

# Chama o método config_settings_xml para configurar o arquivo settings.xml
orgset.config_maven_settings()

# Chama o método config_http_proxy para configurar o proxy HTTP
orgset.config_http_proxy()
