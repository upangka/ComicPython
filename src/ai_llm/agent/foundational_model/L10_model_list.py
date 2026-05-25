"""
L10_model_list.py

This module demonstrates how to retrieve and manage available model lists from different providers.
It covers querying available models, filtering by capabilities, and managing model metadata
for dynamic model selection in applications.
"""
import os
import requests
token = os.getenv("DEEPSEEK_API_KEY")
response = requests.get(
    "https://api.deepseek.com/models",
    headers={"Authorization": f"Bearer {token}"}
)

if response.status_code == 200:
    models = response.json()
    print(models)
    for model in models['data']:
        print(model['id'])
else:
    raise Exception(f"Error: {response.status_code}")

"""
{'object': 'list', 'data': [{'id': 'deepseek-v4-flash', 'object': 'model', 'owned_by': 'deepseek'}, {'id': 'deepseek-v4-pro', 'object': 'model', 'owned_by': 'deepseek'}]}
deepseek-v4-flash
deepseek-v4-pro
"""