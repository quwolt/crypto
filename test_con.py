import json
import web3
from web3 import Web3
from web3.providers.rpc import HTTPProvider



web3 = Web3(HTTPProvider('http://89.223.65.203:9545'))  # 9545 port for Rinkeby,  8545 port for Mainnet
# web3 = Web3(Web3.WebsocketProvider("ws://89.223.65.203:9546"))  # 9546 port for Rinkeby,  8546 port for Mainnet (not working with the current version)




# print('unlock account:', web3.personal.unlockAccount('0x0b7b39bdfba0c85e8351b34d443a800faa1779f6', 'Lord2015')) # print command shows result "True" in console

print(web3.eth.accounts)
print('balance 0 (eth):', web3.fromWei(web3.eth.getBalance(web3.eth.accounts[0]), "ether"))  # shows account 0 balance
print('balance 1 (eth):', web3.fromWei(web3.eth.getBalance(web3.eth.accounts[1]), "ether"))  # shows account 1 balance
print('balance 2 (eth):', web3.fromWei(web3.eth.getBalance(web3.eth.accounts[2]), "ether"))  # shows account 2 balance





# abi = [{"constant":True,"inputs":[],"name":"promoCreatedCount","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"pure","type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_tokenId","type":"uint256"}],"name":"approve","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"ceoAddress","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"}],"name":"payout","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"implementsERC721","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"pure","type":"function"},{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"total","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_tokenId","type":"uint256"}],"name":"getPerson","outputs":[{"name":"personName","type":"string"},{"name":"sellingPrice","type":"uint256"},{"name":"owner","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_newCEO","type":"address"}],"name":"setCEO","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_newCOO","type":"address"}],"name":"setCOO","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_owner","type":"address"},{"name":"_name","type":"string"},{"name":"_price","type":"uint256"}],"name":"createPromoPerson","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"_name","type":"string"}],"name":"createContractPerson","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"name":"owner","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"tokensOfOwner","outputs":[{"name":"ownerTokens","type":"uint256[]"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"name":"","type":"uint256"}],"name":"personIndexToApproved","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"pure","type":"function"},{"constant":True,"inputs":[],"name":"NAME","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_tokenId","type":"uint256"}],"name":"transfer","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"","type":"uint256"}],"name":"personIndexToOwner","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"cooAddress","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_tokenId","type":"uint256"}],"name":"takeOwnership","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"_tokenId","type":"uint256"}],"name":"priceOf","outputs":[{"name":"price","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"_tokenId","type":"uint256"}],"name":"purchase","outputs":[],"payable":True,"stateMutability":"payable","type":"function"},{"constant":True,"inputs":[],"name":"SYMBOL","outputs":[{"name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"inputs":[],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":False,"name":"tokenId","type":"uint256"},{"indexed":False,"name":"name","type":"string"},{"indexed":False,"name":"owner","type":"address"}],"name":"Birth","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"name":"tokenId","type":"uint256"},{"indexed":False,"name":"oldPrice","type":"uint256"},{"indexed":False,"name":"newPrice","type":"uint256"},{"indexed":False,"name":"prevOwner","type":"address"},{"indexed":False,"name":"winner","type":"address"},{"indexed":False,"name":"name","type":"string"}],"name":"TokenSold","type":"event"},{"anonymous":False,"inputs":[{"indexed":False,"name":"from","type":"address"},{"indexed":False,"name":"to","type":"address"},{"indexed":False,"name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"owner","type":"address"},{"indexed":True,"name":"approved","type":"address"},{"indexed":False,"name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"}]


# Contr = web3.eth.contract(0xbcba9e3317dd5e46c5604a358a108b746d1ca71f, abi=abi)

# class web3.contract.Contract(0xbcba9e3317dd5e46c5604a358a108b746d1ca71f):




# print(Contr.abi)

# print(Contr.address)
# print(contr_instance.find_functions_by_name(totalSupply()))



# print(contr_instance.call.totalSupply())








# print(web3.eth.getBlock('latest'))

print(web3.eth.syncing)



