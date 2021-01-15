import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?rlz=1C1CHBF_enIN869IN870&sxsrf=ALeKk011IoOJxmEJhIsYAXVi2RR9FHicsQ%3A1609999516397&ei=nKT2X7HrF8ev9QO1rruICQ&q=meaning+of+coding&oq=meaning+of+coding&gs_lcp=CgZwc3ktYWIQAzINCAAQyQMQkQIQRhD5ATICCAAyAggAMgcIABAUEIcCMgIIADICCAAyAggAMgIIADICCAAyAggAOgQIABBHOgkIIxAnEEYQ-QE6CAgAEMkDEJECOgUIABCRAjoFCAAQsQM6CwgAELEDEMkDEJECUN0jWOAoYLoqaABwAngAgAHoAogBmwmSAQUyLTMuMZgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab&ved=0ahUKEwixqY3Kk4nuAhXHV30KHTXXDpEQ4dUDCA0&uact=5"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, "html.parser")
print(soup.findAll('a'))