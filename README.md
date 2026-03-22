## 🏁 DESCRIPTION
A API CineReserve é uma aplicação backend RESTFull, de alto desempenho e escalavel desenvolvida para gerenciar as complexidades das operações de um cinema moderno. Feito com o foco na integridade dos dados e no controle de concorrências, o sistema fornece um portal para entusiastas de filmes para descobrirem filmes, visualizarem a disponibilidade de assentos em tempo real e garantam seus ingressos por mei ode um fluxo de reservas robusto.

## 📄 TECHNICAL REQUIREMENTS

- [x] ⚙️ [TC.1] Desenvolvimento da API:
    - [x] Python 3
    - [x] Webframework (Django de Preferencia) - Vou usar o Flask
    - [x] Poetry (Desconheço, mas vamos para o desafio)
- [x] 🔐 [TC.2] Autenticação:
    - [x] JWT 
- [x] 💽 [TC.3.1] Banco de Dados:
    - [x] DB Relacional (PostgreSQL de preferencia) - Vou usar o MySQL
    - [x] Garantir que o banco siga as melhores praticas, com atenção a normalização e otimização
- [ ] 🔋 [TC.3.2] Caching & Scalability:
    - [ ] Use estrategias de cache, por exemplo o Redis, para guardar sessões populares e disponibilizar um endpoint de alta performance sobre muita demanda
- [x] 📄 [TC.4.] Paginação:
    - [x] Endpoints de lista com paginação (Filmes, Sessões e Tickets do Usuário).
- [ ] 🧪 [TC.5] Testes:
    - [x] Envie seus unit tests
    - [ ] Garanta que tantos os casos funcionais quanto os extremos estejam cobertos
- [ ] 📝 [TC.6] Documentação:
    - [x] Documentação da API usando Swagger ou Postman
- [-] 🐳 [TC.7] Docker:
    - [-] Disponibilizar o DockerFile e DockerCompose ("Plug&Play")
- [x] 🔧 [TC.8] Git:
    - [x] O projeto deve estar em um repositório publico

## 🌟 BONUS POINTS
- [ ] 👮🏻 Advanced Security Features:
    - [ ] Implemente limitação de requisições nos endpoints da API para prevenir abuso e extração de dados
    - [x] Proteja os endpoint usando as melhores práticas (Validação de inputs, prevenção de SQL Injection e proteção CSRF)
- [ ] 🔁 Asynchronous Tasks:
    - [ ] Use Celery (ou agendador de tarefas similar) para gerenciar processos em segundo plano, auto liberação de filas e envio de e-mails de confirmação.
- [x] 🚀 CI/CD:
    - [x] Configure um sistema basico de CI/CD (Github Actions, GitLab CI/CD, travis CI ou algo parecido) para rodar testes automaticos em todos os push's

## 👨🏼‍🏫 USE CASES
Deverá criar uma API para uma aplicação de ingressos de cinemas. O cinema chama-se "Cinépolis Natal". O software deverá usar as seguintes API's:

- [x] CASE 1: Registro e Login
    - [x] Usuarios devem ser capazes de se cadastrar através da API, fornecendo e-mail, usuário e senha
    - [x] O Sistema deve usar JWT para gerenciar as sessões de login e autorizar requisições protegidas
- [x] CASE 2: Listar todos os filmes disponiveis
    - Um usuário (autenticado ou não) poderá ver a lista completa dos filmes disponiveis no cinema
- [x] CASE 3: Listar todas as sessões disponiveis para um filme especifico
    - Um usuário (autenticado ou não) poderá ver a lista de sessões disponiveis para um filme especifico
- [ ] CASE 4: Visualização do Mapa de Assentos por sessão
    - [ ] O sistema deve distinguir entre assentos que estão disponiveis, reservados (temporariamente bloqueados) ou comprados.
    - Todos os ingressos são grátis
- [ ] CASE 5: Reservas e Bloqueios por sessão
    - [ ] Ao selecionar um assento, o sistema deverá disparar um bloqueio temporário (exemplo, um limite de 10 minutos)
    - [ ] Prevenir outros usuários de selecionar o mesmo assento durante o processo
    - [ ] Observação: Candidatos Full-time devem implementar isso usando Redis; Trainees podem usar uma abordagem mais simples em nível de DB, se preferir.
- [x] CASE 6: Pagamento e Geração de Ticket
    - [x] O sistema processa o pedido e transita a reserva de um cache temporário para um registro permanente no banco de dados (se for um candidato Full-time)
    - Aqui não existe o processo de pagamento. Todos os ingressos são grátis.
    - [x] Um único ingresso digital é gerado e linkado à conta do usuário.
- [ ] CASE 7: Portal de "Meus Ingressos"
    - [ ] Usuários autenticados podem visualizar todos os seus ingressos que comprou
    - [ ] O portal deve permitir usuários de verem seus tickets ativos para os próximos filmes e o histórico completo de suas compras