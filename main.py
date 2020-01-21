"""
https://stackoverflow.com/questions/11587044/how-can-i-create-a-tree-for-huffman-encoding-and-decoding
"""
import queue 

# funzione che legge un testo e crea un dizionario con le frequenze
def preprocessing(text):
  # creo un dizionario con le frequenze di ogni lettera
  d = {}
  for char in text:
    # se un carattere non è già presente viene inserito con il valore iniziale 0
    # altrimenti viene incrementata la sua frequenza
    d[char] = d.get(char, 0) + 1
  return d
  
# stampa dei caratteri ordinati per frequenze
def printDict(d):
  for x in sorted(d, key=d.get):
    print(x, d[x])

# classe per creare l'albero delle frequenze
class HuffmanNode(object):
  # metodo per costruire un nodo; per default viene creata una foglia ossia un nodo senza figli
  def __init__(self, left = None, right = None, char = ""):
    self.left = left
    self.right = right
    self.char = char    # char è il carattere associato al nodo
  # workaround to fix the bug when two elements in the priority queue have the same frequence
  def __lt__(self,other):
    return 0

# funzione per creare l'albero di Huffman dato il dizionario delle frequenze
def createTree(freq):
  p = queue.PriorityQueue()
  # 1. inizializzazione della coda di priorità
  # per ogni carattere nel dizionario freq creo un nodo foglia formato da (frequenza, lettera) e lo inserisco nella coda p
  for e in freq:
    new_n = HuffmanNode(None, None, e)
    new_e = (freq[e], new_n)
    p.put(new_e)
  # 2. finchè ci sono almeno due nodi nella coda vado avanti con il ciclo
  while(p.qsize() > 1):
    # 2a. estraggo i primi due elementi
    l, r = p.get(), p.get()
    # 2b. creo un nodo con i due elementi estratti 
    new_n = HuffmanNode(l[1], r[1])
    # 2c. e lo inserisco nella coda
    new_e = (l[0] + r[0], new_n)
    p.put(new_e)
  # 3. l'albero è completo, estraggo l'ultimo elemento nella coda che è la radice
  return p.get()

# funzione che riceve un nodo radice dell'albero di Huffman e ritorna
# un dizionario con la codifica binaria dei caratteri
def createCode(node, prefix = "", code = {}):
  # controllo se il figlio sinistro è una foglia, ossia se il carattere ad esso associato non è la stringa vuota
  if(node.left.char != ""):
    # caso base: il nodo è un carattere del testo originale: mi fermo con la ricorsione
    code[node.left.char] = prefix + "0" 
  else:
    # passo ricorsivo: continuo con il sottoalbero di sinistra
    createCode(node.left, prefix + "0", code)
  # caso base: il nodo è un carattere del testo originale: mi fermo con la ricorsione
  if(node.right.char != ""):
    code[node.right.char] = prefix + "1" 
  else:
    # passo ricorsivo: continuo con il sottoalbero di destra
    createCode(node.right, prefix + "1", code)  
  return code

# Huffman algorithm: return a code for lossless compression
def compress(text):
  return

###################################################################################
# preprocessing
###################################################################################

document = open("testo.txt", "r")     
text = document.read()
document.close()
d = preprocessing(text)
root = createTree(d)
encodeDict = createCode(root[1])
# stampo il dizionario di compressione creato
for e in encodeDict:
  print(e, encodeDict[e])

###################################################################################
# compressione
###################################################################################

# sostituisco ogni carattere del testo con il suo codice e lo memorizzo in una stringa
ctext = ""
for char in text:
  ctext = ctext + encodeDict[char]

# memorizzo la stringa compressa nel file compressedtext.txt
document = open("compressedText.txt", "w")     
document.write(ctext)
document.close()

###################################################################################
# decompressione
###################################################################################

# creo il dizionario per decomprimere invertendo il dizionario usato per comprimere
decodeDict = {}
for e in encodeDict:
  decodeDict[encodeDict[e]] = e

"""
# stampo il dizionario di decompressione creato
for e in decodeDict:
  print(e, decodeDict[e])
"""

clearText = ""
word = ""
# leggo dal file contenente il testo compresso
document = open("compressedText.txt", "r")
c = document.read(1)
while(c != ""):
  word = word + c
  if(word in decodeDict):
    clearText = clearText + decodeDict[word]
    word = ""
  c = document.read(1)
print(clearText)

#codice per eseguire il file risparmio.py
import subprocess
import sys

subprocess.check_call([sys.executable, 'risparmio.py'])
