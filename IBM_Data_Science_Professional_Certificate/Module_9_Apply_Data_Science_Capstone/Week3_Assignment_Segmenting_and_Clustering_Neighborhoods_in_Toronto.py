
# coding: utf-8

# <H1> IBM Apply Data Science Capstone - Week 3 Segmenting and Clustering Neighborhoods in Toronto </H1>

# <B> Import Libraries </B>

# In[53]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# <B> Load html table form Wikipedia - List of postal codes of Canada

# In[54]:


url = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'


# In[55]:


result = requests.get(url)
html_file = result.content
 
soup = BeautifulSoup(html_file, "html.parser")

print(soup.prettify())


# In[56]:


table = soup.find('table', class_='wikitable sortable')

print(table)


# In[82]:


table_rows = table.find_all('tr')

res = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [tr.text.strip() for tr in td if tr.text.strip()]
    if row:
        res.append(row)


# <B> Load data into dataframe </B>

# In[58]:


df = pd.DataFrame(res, columns=["Postcode","Borough","Neighbourhood"])
df.head()


# In[59]:


df.shape


# <B> Merge Neighbourhood with same Postcode and Borough </B>

# In[84]:


Postcode = df.Postcode
Borough = df.Borough
Neighbourhood = df.Neighbourhood

unique_p = set(Postcode)
print('num of unique Postal codes:', len(unique_p))
Postcode_u      = []
Borough_u       = []
Neighbourhood_u = []



for postcode_unique_element in unique_p:
    p_var = ''; b_var = ''; n_var = ''; 
    for postcode_idx, postcode_element in enumerate(Postcode):
        if postcode_unique_element == postcode_element:
            p_var = postcode_element;
            b_var = Borough[postcode_idx]
            if n_var == '': 
                n_var = Neighbourhood[postcode_idx]
            else:
                n_var = n_var + ', ' + Neighbourhood[postcode_idx]
    Postcode_u.append(p_var)
    Borough_u.append(b_var)
    Neighbourhood_u.append(n_var)
    
  


# In[87]:


toronto_dict = {'Postcode':Postcode_u, 'Borough':Borough_u, 'Neighbourhood':Neighbourhood_u}
df_toronto = pd.DataFrame.from_dict(toronto_dict)
df_toronto.sort_values('Postcode')
df_toronto


# In[86]:


df_toronto.shape

