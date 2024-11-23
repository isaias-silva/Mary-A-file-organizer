# Mary-A: Organizador de Arquivos
![alt text](image.png)

**Mary-A** é uma ferramenta automatizada para organizar seus arquivos de maneira simples e eficiente. Feito em Python, este script move e renomeia arquivos com base em suas extensões, permitindo que você mantenha seu sistema organizado sem esforço.

## Funcionalidades

- Mover arquivos automaticamente para pastas específicas com base em suas extensões (ex: .pdf, .jpg, .mp4, etc).
- Suporte para múltiplas linguagens e formatos de arquivo (ex: SQL, HTML, JavaScript, Python, TypeScript, JSON, etc).
- Renomeia arquivos automaticamente se houver conflitos de nome no diretório de destino.
- Fácil de configurar e personalizar para diferentes categorias de arquivos.

## Requisitos

- Python 3.6+
- Bibliotecas padrão do Python: `shutil`, `os`, `pathlib`, `re`

## Instalação

1. Clone este repositório:

    ```bash
    git clone <link do repositorio>
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd mary-a
    ```

3. (Opcional) Crie um ambiente virtual e ative-o:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

## Uso

1. Defina as categorias de arquivos que deseja organizar no arquivo de configuração *data/config.json*:

    Exemplo de categorias:

    ```json 
   {"path": "your_path",
    "default_paths": [
        {
            "name": "images",
            "regex": "*.jpg|*.jpeg|*.png|*.gif|*.bmp|*.tiff|*.webp|*.avif|*.svg|*.ico"
        },
        {
            "name": "videos",
            "regex": "*.mp4|*.mkv|*.avi|*.mov|*.wmv|*.flv|*.webm|*.3gp|*.mpeg"
        },
        {
            "name": "documents",
            "regex": "*.pdf|*.docx|*.doc|*.txt|*.md|*.rtf|*.odt|*.xls|*.xlsx|*.ppt|*.pptx|*.epub|*.csv"
        },
        {
            "name": "musics",
            "regex": "*.mp3|*.m4a|*.flac|*.wav|*.aac|*.ogg|*.wma|*.alac"
        },
        {
            "name": "install",
            "regex": "*.deb|*.rpm|*.tar.gz|*.tar.bz2|*.tar.xz|*.snap|*.AppImage|*.exe|*.msi|*.pkg"
        },
        {
            "name": "iso_images",
            "regex": "*.iso|*.img|*.bin|*.cue|*.nrg"
        },
        {
            "name": "code_files",
            "regex": "*.js|*.html|*.css|*.py|*.java|*.c|*.cpp|*.ts|*.php|*.sh|*.json|*.xml|*.yml|*.yaml"
        },
        {
            "name": "archives",
            "regex": "*.zip|*.rar|*.7z|*.tar|*.gz|*.bz2|*.xz"
        },
          {
            "name": "access_keys",
            "regex": "*.pem|*.key|*.crt|*.cer|*.pfx|*.p12|*.asc|*.gpg|*.pgp|*.ssh|*.id_rsa|*.id_dsa|*.ed25519"
        }
    ]}
   ```

2. Execute o script:

    ```bash
    python3 main.py
    ```

3. Os arquivos serão automaticamente movidos para suas pastas correspondentes.
