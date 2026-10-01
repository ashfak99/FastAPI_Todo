with open("prompt.txt", "r", encoding="utf-8") as file:
    prompt_template=file.read()

prompt=prompt_template.replace("{{name}}","Ashfak").replace("{{place}}","Kolkata, West Bengal")

print(prompt)