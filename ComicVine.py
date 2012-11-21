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
  data = dict({
    'api_key': __cv_api_key,
    'format': 'json'
  }, **data)
  request_url = '%s/%s' % (__cv_api_url, method)
  debug('%s, params: %s' % (request_url, data))
  response = requests.get(request_url, params=data)

  json = response.json
  if json['status_code'] == 1:
    return json
  else:
    debug('ComicVine Error %(status_code)s: %(error)s' % json)
    return False

def __search(query, data):
  """ http://api.comicvine.com/documentation/#search """
  data = dict({'query': query}, **data)
  if 'field_list' in data:
    data['field_list'] = ','.join(data['field_list'])
  return __get_json('search', data)

def search_series(query):
  data = {
    'resources': 'volume',
    'field_list': [
      'id',
      'name',
      'publisher',
      'start_year',
      'count_of_issues'
    ]
  }
  return __search(query, data)

def search_issues(query):
  data = {
    'resources': 'issue',
    'field_list': [
      'id',
      'name',
      'volume',
      'issue_number',
      'publish_year',
      'publish_month',
      'publish_day'
    ]
  }
  return __search(query, data)

def __view_object(obj_type, obj_id, data):
  method = '%s/%s/' % (obj_type, obj_id)
  return __get_json(method, data)
def view_series(id):
  return __view_object('volume', id, {})
def view_issue(id):
  return __view_object('issue', id, {})
