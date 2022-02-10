# Visão do Produto e Projeto

## 1. Visão Geral do Produto

### 1.1 Declaração do Problema

|                                | 	                                                  |
| :----------------------------: | :------------------------------------------------------------------------------------ |
| O problema                     |  Dificuldade, dos alunos da UnB, em organizar a agenda quanto às aulas e quanto às demais atividades do dia-a-dia. |
| Afeta                          |  Alunos da UnB.      |
| Cujo Impacto é                 |  Menor desempenho acadêmico.   |
| Uma solução de sucesso seria   |  Uma agenda personalizada para esse público. |

### 1.2 Declaração de Posição do Produto

Apesar de existirem muitas agendas no mercado, nenhuma delas é voltada e personalizada para o público que o produto apresentado pretende atingir. Dessa forma, o nosso produto destaca-se em meio aos demais devido à forma que se atentará aos problemas dos discentes. Para isso haverá, na aplicação Web, por exemplo, uma maior facilidade de se agendar eventos conforme a grade horária da instituição acadêmica.

|                                | 	                                                  |
| :----------------------------: | :------------------------------------------------------------------------------------ |
| Para                           |  Alunos da UnB. |
| Quem                           |  Possuem dificuldade em se organizar    |
| O (nome do projeto)            |  FGAgenda   |
| Que                            |  Será personalizado para o público-alvo, facilitando, por exemplo, enquadrar seus afazeres dentro da Grade horária seguida pela instituição acadêmica. |
| Ao contrário                   |  Do google agenda, que não é personalizado para os estudantes da UnB. |
| Nosso Produto                  |  Será sincronizado com a grade da UnB, cada evento possuirá uma To-Do List do que o usuário necessita realizar. Além disso, terá notificações para informar que o prazo para a realização de determinada meta está acabando. Finalmente, outras pessoas poderão enviar convites de eventos (ex.: monitoria) e serão apresentadas as porcentagens cumpridas das tarefas.     |

### 1.3 Objetivos do Produto
O produto visa facilitar a organização pessoal do usuário com relação a seu tempo, por meio da junção, na aplicação, de todos os eventos e metas do usuário, sendo todos esses bem detalhados na própria aplicação. Mais especificamente, o produto visa o público alvo de alunos da UnB e, dessa forma, objetiva que esses usuários possam adicionar eventos que seguem a grade horária da faculdade mais facilmente, diferentemente de outros tipos de eventos.

## 2. Abordagem de desenvolvimento de software

### 2.1 Metodologia

A partir dos fatores propostos por Sommerville (SOMMERVILLE, 2011), para avaliação quanto a utilização de uma abordagem dirigida a plano ou ágil, a equipe utilizou os seguintes:
Sistema. 
Nas questões técnicas, o sistema a ser desenvolvido é considerado médio-grande devido ao escopo da aplicação, a qual será realizada para a Web (responsiva) e possui vida útil até o final do semestre 2021/2, pois o produto é focado, principalmente, para os alunos na UnB, portanto, contará com funcionalidades específicas para o público-alvo. Além do que,  as atividades do sistema não precisará passar por análise com o objetivo de verificar se estão de acordo com as normas estabelecidas pelo Governo por Lei, ou seja, não será auditável.  
Equipe. 
O nível de competência da equipe é satisfatório para as tecnologias escolhidas para produzir a aplicação, e como ocorrerá a rotatividade dos desenvolvedores do back-end e do front-end, a equipe pode ser considerada full-stack, ainda tendo como suporte para o sistema as tecnologias: Django/Python, HTML/CSS, PWA, Git/GitHub, Figma, Microsoft Teams, ZenHub.
Organização. 
Nos aspectos organizacionais, não é necessário uma especificação detalhada dos requisitos antes de começar a implementação, além do que o Product Owner será parte da equipe, e com a entrega de uma funcionalidade da aplicação por semana, o objetivo principal é a valorização do produto como um todo.  
De acordo com as características do produto com relação às questões técnicas, humanas e organizacionais, a metodologia escolhida pela equipe foi a Metodologia Ágil, e dentro dela, o Framework Scrum.  
Tendo em vista os aspectos do sistema, o Scrum possibilita desenvolver, de maneira mais eficiente,  uma aplicação a partir do tamanho do escopo definido,  médio-grande, em um prazo curto-médio, de 4 a 5 meses, pois a Framework utiliza-se, principalmente, da construção de um Backlog e de Sprints.
Com base nos aspectos da equipe, o Scrum se alinha com o conhecimento prévio possuído pelos desenvolvedores. Dado que todos envolvidos no projeto possuem pouca experiência na concepção de softwares complexos, o scrum certamente é uma boa ideia por possibilitar, com certa facilidade, o melhor planejamento da resolução de pendências que eventualmente surgirem no fim de cada sprint.
Considerando os aspectos da organização, o Scrum possibilita um desenvolvimento do produto sem ter todas as etapas especificadas previamente, isso facilitaria o planejamento de todo o projeto. Além disso, com as sprints semanais a equipe teria uma melhor produtividade e organização de todo o desenvolvimento do produto.      
.As principais práticas, baseadas no método Scrum, que serão utilizadas pela equipe são: planejamento da sprint, daily scrum, sprints de uma semana de duração, retrospectiva da sprint, com sprint review ao final de cada sprint, rotatividade dos papéis de Product Owner e Scrum Master com o objetivo de que cada membro ganhe experiência diferentes de não apenas ser Desenvolvedor, utilização do quadro kanban que será o ZenHub do GitHub, além de pair pairing e planning poker.


### 2.2 Processo e Procedimentos

| Atividade | Objetivo | Papel | Método | Ferramenta |
| :-----:| :------: | :---------: | :--------: | :------------: |
| Estabelecer escopo do produto | Estabelecer funcionalidades e definir as características que devem estar presentes no produto. | Product Owner e Equipe de  desenvolvimento | Reunião em que será definido o escopo do produto e organizá-lo em uma planilha | Google Sheets |
| Organizar sprint | Planejar o Backlog  da Sprint. | Product Owner, Scrum master e Equipe de  desenvolvimento | Reuniões no começo da semana para definir o backlog e alinhamento da equipe | GitHub/ZenHub |
| Executar Sprint | Concluir todas as atividades determinadas pelo Backlog | Equipe de Desenvolvimento | Distribuição dos requisitos para os membros da equipe | GitHub/ZenHub e Django/Python |
| Reuniões Diárias | Acompanhar o desenvolvimento das funcionalidades da Sprint. | Equipe de  desenvolvimento | Exposição das atividades realizadas no dia e planejamento do dia seguinte. | Microsoft Teams |
| Controlar Versões do Produto | Administrar os diferentes branches do produto para que seja possível voltar à versões mais estáveis caso necessário. | Desenvolvedor | Desenvolvimento de novas funcionalidades através do versionamento do projeto. | Git/GitHub |
| Definição de protótipo de baixa/média fidelidade | Criar protótipos de telas que serão utilizadas como base para desenvolvimento da aplicação web. | Desenvolvedor | | Elaborar páginas que servirão de base para desenvolver front-end. | Figma |
| Criar interface da tela | Concluir as telas da aplicação WEB | Desenvolvedor | Códigos html buscando desenvolver a interface de acordo com o protótipo de baixa/média fidelidade | HTML/CSS | 
| Deployment | Criar um link para o projeto poder ser acessado por qualquer pessoa. | Desenvolvedor | Deploy no Github Pages | GitHub Pages |
| Entregar o produto | Entregar produto (MVPs) para o cliente | Product Owner | Commit no Github | GitHub |

## 3. Lições Aprendidas

### 3.1 Unidade 1
As principais lições aprendidas pela equipe Gama foram: organização e pré-concepção de um projeto de software, diferença entre abordagens ágeis e dirigidas a plano,  disciplinas de Engenharia de Software, Framework Scrum. As ações a serem tomadas para melhorar são: o ambiente de desenvolvimento,  execução das reuniões diárias, definição dos requisitos, criação de protótipos de telas para basear a codificação do site da aplicação e nivelamento dos conhecimentos da equipe.

### 3.2 Unidade 2
### 3.3 Unidade 3
### 3.4 Unidade 4
### 3.5 Unidade 5

## 4. Referências Bibliográficas

SOMMERVILE, I. Processos de software. In: SOMMERVILLE, I. Engenharia de software. 9. ed. rev. São Paulo: Pearson, 2011.
