from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

def validateURL(url):
  try:
    result = urlparse(url)
    if all([result.scheme, result.netloc]):
      print('URL OK')
      return True
    else:
      print('URL does not look correct')
      return False
  except ValueError:
    print('Error')
    return False

def getTags(pageSource, tagOne, tagTwo):
  res = requests.get(pageSource)
  pagesource = res.text
  soup = BeautifulSoup(pagesource, 'html.parser')

  count = 0
  tagsStore = []
  for tags in soup.find_all(tagOne):
    myTags = tags.get(tagTwo)
    if myTags is not None:
      count += 1
      if not myTags in tagsStore: # tests for duplciate tags
        tagsStore.append(myTags)
  # return tagsStore
  if count > len(tagsStore):
    dupeMsg = 'duplicate {} and {} tags found'.format(tagOne, tagTwo)
    tagsStore.append(dupeMsg)
    return tagsStore
  else:
    return tagsStore

def seeMore(pageSource, tagOne):
  res = requests.get(pageSource)
  pagesource = res.text
  soup = BeautifulSoup(pagesource, 'html.parser')
  extract = soup.find_all(tagOne)

  print('More details. Will show all {} tags...'.format(tagOne))
  count = 0
  detailStore = []
  for line in extract:
    moreDetails = ('{}: {}'.format(count,line))
    if moreDetails is not None:
      detailStore.append(moreDetails)
    count += 1
  print(detailStore)
  return detailStore

# def findTagNames(getSource, tagOne, tagTwo):
#   soup = startSoup(getSource)
#   print('Finding {} tags with the value {}'.format(tagOne,tagTwo))
#   count = 0
#   tagList = soup.find_all(attrs={tagOne: tagTwo})
#   for line in tagList:
#     return('{}: {}'.format(count,line))
#     count += 1
