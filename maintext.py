#pip install pdfminer.six
import re
from pdfminer.high_level import extract_pages, extract_text

## this extracts all the texts in the table, content , picture size
# for page_layout in extract_pages("Sample.pdf"):
#     for element in page_layout:
#         print(element)

# this extracts all the texts in the table, content
text = extract_text("Sample.pdf")
print(text)

# pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
# matches = pattern.findall(text)
# print(matches)

pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text)
names = [n[:-2] for n in matches]
print(names)
