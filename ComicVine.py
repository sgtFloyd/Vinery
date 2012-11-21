import requests
import inspect

__cv_api_url = "http://api.comicvine.com"
__cv_api_key = "f162efb8cc8e7d4291a5df62aaf5b25146a55d7f"
__cv_debug = False

def set_debug(on):
  global __cv_debug
  __cv_debug = on

def debug(message):
  if __cv_debug:
    parent = inspect.stack()[1][3]
    print '%s: %s' % (parent, message)

def __get_json(method, data):
  request_url = '%s/%s' % (__cv_api_url, method)
  debug('%s, params: %s' % (request_url, data))

  data = dict({
    'api_key': __cv_api_key,
    'format': 'json'
  }, **data)
  response = requests.get(request_url, params=data)
  debug(response.url)

  json = response.json
  if json['status_code'] == 1:
    return json
  else:
    debug('ComicVine Error %(status_code)s: %(error)s' % json)
    return False

series_fields = ','.join(['id', 'name', 'publisher', 'start_year', 'count_of_issues', 'issues'])
issue_fields = ','.join(['id', 'name', 'volume', 'issue_number', 'publish_year', 'publish_month', 'publish_day'])

def __search(query, data):
  """ http://api.comicvine.com/documentation/#search """
  data = dict({'query': query}, **data)
  return __get_json('search', data)

def search_series(query):
  data = {
    'resources': 'volume',
    'field_list': series_fields
  }
  return __search(query, data)

def search_issues(query):
  data = {
    'resources': 'issue',
    'field_list': issue_fields
  }
  return __search(query, data)

def __get_object(obj_type, obj_id, data):
  method = '%s/%s/' % (obj_type, obj_id)
  return __get_json(method, data)

def get_series(obj_id):
  data = {'field_list': series_fields}
  return __get_object('volume', obj_id, data)

def get_issue(obj_id):
  data = {'field_list': issue_fields}
  return __get_object('issue', obj_id, data)
