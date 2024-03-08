from apilib import Api


def show_top_three_changers():
    # return_data = Api.mocked_data()  # Local file data option - used for making the solution
    return_data = Api.get(Api())
    results = Api.top3(return_data)
    i = 2
    while i >= 0:
        print("Currency ID: " + results[i]['symbol'])
        print("Price change: " + results[i]['priceChangePercent'] + "%")
        price = Api.get(Api(), 'avgPrice', {'symbol': results[i]['symbol']})
        print("Average Price: " + price['price'] + "\n")
        i -= 1


show_top_three_changers()
