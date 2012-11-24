import API

fields = ['id', 'name', 'volume', 'issue_number', 'publish_year', 'publish_month', 'publish_day']

def search(query):
  data = {
    'resources': 'issue',
    'field_list': ','.join(fields)
  }
  return API.__search(query, data)

def show(obj_id):
  """ http://api.comicvine.com/documentation/#issue """
  data = {'field_list': ','.join(fields)}
  return API.__show_object('issue', obj_id, data)
