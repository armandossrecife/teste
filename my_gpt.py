import requests

# Fetch the interview text from the URL
url = "https://raw.githubusercontent.com/armandossrecife/teste/main/ipek.txt"
response = requests.get(url)
interview_text = response.text

# Count the number of occurrences of "Technical debt"
count = interview_text.count("technical debt")

# Print the result
print(f"The term 'Technical debt' appears {count} times in the interview.")