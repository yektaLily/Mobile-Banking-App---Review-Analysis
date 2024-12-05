from app_store_scraper import AppStore

cibc = AppStore(country="ca", app_name="cibc-mobile-banking")
cibc.review(how_many=10000)

print(cibc.reviews_count)
result = cibc.reviews

# url_cibc = "https://apps.apple.com/ca/app/cibc-mobile-banking/id351448953"
# url_rbc = "https://apps.apple.com/ca/app/rbc-mobile/id407597290"
# url_td = "https://apps.apple.com/ca/app/td-canada/id358790776"
# url_bmo = "https://apps.apple.com/ca/app/bmo-mobile-banking/id429080319"
# url_scotia = "https://apps.apple.com/ca/app/scotiabank/id341151570"