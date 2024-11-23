# Trabalho prático 4 - Redes de Computadores II - Sistemas de Informação - UFVJM
### Alunos: Ian Carlos Gonçalves da Conceição, Jhonathan Wallace Lacerda dos Santos e Pedro Henrique Barroso;

# Chat utilizando websockets com Python

## Para conseguir utilizar esta aplicação, siga os passos abaixo:

> 1. Clone o repositório;
>
> 2. Verifique se você possui o Python instalado em sua máquina. Caso não possua, você pode baixá-lo [aqui](https://www.python.org/downloads/);
>
> 3. Instale as dependências necessárias presentes no arquivo "requirements.txt". Neste projeto foi criado um ambiente virtual usando venv, no final deste arquivo readme estará um passo a passo de como criar um ambiente virtual;
>
> 4. Execute o arquivo "main.py" através do terminal, pelo Pycharm ou Visual Studio Code para inicializar o servidor;
>
> 5. Abra o arquivo "index.html", seguindo as instruções logo abaixo, para visualizar o chat e utilizá-lo;

> <strong> << ATENÇÃO! ABERTURA DO ARQUIVO INDEX.HTML>>
>
> Utilize a extensão Live Server no Visual Studio Code para abrir o arquivo "index.html" ou abra o arquivo no navegador através do Pycharm(ambos exemplos mostrados no vídeo explicativo). </strong> 
> <br> Apenas abrir o arquivo "index.html" com seu navegador diretamente não irá fazer com que o chat funcione, pois o arquivo "index.html" precisa estar mesmo que em um servidor local para que comunique com o websocket e funcione corretamente;
> 
> <strong> ID de Extensão "Live Server": </strong>
> <br> Cole isto na aba de extensões do Visual Studio Code: ritwickdey.LiveServer

> ### Acesse o vídeo de explicação do código clicando [aqui](https://drive.google.com/);


> <strong> CRIAÇÃO AMBIENTE VIRTUAL: </strong>
>
> Passo 1 - Criar um diretório:
> <br> mkdir redes2chatwebsockets
>
> Passo 2 - Entrar no diretório:
> <br> cd redes2chatwebsockets
> <br> *Obs: Verifique se está no diretório correto usando o comando "pwd"
>
> Passo 3 - Instalar o ambiente virtual:
> a. Instalação do pacote
> <br> sudo apt install python3.12 -venv
> <br> *Obs: Pode ser que solicite que você execute o comando "sudo apt-get update"
>
> b. Criação do Ambiente Virtual
> <br> python3 -m venv env
>
> Passo 4 - Ativar o ambiente virtual:
> <br> source env/bin/activate
>
> Passo 5 - Instalação das dependências:
> <br> pip3 install websockets
> <br> pip3 install asyncio
>
> Passo 6 - Listar os pacotes instalados:
> <br> pip3 list
>
> Passo 7 - Mostra os pacotes e a versão para inserir no arquivo requirements.txt
> <br> pip3 freeze
>
> Passo 8 - Criação do arquivo requirements:
> <br> pip3 freeze > requirements.txt
>
> Passo 9 - Listar o arquivo requirements.txt:
> <br> cat requirements.txt
