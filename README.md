# Horarios

## Como rodar o código

* Para construir a imagem docer executar:

```
docker build -t agenda-container .
```

* Executando o container agora com o comando:

```
docker run -p 5000:5000 agenda-container
```
OBS¹: O docker foi exposto na porta 5000, por isso mapeio 5000:5000

* Acesse a API via navegador ou ferramenta como Postman:

```
http://localhost:5000/agenda
```

# Acessando o Ubuntu pelo terminal

```
wsl -d Ubuntu-22.04
```

### Como já configurei o Ubuntu-22.04 como default

```
wsl
```