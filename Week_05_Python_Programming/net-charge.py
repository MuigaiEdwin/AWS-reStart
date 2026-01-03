#This lab applies Python lists, loops, and dictionaries to a real-world problem — calculating the net charge of human insulin across pH levels from 0 to 14.

# Store the human preproinsulin sequence
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  

# Store the remaining sequence elements of human insulin
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  

# Combine the insulin chains
insulin = bInsulin + aInsulin

# pKa values for certain amino acids
pKR = {
    'y': 10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25
}

# Count the number of each charged amino acid
seqCount = {x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']}

# Loop through pH values from 0 to 14
pH = 0
while pH <= 14:
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x])) / ((10**pH)+(10**pKR[x]))) for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH)) / ((10**pH)+(10**pKR[x]))) for x in ['y','c','d','e']}.values()))
    )
    print('{0:.2f}'.format(pH), netCharge)
    pH += 1

