from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)



#text separators: \n\n(para) -> \n(line) -> '-'(words)
#recursivetextsplitter follows the above order that avoids abrupt text cutting. better than length based text splitter.
#most used text splitter
#at the end it will try to optimize your code.

#we use same type of text splitter with its extension to split codes and different format too. it uses different order of text separators like:
#\nclass, \ndef, \n\tdef -> then above mentioned order
#examples in code-based.py and markdown-based.py