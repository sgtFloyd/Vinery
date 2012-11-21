import requests
import inspect

__cv_api_url = "http://api.comicvine.com"
__cv_api_key = "f162efb8cc8e7d4291a5df62aaf5b25146a55d7f"
__debug_mode = False

def set_debug(on):
  global __debug_mode
  __debug_mode = on

def debug(message):
  if __debug_mode:
    parent = inspect.stack()[1][3]
    print '%s: %s' % (parent, message)

def __get_json(method, data):
  data = dict({
    'api_key': __cv_api_key,
    'format': 'json'
  }, **data)
  request_url = '%s/%s' % (__cv_api_url, method)
  debug('%s, params: %s' % (request_url, data))
  response = requests.get(request_url, params=data)

  json = response.json
  if json['status_code'] == '1':
    return json
  else:
    debug('ComicVine Error %(status_code)s: %(error)s' % json)
    return False


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
