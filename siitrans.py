import requests, uuid, json
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import DocumentTranslationClient

# Add your subscription key and endpoint
subscription_key = "c34d7e1ff84d4a35855631f70558051f"
endpoint = "https://api.cognitive.microsofttranslator.com"

# Add your location, also known as region. The default is global.
# This is required if using a Cognitive Services resource.
location = "westeurope"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0'
    'from': 'pl'
    'to': 'en'
}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key
    'Ocp-Apim-Subscription-Region': location
    'Content-type': 'application/json'
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': 'Just try it and tell me some!'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))


document_translation_client = DocumentTranslationClient("https://api.cognitive.microsofttranslator.com", AzureKeyCredential("c34d7e1ff84d4a35855631f70558051f"))
poller = document_translation_client.begin_translation("https://blobish1.blob.core.windows.net/sas1", "https://blobish1.blob.core.windows.net/sas2", "<target_language_code>")