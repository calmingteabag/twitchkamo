# Twitch Bot

Esse é um bot para o chat do twitch que fiz por sugestão de amigos. Não sou streamer, mas me divirto com essas pequenos projetos, além do que, sempre é possível aprender algo diferente.

## Requisitos

- Python >= 3.10
- TwitchIO >= 2.6.0

## Configuração

Todos os parametros estão em config.ini exceto o token de acesso, que deve ser colocada em uma variável de ambiente.

## Utilização

Verificar as configuirações em config.ini e depois rodar

```
$ python main.py
```

## Jogo das Moedinhas

Usando o comando !jogar, todos do chat podem participar do jogo das moedinhas.

- !jogar : Entra no jogo
- !moeda : Distribui uma quantidade randomica de moedas
- !cofre : Mostra quantas moedas tem
- !rank  : Mostra o rank dos top 10 'ricos'
- !aposta <valor> : Aposta uma quantidade para tentar ganhar mais