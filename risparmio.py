#leggo i file testo.txt e compresstext.txt
print("\n")
print("##############################################################")
print("ANALISI STATISTICA DEL RAPPORTO DI COMPRESSIONE E DEL GUADAGNO")
print("##############################################################")
print("\n")
document = open("testo.txt", "r")     
textNO = document.read()
document.close()
document = open("compressedText.txt", "r")     
textSI = document.read()
document.close()

#conto i bit che verrebbero utilizzati tramite codifica con tabella ASCII
nASCII = len(textNO) * 8
print ("NO compressione", nASCII, "bits")

#conto i bit che verrebbero utilizzati tramite algoritmo di Huffman
nHuffman = len(textSI)
print ("SI compressione", nHuffman, "bits" )
#calcolo la differenza 
differenza = nASCII - nHuffman
print ("Differenza di", differenza, "bits, ", differenza / 8,"Byte")

#risparmio percentuale
percentuale = int((differenza / nASCII ) * 100)
print ("Il risparmio è circa del", percentuale,"%")