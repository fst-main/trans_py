from azure.identity import DefaultAzureCredential
from azure.ai.translation.document import DocumentTranslationClient
credential = DefaultAzureCredential()

document_translation_client = DocumentTranslationClient(
    endpoint = "https://SIITransPY.cognitiveservices.azure.com/",
    credential=credential
)