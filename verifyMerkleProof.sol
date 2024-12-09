// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract MerkleProof {
    function verify(bytes32[] memory proof, bytes32 root, bytes32 leaf, uint index) public pure returns (bool) {
        
        bytes32 hash = leaf; // The hash of the leaf node.

        for (uint i = 0; i < proof.length; i++) {

            bytes32 proofElement = proof[i]; // The element which pairs up with the current node for hashing.

            if (index % 2 == 0) {
                hash = keccak256(abi.encodePacked(hash, proofElement));
            } else {
                hash = keccak256(abi.encodePacked(proofElement, hash));
            }

            index = index / 2;
        }

        return hash == root;
    }
}