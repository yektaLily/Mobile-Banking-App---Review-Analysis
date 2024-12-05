from app_store_scraper import AppStore

rbc = AppStore(country="ca", app_name="rbc-mobile")
rbc.review(how_many=10000)

print(rbc.reviews_count)
result = rbc.reviews

# url_rbc = "https://apps.apple.com/ca/app/rbc-mobile/id407597290"