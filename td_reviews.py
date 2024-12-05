from app_store_scraper import AppStore

td = AppStore(country="ca", app_name="td-canada")
td.review(how_many=10000)

print(td.reviews_count)
result = td.reviews

# url_td = "https://apps.apple.com/ca/app/td-canada/id358790776"