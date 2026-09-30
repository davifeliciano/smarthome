import os
import json
import logging
import urllib3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    base_url = os.environ.get('BASE_URL')
    if not base_url:
        raise ValueError("A variável de ambiente BASE_URL não foi definida.")
    
    http = urllib3.PoolManager()
    directive = event.get('directive')
    
    if not directive:
        logger.error("Nenhuma diretiva encontrada no evento.")
        return {}
        
    token = None
    if 'endpoint' in directive and 'scope' in directive['endpoint']:
        token = directive['endpoint']['scope']['token']
    elif 'payload' in directive and 'scope' in directive['payload']:
        token = directive['payload']['scope']['token']
    elif 'payload' in directive and 'grantee' in directive['payload']:
        token = directive['payload']['grantee']['token']
        
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    
    response = http.request(
        'POST', 
        base_url, 
        headers=headers, 
        body=json.dumps(event).encode('utf-8')
    )
    
    if response.status >= 400:
        logger.error("Erro retornado pelo Home Assistant: %s", response.data)
        
    return json.loads(response.data.decode('utf-8'))
    