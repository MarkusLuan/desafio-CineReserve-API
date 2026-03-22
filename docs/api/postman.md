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
Filanizar o processo de reserva
>```
>http://{{host}}:{{port}}/api/assentos/{{UUID_SESSAO}}/40
>```

## Listar Sessoes | GET
>```
>http://{{host}}:{{port}}/api/filmes/{{UUID_FILME}}/sessoes?first_result=0&max_results=200
>```
### Query Params
|Param|value|optional
|first_result|0|True
|max_results|200|True
|dt_inicial|2026-01-12|True

### 🔑 Authentication noauth

## Filmes | GET
>```
>http://{{host}}:{{port}}/api/filmes/?first_result=0&max_results=5&genero=ACAO&ano_lancamento=2011
>```

### Query Params
|Param|value|optional|
|---|---|---|
|first_result|0|True|
|max_results|5|True|
|titulo|Pirates of the Caribbean|True|
|genero|ACAO|True|
|ano_lancamento|2011|True|


### 🔑 Authentication noauth

## Meus Ingressos | GET
>```
>http://{{host}}:{{port}}/api/meus_ingressos
>```
### Query Params

|Param|value|Optional|
|---|---|---|
|uuid_filme|select|True|
|first_result|0|True|
|max_results|5|True|



⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
_________________________________________________
Gerado com: [postman-to-markdown](https://github.com/bautistaj/postman-to-markdown/)
