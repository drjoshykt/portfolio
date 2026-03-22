import string
import re

def extract_text(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    
    # Text strings might be space-separated or interspersed with nulls (UTF-16LE)
    # Let's decode as utf-16le with errors ignored to try and fetch content
    txt_utf16 = data.decode('utf-16le', errors='ignore')
    # Filter out nonsense characters
    valid_chars = set(string.printable)
    filtered1 = ''.join(c if c in valid_chars else ' ' for c in txt_utf16)
    
    txt_ascii = data.decode('ascii', errors='ignore')
    filtered2 = ''.join(c if c in valid_chars else ' ' for c in txt_ascii)
    
    with open("C:/Users/ewinc/OneDrive/Desktop/joshy/resume_text.txt", "w", encoding="utf-8") as f:
        f.write("---UTF16---\n")
        # Removing long chains of spaces
        f.write(re.sub(r' {2,}', '  ', filtered1))
        f.write("\n\n---ASCII---\n")
        f.write(re.sub(r' {2,}', '  ', filtered2))

extract_text(r"C:\Users\ewinc\OneDrive\Desktop\joshy\RESUME K T JOSHY UPDATED.doc")
