import API

def search(query):
  data = {
    'resources': 'volume',
    'field_list': ','.join(Series.fields)
  }
  search = API.search(query, data)
  return [Series(result) for result in search['results']]

def show(obj_id):
  """ http://api.comicvine.com/documentation/#volume """
  data = {'field_list': ','.join(Series.fields)}
  return API.show_object('volume', obj_id, data)

class Series(API.obj):
  fields = ['id', 'name', 'publisher', 'start_year', 'count_of_issues']

  def __setattr__(self, name, value):
    if name == 'publisher':
      value = Publisher(value)
    super(Series, self).__setattr__(name, value)

  def label(self):
    return '%s (%s)' % (self.name.strip(), self.start_year)

  def description(self):
    desc = []
    if self.count_of_issues:
      count = "%s issue" % self.count_of_issues
      if self.count_of_issues != 1:
        count += 's'
      desc.append(count)
    if self.publisher and self.publisher.name:
      desc.append("Publisher: %s" % self.publisher.name.strip())
    return ', '.join(desc)

class Publisher(API.obj):
  fields = ['id', 'name']
