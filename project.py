import requests
from datetime import datetime
from colorama import init, Fore, Style
init(autoreset=True)
def get_rates(baseCUR="EUR"):

    api_key = "c5c51aa4db18f556e06f0b92"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{baseCUR}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["conversion_rates"]
    except:
        print(Fore.RED + Style.BRIGHT+ "Error rquests")
        return None
# funkcija kas konvertē valūtu pēc vietnē norādītā kursa
def convert(amount, from_curr, to_curr, rates):

    if to_curr not in rates:
        print(Fore.RED + Style.BRIGHT+ "Currency not found")
    return amount * rates[to_curr]
# funkcija kas aprēķina cik daudz valūtas ir nepieciešams lai iegūtu lietotāja ievadīto valūtas summu
def reverse_convert(target, from_curr, to_curr, rates):

    if to_curr not in rates:
        print(Fore.RED + Style.BRIGHT+ "Currency not found")
        return None
    return target / rates[to_curr]
# saglabā kursa informāciju teksta failā
def save_file(rates, baseCUR="EUR"):

    try:
        filename = f"Exchange_{baseCUR}.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ({baseCUR})\n")
            for currency, rate in sorted(rates.items()):
                file.write(f"{currency}: {rate}\n")
        print(Fore.WHITE+Style.BRIGHT+f"Data saved: {filename}")
        return True
    except:
        print(Fore.RED + Style.BRIGHT+ "ERROR - file not saved")
        return False
# konvertē izvēlēto valūtu kriptovalūtā
def get_crypto(crypto, amount):

    url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin&vs_currencies={crypto}"
    try:
        response = requests.get(url).json()
        btc_price = response['bitcoin'][crypto]
        eth_price = response['ethereum'][crypto]
        bnb_price = response['binancecoin'][crypto]
        print(Fore.GREEN+f"\nExchange rate for {amount} {crypto.upper()} in crypto:\n")
        print(Fore.GREEN+f"{amount} {crypto.upper()} = {amount / btc_price:.8f} BTC")
        print(Fore.GREEN+f"{amount} {crypto.upper()} = {amount / eth_price:.8f} ETH")
        print(Fore.GREEN+f"{amount} {crypto.upper()} = {amount / bnb_price:.8f} BNB")
    except:
        print(Fore.RED + Style.BRIGHT+ "Invalid currency")
if __name__ == "__main__":

    while True:
        print(Fore.BLUE + "\nSelect an option:")
        print(Fore.CYAN + "1. Currency conversion")
        print(Fore.CYAN+"2. Reverse currency conversion")
        print(Fore.CYAN+"3. Conversion to crypto")
        print(Fore.RED+Style.DIM+"4. Exit")
        choice = input(Fore.YELLOW+"Enter option number: ").strip()
        if choice == "1":
            from_curr = input(Fore.BLACK+Style.BRIGHT+"From currency: ").upper()
            rates = get_rates(baseCUR=from_curr)
            if not rates:
                print(Fore.RED + Style.BRIGHT+"ERROR - no rates")
                continue
            try:
                to_curr = input(Fore.BLACK+Style.BRIGHT+"In currency: ").upper()
                amount = float(input(Fore.BLACK+Style.BRIGHT+"Enter the amount: "))
                if to_curr in rates:
                    result = convert(amount, from_curr, to_curr, rates)
                    print(Fore.GREEN+f"{amount} {from_curr} = {result:.2f} {to_curr}")
                else:
                    print(Fore.RED + Style.BRIGHT+"Invalid currency")
            except:
                print(Fore.RED + Style.BRIGHT+ "ERROR - invalid amount")
            save_file(rates, baseCUR=from_curr)
        elif choice == "3":
            user_currency = input(Fore.BLACK+Style.BRIGHT+"Enter currency: ").lower()
            try:
                amount = float(input(Fore.BLACK+Style.BRIGHT+"Enter the amount: "))
                get_crypto(user_currency, amount)
            except:
                print(Fore.RED + Style.BRIGHT+"ERROR - Enter number")
        elif choice == "2":
            from_curr = input(Fore.BLACK+Style.BRIGHT+"From currency: ").upper()
            rates = get_rates(baseCUR=from_curr)
            if not rates:
                continue
            to_curr = input(Fore.BLACK+Style.BRIGHT+"In currency: ").upper()
            try:
                target = float(input(Fore.BLACK+Style.BRIGHT+f"Enter the amount you want to receive: "))
                if to_curr in rates:
                    base_needed = reverse_convert(target, from_curr, to_curr, rates)
                    if base_needed is not None:
                        print(Fore.GREEN+ f"To receive {target} {to_curr}, you need {base_needed:.2f} {from_curr}")
                else:
                    print(Fore.RED + Style.BRIGHT+ "Invalid currency")
            except:
                print(Fore.RED + Style.BRIGHT+ "Invalid amount")             
        elif choice == "4":
            print(Fore.RED+Style.DIM+"Exiting the program!")
            break
        else:
            print(Fore.RED + Style.BRIGHT+ "Incorrect option.")