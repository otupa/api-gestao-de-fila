API para Gestão de FIla dos Motoristas

Este projeto é um sistema de gestão de filas para mobilidade urbana, que visa melhorar a eficiência no transporte público e proporcionar uma experiência mais agradável aos usuários.

Tecnologias Utilizadas

- Linguagem de Programação: Python 3.10+
- Framework: Flask
- Banco de Dados: [Inserir o banco de dados utilizado (caso aplicável)]
- Outras Tecnologias: [Listar outras tecnologias utilizadas]

Instalação

**Requisitos:**

- Python 3.10 ou versão superior
- Banco de Dados [Inserir o banco de dados utilizado (caso aplicável)]
- Git instalado no sistema
- GitHub CLI instalado para autenticação com o repositório

**Passos de Instalação:**

1. Instale o Git:

```bash
sudo apt update
sudo apt install git -y
```

2. Instale o GitHub CLI para autenticação com o repositório (siga as instruções em [github.com/cli/cli](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)).

3. Configure a autenticação do GitHub usando o personal access token:

```bash
sudo gh auth login
```

4. Crie uma pasta para o projeto:

```bash
mkdir /var/www/api-g4
```

5. Clone o repositório na pasta criada:

```bash
sudo git clone https://github.com/otupa/api-gestao-de-fila /var/www/api-g4
```

6. Crie um ambiente virtual Python:

```bash
apt install python3-venv -y
python3 -m venv /var/www/api-g4/.venv
source /var/www/api-g4/.venv/bin/activate
```

7. Instale as dependências do projeto:

```bash
pip install -r /var/www/api-g4/api-gestao-fila/requirements.txt 
```

8. Teste a aplicação Flask:

```bash
python /var/www/api-g4/app.py
```

9. Quando terminar de trabalhar no ambiente virtual, saia com o comando:

```bash
deactivate
```

Configurando a aplicação como um serviço no Debian

1. Crie o arquivo de configuração para a aplicação:

```bash
sudo nano /etc/systemd/system/api-g4.service
```

2. Adicione o seguinte conteúdo ao arquivo:

```plaintext
[Unit]
Description=Instância do Gunicorn para servir a aplicação Flask
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/api-g4/api-gestao-fila
Environment="PATH=/var/www/api-g4/.venv/bin"
ExecStart=/var/www/api-g4/.venv/bin/gunicorn --workers 3 --bind unix:/var/www/api-g4/api-gestao-fila/app.sock -m 007 wsgi:app


[Install]
WantedBy=multi-user.target
```

3. Inicie e habilite o serviço Gunicorn:

```bash
sudo systemctl start api-g4
sudo systemctl enable api-g4
```

Instalando e configurando Nginx como proxy reverso

1. Instale o Nginx:

```bash
sudo apt update
sudo apt install nginx -y
```

2. Crie um arquivo de configuração para sua aplicação no Nginx:

```bash
sudo nano /etc/nginx/sites-available/api-g4
```

3. Adicione a configuração do servidor ao arquivo:

```plaintext
server {
    listen 80;
    server_name seu_dominio.com;

    location / {
        proxy_pass http://unix:/var/www/api-g4/app.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

4. Crie um link simbólico para habilitar o site no Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/api-g4 /etc/nginx/sites-enabled/
```

5. Verifique a sintaxe do arquivo de configuração do Nginx:

```bash
sudo nginx -t
```

6. Recarregue o Nginx para aplicar as alterações:

```bash
sudo systemctl reload nginx
```

Agora, a aplicação deve estar em execução como um serviço no Debian e pode ser acessada através do Nginx como um proxy reverso. Certifique-se de ajustar os caminhos e configurações conforme necessário para o seu ambiente específico.