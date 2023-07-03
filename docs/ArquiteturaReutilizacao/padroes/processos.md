## Histórico de Alterações

| Versão | Descrição                                          | Responsáveis                                 | Data       |
| ------ | -------------------------------------------------- | -------------------------------------------- | ---------- |
| 1.0    | Criação do documento e desenvolvimento da visão de processos | [Murilo Perazzo](https://github.com/murilopbs) | 03/07/2023 |

# Introdução
Este documento apresenta a visão arquitetural relacionada ao processo de troca e devolução da empresa RiHappy. O objetivo é fornecer uma visão geral das tarefas, interações e configurações envolvidas nesse processo.

A visão arquitetural do processo é fundamental para compreender a estrutura e o fluxo de trabalho relacionados à troca e devolução de produtos. Ela ajuda a identificar as responsabilidades das diferentes partes envolvidas e a visualizar como essas partes interagem entre si.

# Escopo
A visão arquitetural do processo de troca e devolução da RiHappy abrange desde o momento em que o cliente solicita a troca ou devolução de um produto até a conclusão do processo. Isso inclui a interação com a aplicação responsável por receber as informações do produto, verificar a possibilidade de troca e gerenciar as etapas subsequentes.


# Diagrama de Sequência
  <br>![image](https://github.com/UnBArqDsw2023-1/2023.1_G6_ProjetoRiHappy/blob/main/docs/ArquiteturaReutilizacao/imagens/Diagramadesequenciaprocessosjpeg)
# Descrição das Tarefas
- Receber informações do produto:
  - Essa tarefa envolve a interação entre o cliente e a aplicação da RiHappy. O cliente fornece as informações necessárias sobre o produto que deseja trocar ou devolver.

- Verificar a possibilidade de troca:
  - Nesta tarefa, a aplicação realiza uma verificação das condições necessárias para que o produto seja passível de troca. Isso pode incluir a validação de prazos, condições de uso, embalagem, entre outros critérios.

- Decidir o tipo de troca:
  - Com base na verificação anterior, a aplicação determina o tipo de troca que pode ser oferecido ao cliente. Isso pode incluir a troca em uma loja física, a troca pelo WhatsApp ou a troca por meio de um marketplace parceiro.
- Gerenciar o processo de troca:
  - Essa tarefa abrange as etapas de logística e comunicação necessárias para concluir a troca ou devolução do produto. Isso pode incluir a geração de autorização de postagem, o envio de informações ao cliente e a coordenação com a equipe responsável pela logística reversa.


 # Interações e Configurações
A interação principal ocorre entre a aplicação da RiHappy e o cliente, no momento em que as informações do produto são recebidas.
Quanto às configurações, a aplicação deve ser configurada para se integrar com os diferentes canais de troca disponíveis, como lojas físicas, WhatsApp e marketplaces. Também é necessário configurar os critérios de validação para a verificação da possibilidade de troca.


# Conclusão
A visão arquitetural do processo de troca e devolução da RiHappy apresentada neste documento fornece uma visão geral das tarefas, interações, configurações. Essa visão é essencial para compreender a estrutura e o fluxo de trabalho envolvidos, auxiliando no desenvolvimento e na evolução do sistema responsável por gerenciar as trocas e devoluções de produtos.
