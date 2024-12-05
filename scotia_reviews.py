from app_store_scraper import AppStore

scotiabank = AppStore(country="ca", app_name="scotiabank")
scotiabank.review(how_many=10000)

print(scotiabank.reviews_count)
result = scotiabank.reviews

# url_scotia = "https://apps.apple.com/ca/app/scotiabank/id341151570"