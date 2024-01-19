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

def doTranscription(dnaSequence: str) -> tuple: 
    print (f"the DNA Sequence is {dnaSequence}.\n")
    print("You need to enter the correct RNA sequence based on this DNA sequence.\n")
    print("Remember, the RNA Base will have a U base to match with an A base from DNA.\n")
    # START TIMER
    rnaStart = time.time()
    rnaSequence = input("Please type the correct RNA sequence with no spaces. Then press enter.\n").upper()
    rnaStop = time.time()
    rnaTime = rnaStart - rnaStop
    return (rnaSequence, rnaTime) # Tuples are ORDERED (index), UNCHANGEABLE, Allows Duplicates

def checkSequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    for rnaBase, dnaBase in zip(rnaSequence, dnaSequence):
        if rnaBase == "U" and dnaBase != "A":
            break
        elif rnaBase == "A" and dnaBase != "T":
            break
        elif rnaBase == "G" and dnaBase != "C":
            break
        elif rnaBase == "C" and dnaBase != "G":
            break
        else:
            isMatch = True
    return isMatch

def calcScore(time: float, dnaSequence: str) -> int:
    score = 0
    if time < 5.0:
        score += 10000
    elif time < 8.0:
        score += 7500
    elif time < 11.0:
        score += 5000
    elif time < 14.0:
        score += 2500
    else:
        score += 1000
    
    if len(dnaSequence) >= 25:
        score *= 3.5
    elif len(dnaSequence) >= 20:
        score *= 2.0
    elif len(dnaSequence) >= 15:
        score *= 1.5
    elif len(dnaSequence) <= 5:
        score *= 0.8 
    return score


def saveScore(dna: str, rna: str, rnaTime: float, score: int) -> None: 
    firstName = input("What is your first name?\n")
    lastName = input("What is your last name?\n")
    fullName = firstName + " " + lastName

    # Saving Files Example
    # Create the file name to use for your program.
    fileName = "dnaReplicationScore" + fullName + ".txt"
    # My Example: dnaReplicationScoreAidanMoody.txt


gameIntro()

dna = genDNA()
print(dna)

rna = doTranscription(dna)
print(rna)

print(checkSequence(dna, rna[0]))