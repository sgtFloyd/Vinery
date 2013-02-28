import API

def search(query):
  data = {
    'resources': 'issue',
    'field_list': ','.join(fields)
  }
  return API.search(query, data)

def show(obj_id):
  """ http://api.comicvine.com/documentation/#issue """
  data = {'field_list': ','.join(fields)}
  return API.show_object('issue', obj_id, data)

class Issue(API.obj):
  fields = ['id', 'name', 'volume', 'issue_number', 'publish_year', 'publish_month', 'publish_day']
