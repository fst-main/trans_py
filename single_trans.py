from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import DocumentTranslationClient

endpoint = "https://SIITransPY.cognitiveservices.azure.com/"
credential = AzureKeyCredential("c34d7e1ff84d4a35855631f70558051f")
source_container_sas_url_en = "https://blobish1.blob.core.windows.net/sas1/polish.txt?sp=r&st=2022-02-03T09:07:13Z&se=2022-03-03T17:07:13Z&sv=2020-08-04&sr=b&sig=Y7Ui93ieF%2BgBFzF5KFDt0IQSQxhXeRk1UAODeZGmcHs%3D"
target_container_sas_url_es = "https://blobish1.blob.core.windows.net/sas2?sv=2020-10-02&st=2022-02-03T08%3A54%3A41Z&se=2022-03-03T08%3A54%3A00Z&sr=c&sp=racwl&sig=kvq4fZKCAqyjHygJeX9haA5S9yqCsw86YQYLCZK4Ecs%3D"

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