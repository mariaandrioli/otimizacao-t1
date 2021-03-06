## Índice
* [Descrição](#descricao)
* [Instalação](#instalacao)
* [Execução](#execucao)
* [Testes](#testes)


## Descrição
Trabalho 1 da disciplina CI1238 - Otimização, no semestre 2021/1.  
[Especificação do projeto](docs/especificacao.pdf).  
[Relatório](docs/texto.pdf).
	
## Instalação
Para instalar dependências e gerar o executável `./escolha`
```
make
```
	
## Execução
O programa recebe da entrada padrão o seguinte:

> Inicia com dois números, n e c representando, respectivamente, o número de sedes e o número de conexões que podem ser instaladas. Assuma que as sedes são numeradas de 1 a n. Em seguida temos uma linha com três números representando a sede de origem (o), a sede de destino (d), e a demanda de transmissão de o para d. As próximas c linhas, representando os custos, são formadas por três números representando as duas sedes e o custo de instalação desta conexões por unidade de capacidade de transmissão (nas duas direções).

```
./escolha < arquivo_de_teste
```

E gera como saída o arquivo `output.lp` que funciona como entrada para o [lp_solve](http://web.mit.edu/lpsolve/doc/)

## Testes
O script `./escolha.sh` aplica o make depois realiza testes com os arquivos dentro da pasta [/testes](/testes)

```
./escolha.sh
```