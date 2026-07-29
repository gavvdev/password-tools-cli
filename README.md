# 💻 Password Tools CLI

Aplicação de terminal desenvolvida em Python que utiliza a biblioteca **password-tools** por meio de **Git Submodule**.

Este projeto foi desenvolvido como atividade prática sobre estruturas de repositórios, versionamento e submódulos utilizando Git.

## Funcionalidades

* Gerar senhas seguras.
* Verificar a força de uma senha.
* Verificar se uma senha está entre as mais comuns.
* Gerar passphrases.

## Estrutura

```text
password-tools-cli/
│
├── password-tools/   ← Submódulo
├── app.py
├── README.md
├── .gitmodules
├── LICENSE
└── .gitignore
```

## Clonando o projeto

Clone o repositório:

```bash
git clone https://github.com/gavvdev/password-tools-cli.git
```

Entre na pasta:

```bash
cd password-tools-cli
```

Inicialize o submódulo:

```bash
git submodule update --init --recursive
```

## Executando

Execute:

```bash
python app.py
```

Será exibido um menu semelhante ao seguinte:

```text
========================================
      PASSWORD TOOLS CLI
========================================
1 - Gerar senha segura
2 - Verificar força da senha
3 - Verificar senha comum
4 - Gerar passphrase
0 - Sair
========================================
```

## Tecnologias

* Python 3
* Git
* Git Submodules
* GitHub

## Biblioteca utilizada

Este projeto utiliza a biblioteca **password-tools** como submódulo Git.

## Licença

Este projeto utiliza a licença MIT.
