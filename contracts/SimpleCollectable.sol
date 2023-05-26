// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract SimpleCollectable is ERC721URIStorage {
    uint256 public tokenCounter;
    string public nftName;
    event NFTName(string _name);

    constructor(string memory _name) ERC721("INFUSION", "IA") {
        tokenCounter = 0;
        nftName = _name;
    }

    function createCollectibles(
        string memory tokenURI
    ) public returns (uint256) {
        uint256 tokenId = tokenCounter;
        _safeMint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        emit NFTName(nftName);
        tokenCounter++;
        return tokenId;
    }
}
