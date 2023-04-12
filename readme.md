## OrgSet

OrgSet é uma ferramenta de linha de comando desenvolvida em Python que permite configurar o ambiente de desenvolvimento de acordo com o padrão da organização de maneira simples. A classe suporta os sistemas operacionais Linux e Windows e realiza as seguintes tarefas:

* Configura o arquivo settings.xml do Maven para o ambiente de desenvolvimento;
* Configura o proxy HTTP no arquivo `.bash_profile` (Linux) ou nas configurações do VSCode (Windows);
* Configura as variáveis de ambiente necessárias para o ambiente de desenvolvimento.

### Como usar

Para usar a classe OrgSet, siga os seguintes passos:

Clone este repositório em sua máquina local:

```bash
git clone https://github.com/seu_nome_de_usuário/orgset.git
```

Entre na pasta orgset:

```bash
cd orgset
```

Execute o arquivo main.py:

```bash
python main.py
```

Siga as instruções na tela para configurar o ambiente de desenvolvimento. Note que algumas das tarefas realizadas pela classe OrgSet podem exigir privilégios de administrador, por isso é recomendável executar o comando como administrador (no Windows) ou com o prefixo sudo (no Linux).
Requisitos A classe OrgSet requer Python 3.x e o jinja2 para funcionar. Você pode instalar os pacotes necessários usando o seguinte comando:

```bash
pip install jinja2 --user
```

## Contribuição

Se você deseja contribuir para o projeto OrgSet, siga os seguintes passos:

* Faça um fork deste repositório para sua própria conta no GitHub.

Clone o repositório do seu fork em sua máquina local, crie uma nova branch e faça as alterações necessárias e por fim, envie um pull request para o repositório original.