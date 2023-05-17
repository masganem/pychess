```
  a b c d e f g h
8 ♖ □ ■ ■ ♔ □ ■ ♖
7 ♙ ♗ □ ♘ □ ♙ □ ♙
6 ■ □ ♙ ♙ ■ ♘ ♙ ♛
5 □ ♙ □ ■ ♙ ■ □ ■                           ♘ PYCHESS ♘
4 ■ □ ■ ♟︎ ♟︎ □ ■ □
3 ♟︎ ■ ♞ ■ □ ♟︎ □ ■
2 ■ ♟︎ ♟︎ □ ♞ □ ♟︎ ♟︎
1 ♜ ■ □ ■ ♚ ♝ □ ♜
```

Um jogo de xadrez implementado em Python para a linha de comando.

O tabuleiro é exibido com caracteres UTF-8 em alinhamento `monospace`. As peças podem ser movimentadas utilizando uma notação personalizada, que aqui vamos de chamar de **notação de coordenadas**. Ela é simplesmente composta por dois pares de coordenadas: o movimento `a2b4`, indica que a peça na posição `a2` vai se mover para o quadrado `b4`, por exemplo.

O código implementa todas as regras de negócio para viabilizar um jogo fluido de xadrez. A única exceção para esta regra é o movimento de *castling*, que ainda não foi implementado ~~porque seria muito complexo~~. Dá até pra promover os seus peões ♙ -> ♕!

Além disso, é possível consultar todos os movimentos válidos a partir de uma determinada peça, como nos jogos de xadrez eletrônicos contemporâneos. Para fazer isso, basta digitar somente a primeira parte do movimento: `a2` mostra todos os movimentos permitidos para a peça no quadrado `a2`, por exemplo.

Por fim, também é possível salvar as partidas jogadas para fazer um replay depois. O jogo conta com um modo de execução alternativo que pode exibir os jogos de relatórios passados, mostrando cada um dos lances jogados.

## Pré-requisitos
- Python >= 3.10
- Um terminal com fonte `monospace`.

## Executando
Para iniciar um novo jogo, basta estar no diretório do projeto e executar o comando `python main.py`. Ao final do jogo (após o xeque-mate), será possível salvar o relatório da partida jogada com um nome personalizado. Para abrir o replay de uma partida, basta executar `python main.py <nome da partida>`. O relatório de uma partida trivial ([Fool's Mate](https://en.wikipedia.org/wiki/Fool%27s_mate)) está incluso dentro da pasta `games`, e pode ser executado com `python main.py foolsmate`.

Também temos um ambiente no [Repl.it](https://replit.com/@masganem/pychess?v=1) para executar o jogo remotamente.

## Detalhes de implementação
O sistema obedece a uma arquitetura (razoavelmente) orientada a objetos, com duas classes principais, chamadas de `PlayerInterface` e `ReplayInterface`, respectivamente, que conduzem os dois fluxos de uso de mais alto nível do programa.
Ambas as classes fazem uso de um `Controller` para gerenciar o estado do jogo, que é responsável por analisar a legalidade dos movimentos executados, verificar estados de promoção de peões, xeque-mate, entre a garantia de outras regras.

O `Controller`, por sua vez, utiliza de um `Board`, composto por um mapa de 64 `Tile`s, que contém suas respectivas `Piece`s. Essa classe, naturalmente, é responsável pela representação posicional do tabuleiro e suas peças.

Com a coordenação das operações das classes aqui descritas (e mais alguns truques de código), a funcionalidade do jogo é servida ao usuário final pela linha de comando em um display que utiliza o texto para permitir uma experiência gráfica.

---
Desenvolvedores:
- Marcelo Augusto Salomão Ganem
- Gabriel Medeiros Teixeira
- Rafael Vinícius dos Santos
