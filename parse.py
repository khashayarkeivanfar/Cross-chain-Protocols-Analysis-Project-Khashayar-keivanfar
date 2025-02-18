import json
import matplotlib.pyplot as plt
import json
import matplotlib.pyplot as plt
from tokens import *
def Bungee_analytics(json_data):  

    bridge_names = []
    total_output_value = 0
    total_gas_fees = 0
    total_protocol_fees = 0
    from_asset = json_data.get("result", {}).get("fromAsset", {})
    to_asset = json_data.get("result", {}).get("toAsset", {})
    
    fromToken = from_asset.get("symbol", "Unknown")
    fromchainid = json_data.get("result", {}).get("fromChainId", "Unknown")
    toToken = to_asset.get("symbol", "Unknown")
    tochainid = json_data.get("result", {}).get("toChainId", "Unknown")
    for route in json_data.get("result", {}).get("routes", []):
        bridge_names.extend(route.get("usedBridgeNames", []))
        output_value = route.get("outputValueInUsd", 0)
        gas_fees = route.get("totalGasFeesInUsd", 0)
        protocol_fees = route.get("protocolFees", {}).get("feesInUsd", 0) if "protocolFees" in route else 0

        total_output_value += output_value
        total_gas_fees += gas_fees
        total_protocol_fees += protocol_fees

    bridge_names = list(set(bridge_names))
    net_output_value = total_output_value - (total_gas_fees + total_protocol_fees)

    
    labels = ["Total Output Value", "Total Gas Fees", "Total Protocol Fees", "Net Output Value"]
    values = [total_output_value, total_gas_fees, total_protocol_fees, net_output_value]

    plt.show(block=False)  
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=['blue', 'red', 'orange', 'green'])
    plt.xlabel("Cost Categories")
    plt.ylabel("Amount in USD")
    plt.title("Transaction Cost Breakdown for ({} on {}) to ({} on {})".format(
        fromToken, get_chain_name(fromchainid), toToken, get_chain_name(tochainid)))

    
    for i, v in enumerate(values):
        plt.text(i, v + 0.1, f"{v:.5f}", ha='center', fontsize=10)

    
    plt.figtext(0.5, -0.1, f"Bridges Used: {', '.join(bridge_names) if bridge_names else 'None'}",
                wrap=True, horizontalalignment='center', fontsize=10)

    plt.draw()
    plt.pause(0.001) 

    
def LiFi_analysis(json_data):
    fromchainid = int(json_data["action"]["fromToken"]["chainId"])
    tochainid = int(json_data["action"]["toToken"]["chainId"])

    fromToken= json_data["action"]["fromToken"]["symbol"]
    toToken = json_data["action"]["toToken"]["symbol"]

    from_amount = float(json_data["estimate"]["fromAmountUSD"])
    to_amount = float(json_data["estimate"]["toAmountUSD"])
    total_gas_fees = sum(float(gas["amountUSD"]) for gas in json_data["estimate"]["gasCosts"])
    total_protocol_fees = sum(float(fee["amountUSD"]) for fee in json_data["estimate"]["feeCosts"])
    total_output_value = to_amount
    net_output_value = total_output_value - total_gas_fees - total_protocol_fees
    bridge_names = set()
    for step in json_data.get("includedSteps", []):
        if step.get("type") == "cross": 
            bridge_names.add(step.get("toolDetails", {}).get("name", "Unknown"))
    bridge_names_list = sorted(bridge_names)
    labels = ["Total Output Value", "Total Gas Fees", "Total Protocol Fees", "Net Output Value"]
    values = [total_output_value, total_gas_fees, total_protocol_fees, net_output_value]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=['blue', 'red', 'orange', 'green'])
    plt.xlabel("Cost Categories")
    plt.ylabel("Amount in USD")
    plt.title("Transaction Cost Breakdown for ({} on {}) to ({} on {})".format(
            fromToken, get_chain_name(fromchainid),toToken, get_chain_name(tochainid)))
    for i, v in enumerate(values):
        plt.text(i, v + 0.1, f"{v:.5f}", ha='center', fontsize=10)


    plt.figtext(0.5, -0.1, f"Bridges Used: {', '.join(bridge_names_list) if bridge_names_list else 'None'}",
        wrap=True, horizontalalignment='center', fontsize=10)

    plt.draw()
    plt.pause(0.001)
