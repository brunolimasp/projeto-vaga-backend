# ACMEVita


O projeto da ACMEVita foi construído com FastAPI devido à sua facilidade e agilidade na criação de APIs, juntamente com sua documentação automática utilizando recursos da OpenAPI como Swagger e Redoc. Para armazenar os dados, optei pelo Postgres devido à sua estabilidade, solidez e ampla adoção no mercado.

## Instruções e Requisitos


- Certifique-se de ter o Docker instalado em seu ambiente. Se ainda não o tiver, você pode baixá-lo e instalá-lo a partir do site oficial: Docker.

- Após instalar o Docker, abra um terminal ou prompt de comando.

- Navegue até o diretório raiz do projeto onde está localizado o arquivo docker-compose.yml.

- Execute o seguinte comando:


```cmd
docker-compose up -d
```

- Aguarde até que o Docker baixe as imagens, construa os contêineres e inicie o serviço.

- Uma vez que o serviço esteja em execução, você poderá acessar a documentação das API´s pelo Swagger ou Redocs através das rotas: http://127.0.0.1:8000/redoc  ou http://127.0.0.1:8000/docs para acessar o banco de dadados é possivel fazer acesso pelo PGadmin na rota http://localhost:16543/

- As credenciais para acesso ao banco estão no arquivo `.env`

### Testes unitários
Neste projeto, utilizamos a biblioteca pytest para realizar testes nos endpoints da nossa aplicação. Os testes são uma parte fundamental do desenvolvimento de software, pois garantem que o código funcione corretamente em diferentes cenários e situações.

Para realizar os testes nos endpoints, é necessário que o banco de dados esteja rodando, pois os testes irão comparar as respostas dos endpoints com os dados armazenados no banco de dados. Isso nos permite verificar se os endpoints estão retornando as respostas esperadas de acordo com os dados fornecidos.

Para executar os testes, basta rodar o seguinte comando no terminal, na pasta raiz do projeto

```cmd
pytest ./src/
```
### Observações

Ao iniciar a aplicação através do Docker Compose, as tabelas serão criadas automaticamente e dados fictícios serão inseridos. Isso simula o funcionamento da aplicação em um ambiente de testes ou desenvolvimento, proporcionando uma experiência prática e realista para fins de avaliação e desenvolvimento.