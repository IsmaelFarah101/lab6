import requests


def question():
    amount = float(input('Enter the amount of dollars: '))
    return amount

def rate():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    data = requests.get(url).json()
    price = data['bpi']['USD']['rate_float']
    return price
def calculate(answer):
    price = answer * rate()
    return price

def main():
    answer = question()
    price = calculate(answer)
    print(f'{answer} amount in dollars is {price}')

if __name__ == '__main__':
    main()