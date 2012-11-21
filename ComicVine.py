import requests

__cv_api_url = "http://api.comicvine.com/"
__cv_api_key = "f162efb8cc8e7d4291a5df62aaf5b25146a55d7f"

def __get_json(method, data):
  data = dict({'api_key': __cv_api_key, 'format': 'json'}, **data)
  request_url = __cv_api_url + method
  response = requests.get(request_url, params=data)
  return response.json

def __search(query, data):
  """ http://api.comicvine.com/documentation/#search """
  data = dict({'query': query}, **data)
  return __get_json('search', data)

def search_series(query):
  data = {'resources': 'volume'}
  return __search(query, data)
def search_issues(query):
  data = {'resources': 'issue'}
  return __search(query, data)
