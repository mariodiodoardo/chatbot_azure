
import os
from openai import AzureOpenAI

class api_azure:
  

  def __init__(self) -> None:
    self.__endpoint = os.getenv("ENDPOINT_URL", "https://rag-makeathon.openai.azure.com/")
    self.__deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o-mini")
    self.__search_endpoint = os.getenv("SEARCH_ENDPOINT", "https://openai-resource-makeathon.search.windows.net")
    self.__search_key = os.getenv("SEARCH_KEY", "")
    self.__subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "")

    # Inizializzare il client OpenAI di Azure con l'autenticazione basata su chiave
    self.client = AzureOpenAI(
        azure_endpoint=self.endpoint,
        api_key=self.subscription_key,
        api_version="2024-05-01-preview",
    )

  def api_call(self, content:str) ->dict:

    # Preparare la richiesta di chat
    chat_prompt = [
    {
        "role": "user",
        "content": content # "there are problems with the wings? "
    }
    ]

    # Includere risultato vocale se il riconoscimento vocale è abilitato
    speech_result = chat_prompt
    extra_body={
    "data_sources": [{
      "type": "azure_search",
      "parameters": {
        "endpoint": f"{self.search_endpoint}",
        "semantic_configuration": "default",
        "query_type": "simple",
        "fields_mapping": {},
        "in_scope": True,
        "filter": None,
        "strictness": 3,
        "top_n_documents": 5,
        "authentication": {
          "type": "api_key",
          "key": f"{self.__search_key}"
        },
        "index_name" : "reportdocs2"
      }
    }]
    }
    # Generare il completamento
    completion = self.client.chat.completions.create(
        model=self.__deployment,
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

    return completion.to_json()

