import { useEffect, useState } from "react"
import { useEthers, useContractFunction } from "@usedapp/core"
import { constants, utils } from "ethers"
import TokenFarm from "../chain-info/contracts/TokenFarm.json"
import ERC20 from "../chain-info/contracts/MockERC20.json"
import networkMapping from "../chain-info/deployments/map.json"
import { Contract } from "@ethersprject/contracts"
//import { constants } from "buffer"

export const useStakeTokens = (tokenAddress: string) => {
    // address
    // abi
    // chainId
    const { chainId } = useEthers()
    const { abi } = TokenFarm
    const tokenFarmAddress = chainId ? networkMapping[String(chainId)]["TokenFarm"][0] : constants.AddressZero
    const tokenFarmInterface = new utils.Interface(abi)
    const tokenFarmContract = new Contract(tokenFarmAdddress, tokenFarmInterface)


    const erc20ABI = ERC20.abi
    const erc20Interface = new utils.Interface(erc20ABI)
    const erc20Contract = new Contract(tokenAddress, erc20Interface)
    // approve
    // stake tokens   

    const { send: approveErc20Send, state: approveAndStatkeErc20State } =
        useContractFunction(erc20Contract, "approve", {
            transactionName: "approve ERC20 transfer"
        })
    const approveAndStake = (amount: string) => {
        setAmountToStake(amount)
        return approve Erc20Send(tokenFarmAddress, amount)
    }
    // stake
    const { send: stakeSend, state: stakeState } =
        useContractFunction(tokenFarmContract, "stakeTokens", {
            transactionName: "Stake Tokens",
        })
    const [amountToStake, setAmountToStake] = useState("0")




    //useEffect
    useEffect(() => {
        if (approveAndStakeErc20State.status == "Success") {
            // stake function
            stakeSend(amountToStake, tokenAddress)
        }
    }, [approveAndStakeErc20State, amountToStake, tokenAddress])

    const [state, setState] = useState(approveAndStatkeErc20State)

    useEffect(() => {
        if (approveAndStatkeErc20State.status === "Success") {
            setState(stakeState)
        } else {
            setState(approveAndStatkeErc20State)
        }
    }, [approveAndStakeErc20State, stakeState])

    return { approveAndStake, state }
}