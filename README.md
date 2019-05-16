# Treinamento FIWARE Lab @ RNP
## Desenvolvimento de aplicações com FIWARE

Os passos das etapas práticas foram disponibilizados no atual repositório em arquivo `.ipynb` que podem ser executados utilizando a ferramenta **Jupyter Notebook**.

Para isso, tendo em um ambiente com Python instalado, instale as seguintes depências usando o `pip`:
- **Jupyter** para visualização e execução dos passos:
```
pip install jupyter
```
- **requests** para realização de requisições HTTP:
```
pip install requests
```
- **fiotclient** para chamadas abstraídas aos serviços FIWARE:
```
pip install fiotclient
```

#### Implantação do ambiente

Para configuração do ambiente tradicionalmente, cada um dos componentes (Generic Enablers, ou GEs) do FIWARE tem que ser implantados e configurados.
Um exemplo de arquitetura contendo alguns dos principais GEs é apresentada abaixo:

![](https://raw.githubusercontent.com/FIoT-Client/fiot-client-tutorial/master/extras/fiware_components_deploy.png)

Essa configuração pode ser feita de forma manual, a partir dos passos descritos na documentação de cada GE.
As documentações para os principais GEs do FIWARE, contendo os passos de configuração manual de cada serviço, pode ser acessada a partir dos links abaixo:

- Orion Context Broker: https://fiware-orion.readthedocs.io/en/master/user/index.html
- UL IoT-Agent: https://fiware-iotagent-ul.readthedocs.io/en/latest/index.html
- Cygnus: https://fiware-cygnus.readthedocs.io/en/latest/
- STH_Comet: https://fiware-sth-comet.readthedocs.io/en/latest/
- Wirecloud: https://wirecloud.readthedocs.io/en/stable/user_guide/

Porém, normalmente a mesma é feita a partir da implantação de *containers Docker* disponibilizadas nos repositórios de cada componente e na página do [Dockerhub do FIWARE](https://hub.docker.com/u/fiware/).

#### Configuração da aplicação
Após ter configurado ou ter acesso a um conjunto de componentes (Generic Enablers) FIWARE, a configuração de uma aplicação que utiliza esse serviços tem os seguintes passos:
- Criação do serviço
- Criação de entidade
- Registro de dispositivo
- Configuração do dispositivo para envio de dados e/ou execução de comandos
- Armazenamento de dados históricos de leituras

No arquivo `raw_fiware.ipynb` são exibidos os passos para executar cada um dessas etapas usando diretamente *chamadas HTTP* às APIs FIWARE.

No arquivo `fiotclient.ipython` os passos são exibidos utilizando a biblioteca *fiotclient* de abstração às chamadas FIWARE.

Utilizando o *FIWARE-Lab@RNP*, os passos de uso serão explicitados ao longo da apresentação e, posteriormente, disponibilizados a partir de um manual de usuário ilustrado.

#### Implementação de código no dispositivo

Tendo configurado os serviços, entidades e dispositivos da aplicação, o código que estará em execução em um dispositivo (como RaspberryPi ou Arduino) deve então ser desenvolvido para que os dados de medições e a execução de comandos possa ser realizada.
Um exemplo de contendo trechos de código dessas principais funções é apresentado no arquivo `device_smart_place.py`.
