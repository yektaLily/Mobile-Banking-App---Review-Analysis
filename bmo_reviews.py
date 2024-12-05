from app_store_scraper import AppStore

bmo = AppStore(country="ca", app_name="bmo-mobile-banking")
bmo.review(how_many=10000)

print(bmo.reviews_count)
result = bmo.reviews

# url_bmo = "https://apps.apple.com/ca/app/bmo-mobile-banking/id429080319"
