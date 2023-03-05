import random

R_INTROJIRA1 = "jira é um aplicativo de software desenvolvido pela empresa de software australiana Atlassian que permite que as equipes rastreiem problemas, gerenciem projetos e automatizem fluxos de trabalho."
R_INTROJIRA2 = "A configuração do Jira Software depende de suas necessidades. Primeiro, você precisa criar um projeto para gerenciar seu trabalho. Depois, você pode adicionar usuários e definir as permissões de acesso. Você também pode personalizar os campos e as telas para atender às suas necessidades específicas. Além disso, você pode configurar fluxos de trabalho, notificações e integrações com outros sistemas."
R_INTROJIRA3 = "Acesse o site do Jira Software e faça login na sua conta.  2. Clique no botão Criar Projeto na parte superior da página inicial. 3. Selecione o tipo de projeto que você deseja criar (por exemplo, Agile, Scrum ou Kanban). 4. Insira um nome para o seu projeto e uma descrição opcional. 5. Selecione um modelo de projeto para ajudar a configurar as etapas do seu projeto (por exemplo, software, serviços ou marketing). 6. Selecione os membros da equipe que participarão do projeto e defina as permissões de acesso para cada um deles."
R_INTROJIRA4 = "1. Gerenciamento de Projetos: O Jira Software oferece recursos para ajudar os usuários a gerenciar projetos, como criação de quadros Kanban e Scrum, rastreamento de tarefas e controle de tempo, além de recursos avançados como relatórios e gráficos. 2. Gerenciamento de Bugs: O Jira Software possui ferramentas robustas para ajudar os usuários a identificar, rastrear e resolver bugs rapidamente. 3. Integração com outras ferramentas: O Jira Software pode ser facilmente integrado com outras ferramentas, como GitHub, Bitbucket, Slack e Confluence. Isso permite que os usuários trabalhem em conjunto em projetos sem ter que sair do ambiente do Jira Software.4. Gerenciamento de Riscos: O Jira Software oferece recursos para ajudar os usuários a identificar e gerenciar riscos potenciais associados a um projeto ou atividade específica."
R_INTROJIRA5 = "1. Crie um projeto: Primeiro, crie um projeto no Jira Software para gerenciar suas tarefas. Você pode usar modelos pré-configurados ou configurar seu próprio projeto. 2. Adicione tarefas: Agora, adicione tarefas ao seu projeto. Você pode adicionar tarefas individuais ou criar grupos de tarefas relacionadas. 3. Atribua tarefas: Atribua as tarefas aos usuários responsáveis ​​usando a funcionalidade de atribuição do Jira Software. Isso permitirá que você saiba quem está trabalhando em qual tarefa e quando ela deve ser concluída. 4. Acompanhe o progresso: Use o recurso de visualização do Jira Software para acompanhar o progresso das suas tarefas e verificar se elas estão sendo concluídas dentro do prazo previsto. 5. Gerencie alterações: Use o recurso de controle de versão do Jira Software para gerenciar quaisquer alterações nas suas tarefas e manter todos os envolvidos informados sobre as atualizações mais recentes."
R_INTROJIRA6 = "1. Acesse a página de relatórios do Jira Software. Você pode encontrá-la na barra lateral esquerda da sua tela inicial. 2. Selecione o tipo de relatório que deseja criar, como por exemplo, um gráfico de barras, gráfico de pizza ou tabela de dados. 3. Escolha as informações que deseja incluir no seu relatório, como por exemplo, o número total de tarefas concluídas, tempo médio para conclusão das tarefas e assim por diante. 4. Selecione os filtros que deseja aplicar ao seu relatório, como por exemplo, data inicial e final do período de tempo que deseja analisar ou usuários específicos envolvidos nas tarefas. 5. Clique em “Gerar Relatório” para visualizar os resultados em seu navegador."
R_INTROJIRA7 = "1. Crie uma estrutura de projetos eficaz: Defina as estruturas de projetos adequadas para seus times e crie fluxos de trabalho que ajudem a maximizar a produtividade. 2. Utilize os recursos de gerenciamento de tempo: O Jira oferece recursos como o Gerenciamento de Tempo, que permite que os usuários rastreiem o tempo gasto em tarefas específicas. Isso ajuda a manter o controle do progresso dos projetos e identificar possíveis gargalos. 3. Use as ferramentas de relatórios: O Jira oferece várias ferramentas para criar relatórios detalhados sobre o progresso dos projetos, incluindo gráficos, tabelas e outros tipos de visualização. Esses relatórios podem ser usados para identificar problemas e tomar decisões informadas. 4. Utilize os recursos colaborativos: O Jira oferece várias ferramentas colaborativas, como discussões, comentários e tarefas compartilhadas entre membros do time. Isso facilita a comunicação entre os membros do time e melhora a produtividade geral. 5. Use as notificações: O Jira oferece notificações por email para alertar os usuários sobre atualizações importantes nos projetos em andamento. Isso garante que todos estejam sempre atualizados sobre o progresso dos projetos e possam tomar decisões informadas rapidamente."
R_INTROJIRA8 = "Para personalizar o layout do Jira, você pode usar o tema de interface do usuário do Jira. O tema permite alterar a cor e o estilo da interface do usuário para que seja mais adequado às suas necessidades. Você também pode criar seus próprios temas personalizados, adicionando imagens, fontes e outros elementos de design. Além disso, é possível alterar a disposição dos campos e das colunas na visualização de lista para melhorar a experiência do usuário."

def unknown():
    response = ["Eu nao entendi, poderia tentar novamente?",
                "Hum, nao encontrei essa informacao",
                "Preciso verificar!",
                ][
        random.randrange(4)]
    return response