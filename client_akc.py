from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import DocumentTranslationClient

endpoint = "https://SIITransPY.cognitiveservices.azure.com/"
credential = AzureKeyCredential("c34d7e1ff84d4a35855631f70558051f")
document_translation_client = DocumentTranslationClient(endpoint, credential)