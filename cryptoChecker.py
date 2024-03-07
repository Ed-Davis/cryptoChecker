from apilib import Api


def show_top_three_changers():
    # Comment out EITHER mocked or real API call
    # return_data = Api.data(Api)  # Default real API call
    return_data = Api.mocked_data(Api)  # Local file data
    results = Api.top3(Api, return_data)
    i = 2
    while i >= 0:
        print(results[i])
        price = Api.data(Api(), 'avgPrice', {'symbol': results[i]['symbol']})
        print(price)
        i -= 1


show_top_three_changers()

