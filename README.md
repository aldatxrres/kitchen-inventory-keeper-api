# kitchen-inventory-keeper
Repositório criado para a disciplina de Laboratório de Engenharia de Software
Sistema para Gerenciamento de Despensas de Cozinha. 


# Como inicializar o projeto
 1. Crie um ambiente virtual para isolar as dependências do projeto.
       ```bash
       python3 -m venv env

       source env/bin/activate  # No Windows use `env\Scripts\activate`
       ```
2. Clonar o arquivo .env_example e renomear para .env
3. Preencher corretamente as variáveis do .env
4. Criar um novo database com o nome "kitchen_inventory"
5. Executar as migrations: "python -m manage migrate"
6. Criar um superusuario: "python -m manage createsuperuser"
7. Executar o servidor: "python -m manage runserver"