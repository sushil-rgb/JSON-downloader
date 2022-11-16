from tools import LoadJson


# Enter an api url below: For example, below is an api-url from https://www.booksmandala.com.
api_url = "https://booksmandala.com/api/books?page=2&main_category=lifestyle-%26-wellness"

# Enter a json name below:
json_name = "booksmandala"

booksmandala = LoadJson()

# For download:
booksmandala.download_file(api_url, json_name)
# For fetch from downloaded json data:
print(booksmandala.read_json(json_name))
