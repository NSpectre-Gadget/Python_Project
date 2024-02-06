// SPDX-License-Identifier: MIT
pragma solidity >=0.4.0 <0.9.0;
//version of solidity

contract Deliverables_contract{
//name of the contract    

    address drafter;
    string name;
    string deliverable_type;
    string desc;
    uint deliverable_status;

    event createDeliverableEvent(address indexed _drafter,string _name, string _deliverable_type, string _desc);
    // an event with defining the deliverable filed

    //function to create an  investigation deliverable with the name of the filer, the type of deliverable, with the deliverable description
    // initial state of deliverable will be 1
    function createDeliverable(string memory _name, string memory _deliverable_type, string memory _desc) public {
        drafter = msg.sender;
        name = _name;
        deliverable_type = _deliverable_type;
        desc = _desc;
        deliverable_status = 1;
        emit createDeliverableEvent(drafter,name,deliverable_type,desc);
    }

    // function getDeliverable() will simply display the details of the latest deliverable filed
    // function wil display the name of the drafter, the type of deliverable, its description and the current status
    function getDeliverable() public view returns(
        address _drafter,string memory _name, string memory _deliverable_type, string memory _desc, uint _deliverable_status){
        return(drafter,name,deliverable_type,desc,deliverable_status);
    }

    // function setStatus() will simply update the status of the deliverable filed by the drafter 
    function setStatus(uint _deliverable_status) public{
        deliverable_status = _deliverable_status;
    }
}