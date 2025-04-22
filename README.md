Aplicativo LEM (primeira versão)  
Laboratório de Ensaio de Materiais

## Criar o executável
Para criar o executável é necessário instalar o PyInstaller:

<pre> pip install pyinstaller </pre>

Depois basta rodar a linha abaixo do diretório onde se encontra o arquivo main.py.
<pre> pyinstaller --onefile main.py </pre>

## Rodar o executável
O executável é criado na pasta dist, que está no mesmo diretório do arquivo main.py, e precisa de 3 informações de entrada:
- O caminho do arquivo .csv dos dados coletados
- Alguma informação do corpo de prova (área ou diâmetro, pelo menos uma das duas)
- A escala adotada (no momento, 50kg ou 100kg)

Essas informações devem ser passadas da seguinte forma:
<pre> main.exe caminho/arquivo/csv.csv --area VALOR_AREA --diametro VALOR_DIAMETRO --escala VALOR_ESCALA</pre>
O valor da área ou do diâmetro pode ser omitido, mas nunca ambos.

## Saídas
O executável retorna:
- um arquivo .csv contendo as informações calculadas (Força (N) e Tensão (Pa)) no mesmo diretório do arquivo usado como entrada
- uma imagem contendo o gráfico plotado dentro da pasta dist
