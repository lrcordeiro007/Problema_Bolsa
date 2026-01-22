# Resolução Problema

Afim de criar uma solução simples de classificação textual, foi feito uma análise de sentimento.

Para fazer o projeto funcionar é preciso que primeiramente você tenha o `Docker` já instalado na sua máquina.
Após isso é preciso que clone o repositório em seu terminal
```bash
git clone https://github.com/lrcordeiro007/Problema_Bolsa.git
cd Problema_Bolsa
```
Logo em seguida é preciso rodar os comandos do `Docker`, já que ele vai fazer tudo para você
```bash
docker build -t mlops-problema .
```
```bash
docker run -d -p 8000:8000 --name nlp-service mlops-problema
```
Assim já estará funcionando o seu código, se quiser testa-lo é preciso que clique, com Control + clique no botão direito, no `8000:8000` que vai aparecerno terminal após 
os contairnes já estivem rodando, ou se preferir cole isto no seu navegador:
```bash
http://localhost:8000/docs
```
Após isso, dentro já da API, é possível escrever frases e testar o modelo ver se ele está classificando de forma correta.

