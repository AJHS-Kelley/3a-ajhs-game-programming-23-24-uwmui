# DNA Replication Game, Aidan Moody, v0.0a

# Import Entire Module
import time, datetime # BRING THE WHOLE TOOLBOX

# Import Specific Method from a Module
from random import choice # BRING JUST THE TOOL YOU NEED

dnaBases = ["A", "T", "G", "C"] # Adenine, Thymine, Guanine, Cytosine

def gameIntro() -> None:
    print("Welcome to the DNA Replication game!!\n In this game you will be generating DNA sequences and matching the correct RNA sequences to them.\n For example; A to T, T to U, etc.\n")

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("Please enter a positive integer value for the number of bases to generate.\n"))
    dnaSequence = ""    
    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    return dnaSequence

def genRNA(dnaSequence: str) -> tuple: 
    print (f"the DNA Sequence is {dnaSequence}.\n")
    print("You need to enter the correct RNA sequence based on this DNA sequence.\n")
    print("Remember, the RNA Base will have a U base to match with an A base from DNA.\n")
    # START TIMER
    rnaStart = time.time()
    rnaSequence = input("Please type the correct RNA sequence with no spaces. Then press enter.\n")
    rnaStop = time.time()
    rnaTime = rnaStart - rnaStop
    return (rnaSequence, rnaTime) # Tuples are ORDERED (index), UNCHANGEABLE, Allows Duplicates

def checkSequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    for rnaBase, dnaBase in zip(rnaSequence, dnaSequence):
        if rnaBase == "U" and dnaBase != "T":
            break
        elif rnaBase == "T" and dnaBase != "A":
            break
        elif rnaBase == "G" and dnaBase != "C":
            break
        elif rnaBase == "C" and dnaBase != "G":
            break
        else:
            isMatch = True
    return isMatch

gameIntro()

dna = genDNA()
print(dna)

rna = genRNA(dna)
print(rna)

print(checkSequence(dna, rna))