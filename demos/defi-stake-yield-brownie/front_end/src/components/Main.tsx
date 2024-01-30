/* eslint-disable spaced-comment */
/// <reference types= "react-scripts"/>
import { useEthers } from "@usedapp/core"
import helperConfig from "../helper-config.json"
import networkMapping from "../chain-info/deployments/map.json"
//import { constants } from "buffer"
import { constants } from "ethers"
import brownieConfig from "../brownie-config.json"
import dapp from "../dapp.png"
import eth from "../eth.png"
import dai from "../dai.png"
import { YourWallet } from "../YourWallet"


export type Token = {
    image: string
    address: string
    name: string

}

export const Main = () => {
    // Show token values from the wallet
    // Get teh address of different tokens
    // Get teh balance of the users wallet

    // send the brownie-config to our 'src' folder
    // send the build folder.  We are going to open up brownie-config and paste/dump into 'src' folder
    const { chainId, error } = useEthers()
    const networkName = chainId ? helperConfig[chainId] : "dev"
    let stringChainId = String(chainId)
    //const dappTokenAddress
    //console.log(chainId)
    //console.log(networkName)

    const dappTokenAddress = chainId ? networkMapping[String(chainId)]["DappToken"][0] : constants.AddressZero  // looking into mapping : 000//chain-info folder created.
    const wethTokenAddress = chainId ? brownieConfig["networks"][networkName]["weth_token"] : constants.AddressZero
    const fauTokenAddress = chainId ? brownieConfig["networks"]["networkName"]["fau_token"] : constants.AddressZero

    const supportedTokens: Array<Token> = [
        {
            image: dapp,
            address: dappTokenAddress,
            name: "DAPP",
        },
        {
            image: eth,
            address: wethTokenAddress,
            name: "WETH"
        },
        {
            image: fdai,
            address: fauTokenAddress,
            name: "DAI",
        }
    ]
    return (<YourWallet supportedTokens={supportedTokens} />)
}