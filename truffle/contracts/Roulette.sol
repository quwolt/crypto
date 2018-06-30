pragma solidity ^0.4.0;

contract Roulette {
    mapping(address => uint) balances;
    function betRed () payable {
        bool winner = (randomNumber() % 2 == 0);
        if (winner)
            balances[msg.sender] += msg.value * 2;
    }
    function randomNumber() returns (uint) {
    // we will implement this in a later section
    // for now, imagine it returns a number from
    // 0-36
    }
    function withdraw () {
        uint amount = balances[msg.sender];
        balances[msg.sender] = 0;
        msg.sender.transfer(amount);
    }
}
