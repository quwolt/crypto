var Web3 = require('web3');

// var web3 = new Web3('ws://89.223.65.203:9546');
var web3 = new Web3(new Web3.providers.HttpProvider('http://89.223.65.203:8545')); //9549 port for Rinkeby Full,  8545 port for Mainnet, 9547 port for Rinkeby LES
// console.log(web3);

// web3.eth.getAccounts(console.log);
// web3.eth.getBalance("0xfa11d0AC741eCCe206250E62A3D9725f56498674")
//     .then(console.log);
// web3.eth.getBalance("0x0B7B39BdfbA0c85e8351b34d443a800FaA1779F6")
//     .then(console.log);
// web3.eth.getBalance(web3.eth.accounts[0])


// new web3.eth.Contract([0xe76f0275872b7038e0c24093fc81bd8549728a19]);
// console.log(this.get(_address))

web3.eth.getAccounts(console.log);