from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency="GBP")
    bot.select_place_to_go(place_to_go='New York')
    bot.select_date(check_in_date='2022-03-24',
                    check_out_date='2022-03-26')
    bot.select_adults(count=10)
    bot.click_search()
