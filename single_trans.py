from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import DocumentTranslationClient

endpoint = "https://siitranspy.cognitiveservices.azure.com/"
credential = AzureKeyCredential("c34d7e1ff84d4a35855631f70558051f")
source_container_sas_url_en = "https://blobish1.blob.core.windows.net/sas1/polish.txt?sp=r&st=2022-02-03T15:05:45Z&se=2022-02-03T23:05:45Z&spr=https&sv=2020-08-04&sr=b&sig=LixkVsfnV49KzCmObJ3eWhmkDg00u%2BqkqAW%2FNpbiY6M%3D"
target_container_sas_url_es = "https://blobish1.blob.core.windows.net/sas2/tradus.txt?sp=r&st=2022-02-03T15:07:30Z&se=2022-02-03T23:07:30Z&spr=https&sv=2020-08-04&sr=b&sig=PCXO7eKd%2FPtPlUPT1JFpKEvMc24zxkXl6Vzn4X5XDYw%3D"

document_translation_client = DocumentTranslationClient(endpoint, credential)

poller = document_translation_client.begin_translation(source_container_sas_url_en, target_container_sas_url_es, "es")

result = poller.result()

print("Status: {}".format(poller.status()))
print("Created on: {}".format(poller.details.created_on))
print("Last updated on: {}".format(poller.details.last_updated_on))
print("Total number of translations on documents: {}".format(poller.details.documents_total_count))

print("\nOf total documents...")
print("{} failed".format(poller.details.documents_failed_count))
print("{} succeeded".format(poller.details.documents_succeeded_count))

for document in result:
    print("Document ID: {}".format(document.id))
    print("Document status: {}".format(document.status))
    if document.status == "Succeeded":
        print("Source document location: {}".format(document.source_document_url))
        print("Translated document location: {}".format(document.translated_document_url))
        print("Translated to language: {}\n".format(document.translated_to))
    else:
        print("Error Code: {}, Message: {}\n".format(document.error.code, document.error.message))