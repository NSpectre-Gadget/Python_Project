// SPDX-License-Identifier: MIT

pragma >=0.6.0 <0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol;

contract AdvancedCollectible is ERC721, VRFConsumerBase {
    uint256 tokenCounter;
    bytes32 public keyhash;
    uint256 public fee;
    enum Breed{PUG, SHIBA_INU, ST_BENARD}
    mapping(uint256 => Breed) public tokenIdToBreed;
    mapping(bytes32 => requeaddress) public requestId;
    event requestedCollectible(bytes32 indexed requestId, address requester);
    event breedAssigned(uint256 indexed tokenId, Breed breed)


    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyHash, unint256 _fee) public VRFConsumerBase(_vrfCoordinator, _linkToken) ERC721("Doggie", "DOG") {
        tokenCounter = 0;
        keyhash = _keyhash;
        fee = _fee;
    }

    function createCollectible(string memory tokenURI) public returns(bytes32){
        bytes32 requestId = requestRandomness(keyhash, fee); //creates randomness request
        requestIdToSender[requestId] = msg.sender;
        emit requestedCollectible(requestId, msg.sender)
    }
    function fulfillRandomness(byes32 requestId, uint256 randomNumber) internal override {
        Breed breed = Breed(randomNumber % 3);
        uint256 newTokenId = tokenCounter;
        tokenIdToBreed[newTokenId]= breed;
        emit breedAssigned(newTokenId, breed);
        address owner = requestIdToSender[requestId];
        _safeMint(owner, newTokenId);
        // _setTokenURI(newTokenId,m tokenURI)
        tokenCounter = tokenCounter +1;
        return newTokenId;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: caller is not owner nor approved");// derived from ERC721 contract
        _setTokenURI(tokenId, _tokenURI)
        _setTokenURI(token)

    }
}
