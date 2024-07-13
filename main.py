#extract tables
#pip install tabula-py

import tabula

# tables = tabula.read_pdf("Sample.pdf", pages="all")
# print(tables)

#pandas dataframe
tables = tabula.read_pdf("Sample.pdf", pages="all")
print(type(tables[0]))
df = tables[0]
print(df[df.Age >30])
