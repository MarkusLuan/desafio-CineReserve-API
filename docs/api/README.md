# Project: Desafio B2Bit - 2026.01 - Backend - CineReserve
# 📁 Collection: Auth 
## Cadastrar Usuário | POST
>```
>http://{{host}}:{{port}}/api/usuarios
>```
### Body (**raw**)

```json
{
    "dt_nascimento": "1997-02-19",
    "email": "markus@teste.com",
    "nome": "teste",
    "senha": "1234"
}
```
### 🔑 Authentication noauth

## Fazer Login | POST
>```
>http://{{host}}:{{port}}/api/auth
>```
### Body (**raw**)

```json
{
    "email": "markus@teste.com",
    "senha": "1234"
}
```
### 🔑 Authentication noauth

## Obter informações do login ativo | GET
>```
>http://{{host}}:{{port}}/api/auth
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Collection: Assentos 
## Listar Assentos | GET
>```
>http://{{host}}:{{port}}/api/assentos/{{UUID_SESSAO}}
>```

## Selecionar Assento | GET
Ao selecionar o assento o sistema deixa em pré-reservar por 10 minutos
>```
>http://{{host}}:{{port}}/api/assentos/{{UUID_SESSAO}}/1
>```

## Finalizar reserva | POST
Finalizar o processo de reserva
>```
>http://{{host}}:{{port}}/api/assentos/{{UUID_SESSAO}}/40
>```

## Listar Sessoes | GET
>```
>http://{{host}}:{{port}}/api/filmes/{{UUID_FILME}}/sessoes?first_result=0&max_results=200
>```
### Query Params

|Param|value|obrigatorio|
|---|---|---|
|first_result|0|False|
|max_results|200|False|
|dt_inicial|2026-01-12|False|
|dt_final|2026-01-12|False|


### 🔑 Authentication noauth

## Filmes | GET
>```
>http://{{host}}:{{port}}/api/filmes/?first_result=0&max_results=5&genero=ACAO&ano_lancamento=2011
>```
### Query Params

|Param|value|obrigatorio|
|---|---|---|
|first_result|0|False|
|max_results|5|False|
|titulo|Pirates of the Caribbean|False|
|genero|ACAO|False|
|ano_lancamento|2011|False|


### 🔑 Authentication noauth
## Meus Ingressos | GET
>```
>http://{{host}}:{{port}}/api/meus_ingressos
>```
### Query Params

|Param|value|obrigatorio|
|---|---|---|
|dt_inicial|2026-03-22T14:59:06|False
|dt_final|2026-03-22T14:59:06|False

_________________________________________________
Gerado com: [postman-to-markdown](https://github.com/bautistaj/postman-to-markdown/)
