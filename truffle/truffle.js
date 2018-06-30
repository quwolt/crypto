/*
 * NB: since truffle-hdwallet-provider 0.0.5 you must wrap HDWallet providers in a 
 * function when declaring them. Failure to do so will cause commands to hang. ex:
 * ```
 * mainnet: {
 *     provider: function() { 
 *       return new HDWalletProvider(mnemonic, 'https://mainnet.infura.io/<infura-key>') 
 *     },
 *     network_id: '1',
 *     gas: 4500000,
 *     gasPrice: 10000000000,
 *   },
 */


module.exports = {

    networks: {
        development: {
            host: "localhost",
            port: 8545,
            network_id: "*" // Match any network id
        },
        // NEW CONFIGURATION INFO HERE
        rinkeby: {
            host: "89.223.65.203",
            port: 9545, // TODO change to port 9549 (full) or 9547 (LES) or add sepraete network
            network_id: 4
        },
        mainnet: {
            host: "89.223.65.203",
            port: 9545, // TODO change to port 8545 (Mainnet)
            network_id: 1
        }
    },
    // USING SOLC OPTIMAZIER
    solc: {
        optimizer: {
            enabled: true,
            runs: 200
        }
    }
};

