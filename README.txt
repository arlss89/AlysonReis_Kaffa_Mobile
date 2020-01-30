# AlysonReis_Kaffa_Mobile
Este repositório faz parte da solução do teste para pré-seleção para estágio da Kaffa_Mobile. Candidato: Alyson Reis


############ Instruções##########
OBS: Como é pedido a solução em software tipo opensource, este arquivo pode ser aberto em um bloco de notas, sendo totalmente gratuito

Candidato: Alyson Reis dos Santos.
Contatos:	alyson.santos@fatec.sp.gov.br
arlss89@gmail.com
(19)99104-9754

                                      Kaffa – Pre-Qualification test (v1.1)

Exercícios resolvidos: 1, 2, 3, 4, e 8.
Apenas os algoritmos dos exercícios de 1 a 4 demandam instruções, a resolução do exercício 8 é dada através da imagem presente no item 4.

################Instalação do Software######################
1.	Instruções para instalação da IDE utilizada para resolução dos problemas:

a)	A IDE utilizada foi o “Pycharm Community Edition 2019.3.2” é uma IDE open source, como mandam os requisitos. Disponível em: https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC;
b)	Faz-se necessário instalar um interpretador para o pycharm funcionar corretamente, utilizando-se da linguagem python. Disponível em: https://www.python.org/ftp/python/3.8.1/python-3.8.1.exe.

2.	Para rodar e verificar as soluções:
a)	Após os passos relatados em a) e b) do item anterior, deve-se abrir o programa “pycharm”;
b)	Em “file -> open” selecionar a pasta chamada “Kaffa_Mobile”;
c)	Na barra lateral esquerda “Project” selecionar a opção “Project Files”;
d)	Abrir a pasta do exercício que deseja verificar a solução;
e)	Para verificar as linhas de código prosseguir com clique duplo;
f)	Para rodar a solução, pular o item e), clicar com o botão direito do mouse e clicar em “Run ‘exercícioDesejado’”;
g)	Seguir as orientações na barra “Run”,  que geralmente fica na parte inferior da tela, abaixo da barra lateral esquerda “Project”.

3.	Sobre a entrada de dados:

a)	Exercício 1 – os dados de entrada podem ser de qualquer tipo, contudo, caso não seja no formato “00.000.000/0000-00” ou “00000000000000”, será dada uma mensagem de erro. Dados que dão mensagens inválidas: letras em alguma das posições nos formatos de exemplo; caso tenha um número diferente de 14 dígitos;
b)	Exercício 2 – está inserido no mesmo código do exercício 1 e a solução é dada quando o usuário seleciona que deseja verificar se o cnpj é válido. OBS: no exercício 1, se o usuário entrar somente com números não ocorrerá erros; já no exercício 2, caso os números não sejam de um cnpj válido o usuário será informado (neste caso ser válido não significa que é existente);
c)	Exercício 3 – os dados de entrada são pares de retângulos e cada retângulo é definido por coordenadas do tipo (x1, y1, x2, y2), sendo que o usuário deve entrar conforme forem pedidos ao mesmo. Não importa se x1>x2 ou se y1>y2 contanto que a sequência seja dada conforme o tipo (o programa organiza o vetor de coordenadas);
d)	Exercício 4 – Ao final da verificação da interseção (exercício 3), caso esta ocorra ou não, será possível calcular a área dela (exercício 4). Caso não ocorra, é natural que a interseção seja 0.

4.	Resolução do exercício 8
O exercício 8 foi resolvido utilizando uma ferramenta gratuita online para o desenho de diagramas, entre eles o UML, dentre eles o de entidade-relacionamento. Com isso, como requerido pelo enunciado, o “Order Manager System”  deve conter as classes: Clientes, Produtos e Ordens. Destes, foram identificados alguns parâmetros (no formato “parâmetro: tipo”), conforme a tabela 1, mostrada abaixo:

Clientes	        Produtos	              Ordem_Produto	          Ordem_Geral
ID_cliente:       int	ID_produto: int	    ID_ordem: int	          ID_ordem: varchar
Nome: varchar	    Nome: varchar	          Descricao: varchar	    ID_cliente: int
End: varchar	    Preco: float	          ID_produto: int	        Data: Date
CEP: int	        Descricao: varchar	    Quantidade: int	        Valor: float
	Estoque: int	  Preco: float	


Com base na tabela 1, tem-se o modelo de entidade-relacionamento mostrado na figura 1, mostrada abaixo:
 
Figura 1 - Modelo de Entidade Relacionamento exercício 8. Fonte: Do autor. Disponível no link:https://www.lucidchart.com/invitations/accept/8e74c021-5c8a-4819-be1e-6f1bb544bace
