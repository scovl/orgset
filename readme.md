## OrgSet

OrgSet é uma ferramenta de linha de comando desenvolvida em Python que permite configurar o ambiente de desenvolvimento de acordo com o padrão da organização de maneira simples. A classe suporta os sistemas operacionais Linux e Windows e realiza as seguintes tarefas:

* Configura o arquivo `settings.xml` do Maven para o ambiente de desenvolvimento.
* Configura o proxy HTTP no arquivo `.bash_profile` no Linux e Mac.
* Configura o vscode com o Proxy HTTP.
* Configura o IntelliJ IDEA com o Proxy HTTP.

### Pré-requisitos

* Python 3.6 ou superior.
* Maven 3.6.3 ou superior.
* Git 2.25.1 ou superior.

```bash
pip install jinja2 configparser --user 
```

### Como usar

Clone o repositório do projeto, entre na pasta e execute o seguinte comando:

```bash
python3 orgset.py
```
> Edite o orgset.py para executar apenas as funções que deseja ao fim do arquivo. Exemplo:

```python
orgset = OrgSet()
orgset.check_os()
orgset.config_maven_settings()
orgset.config_http_proxy()
orgset.config_vscode_proxy()
orgset.config_intellij_proxy()

```

## Configuração

O arquivo `config.cfg` deve conter as informações necessárias para configurar os proxies dos programas. O formato do arquivo é o seguinte:

```bash
[Config]
m2_path = /caminho/para/a/pasta/.m2
HTTP_PROXY = http://<usuario>:<senha>@<endereco>:<porta>
HTTPS_PROXY = https://<usuario>:<senha>@<endereco>:<porta>
vscode_settings_path = /caminho/para/a/pasta/.config/Code/User/
intellij_settings_path = /caminho/para/a/pasta/.IntelliJIdea<versao>/config/
```

---

## Contribuição

Se você deseja contribuir para o projeto OrgSet, siga os seguintes passos:

* Faça um fork deste repositório para sua própria conta no GitHub.

Clone o repositório do seu fork em sua máquina local, crie uma nova branch e faça as alterações necessárias e por fim, envie um pull request para o repositório original. Siga o modelo gitflow para criar as branches.

Para mais informações sobre gitflow, acesse o link: **[https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)**.