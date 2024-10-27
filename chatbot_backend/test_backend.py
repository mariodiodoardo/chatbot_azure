import requests as rq

endpoint = "https://hidden-phantasm-9qxjwrj49552q4v-3000.app.github.dev/getPromptContent"
response = rq.post(endpoint, json={"content": "How is the wing of the aircraft?"})

print(response.status_code)
print(response.json())  # Se vuoi vedere la risposta JSON
