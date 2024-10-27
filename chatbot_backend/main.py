
import os
from openai import AzureOpenAI

endpoint = os.getenv("ENDPOINT_URL", "https://rag-makeathon.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o-mini")
search_endpoint = os.getenv("SEARCH_ENDPOINT", "https://openai-resource-makeathon.search.windows.net")
search_key = os.getenv("SEARCH_KEY", "SEARCH_KEY")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "sub_key")

# Inizializzare il client OpenAI di Azure con l'autenticazione basata su chiave
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2024-05-01-preview",
)

# Preparare la richiesta di chat
chat_prompt = [
{
    "role": "user",
    "content": "there are problems with the wings? "
}
]

# Includere risultato vocale se il riconoscimento vocale è abilitato
speech_result = chat_prompt
extra_body={
"data_sources": [{
  "type": "azure_search",
  "parameters": {
    "endpoint": f"{search_endpoint}",
    "semantic_configuration": "default",
    "query_type": "simple",
    "fields_mapping": {},
    "in_scope": True,
    "filter": None,
    "strictness": 3,
    "top_n_documents": 5,
    "authentication": {
      "type": "api_key",
      "key": f"{search_key}"
    },
    "index_name" : "reportdocs2"
  }
}]
}
# Generare il completamento
completion = client.chat.completions.create(
    model=deployment,
    messages=speech_result,
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False,
    extra_body = extra_body
)



print(completion.to_json())
