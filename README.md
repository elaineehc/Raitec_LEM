Aplicativo LEM (versão 10/05/2025)  
Laboratório de Ensaio de Materiais

## Criar o executável
Para criar o executável é necessário instalar o PyInstaller:

<pre> pip install pyinstaller </pre>

Depois basta rodar a linha abaixo do diretório onde se encontra o arquivo converteForca.py.
<pre> pyinstaller --onefile converteForca.py </pre>

## Rodar o executável
O executável é criado na pasta dist, que está no mesmo diretório do arquivo converteForca.py, e precisa de 3 informações de entrada:
- O caminho do arquivo .csv dos dados coletados
- A escala adotada (50kg, 100kg ou 200kg)

Essas informações devem ser passadas da seguinte forma:
<pre> converteForca.exe "caminho/arquivo/dados.csv" --escala VALOR_ESCALA</pre>

## Saídas
O executável retorna:
- um arquivo .csv contendo as informações calculadas (em 1000kgf, tonelada-força) no mesmo diretório do arquivo usado como entrada
- uma imagem contendo o gráfico plotado dentro da pasta dist
