import hashlib


def buildMerkleTreeFromArray(arr):
    # Base case: If only one element remains, it's the root of the Merkle tree
    if(len(arr) == 1):
        return arr[0]
    
    levelUpArray = [] # To store the hashes one level up the current level in the tree.

    for i in range(0, len(arr), 2):

        firstHash = hashlib.sha256(arr[i].encode()).hexdigest()

        # If there is only one element left at last, we duplicate it to get the other one.
        if((i+1) < len(arr)):
            secondHash = hashlib.sha256(arr[i+1].encode()).hexdigest()
        else:
            secondHash = hashlib.sha256(arr[i].encode()).hexdigest()
        
        levelUpArray.append(hashlib.sha256((firstHash + secondHash).encode()).hexdigest())
    
    return buildMerkleTreeFromArray(levelUpArray)



arr = ["tx1", "tx2", "tx3", "tx4"]

print(buildMerkleTreeFromArray(arr))
