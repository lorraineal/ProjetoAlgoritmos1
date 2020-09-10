# ProjetoAlgoritmos1
Projeto da cadeira de Algoritmos 1. 

## Atividades Resolvidas

O projeto se encontra parcialmente completo. As seguintes atividades foram implementadas.

Tarefa 1: Obtenha os arquivos todo.txt e agenda.py a partir do material postado no Classroom.

Tarefa 2: Crie manualmente um arquivo todo.txt e inclua nele diversos compromissos como os apresentados nesta seção. Invente novos compromissos, porém, para ter um arquivo que lhe ajude a testar todas as funcionalidades do programa que você vai construir. Seu arquivo também deve incluir algumas atividades fora do formato especificado, por exemplo, com uma data com menos que 8 dígitos, para verificar como seu programa se comporta. O número total deatividades desse arquivo deve ser maior ou igual a 20 e deve contemplar todas as funcionalidades da aplicação.

Tarefa 3: Complete a implementação da função horaValida() . Essa função recebe um string e verifica se ele tem exatamente quatro caracteres, se tão todos dígitos, se os dois primeiros formam umnúmero entre 00 e 23 e se os dois últimos formam um número inteiro entre 00 e 59. Se tudo isso for verdade,ela devolve True. Caso contrário, False. O arquivo já inclui uma função auxiliar para verificar se todos os caracteres de um string são dígitos.

Tarefa 4: Implemente a função dataValida() . Essa função recebe um string e verifica se ele tem exatamente oito caracteres, se tão todos dígitos e se os dois primeiros correspondem a um dia válido, se o terceiro e o quarto correspondem a um mês válido e se os quatro últimos correspondem a um ano
válido. Sua função deve checar também se o dia e o mês fazem sentido juntos. Além de verificar se o mês é um número entre 1 e 12, dataValida() deve checar se o dia poderia ocorrer naquele mês, por exemplo, ela deve devolver False caso o dia seja 31 mas o mês seja 04, que tem apenas 30 dias. O ano
pode ser qualquer número de 4 dígitos. Para fevereiro, considere que pode haver até 29 dias, sem se preocupar se o ano é bissexto ou não. Se todas as verificações passarem, a função devolve True. Caso contrário, False.

Tarefa 5: Implemente a função projetoValido(). Essa função recebe um string e verifica se ele tem pelo menos dois caracteres e se o primeiro é ‘+’. Devolve True se as verificações passarem e False caso contrário.

Tarefa 6: Implemente a função contextoValido(). Essa função recebe um string e verifica se ele tem pelo menos dois caracteres e se o primeiro é ‘@’. Devolve True se as verificações passarem e False caso contrário.

Tarefa 7: Implemente a função prioridadeValida(). Essa função recebe um string e verifica se ele tem exatamente três caracteres, se o primeiro é ‘(’, se o terceiro é ‘)’ e se o segundo é uma letra entre A e Z. A função deve funcionar tanto para letras minúsculas quanto maiúsculas. Devolve True se as
verificações passarem e False caso contrário.

Tarefa 8: Complete a implementação da função organizar(). Como dito antes, essa função recebe uma lista de strings representando atividades e devolve uma lista de objetos com as informações dessas atividades organizadas. Para completar essa função, será necessário complementar a implementação da classe Compromisso. Note que seus atributos, exceto pela descrição, são opcionais.

Tarefa 9: Complete a implementação da função adicionar(), que adiciona um compromisso à agenda. Um compromisso tem no mínimo uma descrição. Adicionalmente, pode ter, em caráter opcional, uma data, um horário, um contexto e um projeto. Esses itens opcionais são recebidos através do parâmetro extras, o segundo parâmetro da função. Esse parâmetro pode ser passado como você preferir. Todos os elementos extras precisam ser validados (com as funções definidas nas tarefas anteriores). Qualquer elemento que não passe pela validação deve ser ignorado.

