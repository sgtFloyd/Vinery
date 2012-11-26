import API

fields = ['id', 'name', 'publisher', 'start_year', 'count_of_issues']

def search(query):
  data = {
    'resources': 'volume',
    'field_list': ','.join(fields)
  }
  return API.search(query, data)

def show(obj_id):
  """ http://api.comicvine.com/documentation/#volume """
  data = {'field_list': ','.join(fields)}
  return API.show_object('volume', obj_id, data)
