# Smart Home

Servidor de automação residencial com stack Home Assistant, Zigbee2MQTT, Mosquitto e PostgreSQL

## Resumo

```text
.
├── .env                    # Credenciais de inicialização do PostgreSQL (não versionado)
├── docker-compose.yml
├── homeassistant_data
│   ├── configuration.yaml
│   ├── secrets.yaml        # Contem URL do PostgreSQL (não versionado)
│   └── SERVICE_KEY.json    # Conta de serviço Google (não versionado)
├── mosquitto_data              
│   └── config
│       ├── mosquitto.conf
|       └── pwfile          # Hash das senhas MQTT (não versionado)
└── zigbee2mqtt_data
    ├── configuration.yaml
    └── secret.yaml         # Contem usuário e senha do mosquitto e network_key (não versionado)
```

| Serviço | Função | Endereço |
| --- | --- | --- |
| Home Assistant | Prove interface de usuário, integrações, automações e histórico de atividades | `http://<server_ip>:8123` |
| Zigbee2MQTT | Zigbee to MQTT bridge | `http://<server_ip>:8080` |
| Mosquitto | Broker MQTT | Z2M usa `mqtt://mosquitto:1883` |
| PostgreSQL 15 | Banco de dados para histórico de atividade | HA usa `127.0.0.1:5432` |

## Referências

- [Home Assistant em Docker](https://www.home-assistant.io/installation/raspberrypi#install-home-assistant-container)
- [Documentação do Zigbee2MQTT](https://www.zigbee2mqtt.io/guide/configuration/)
- [Documentação do Mosquitto](https://mosquitto.org/documentation/)
- [Integração Google Assistant do Home Assistant](https://www.home-assistant.io/integrations/google_assistant/)
- [Integração Alexa Smart Home do Home Assistant](https://www.home-assistant.io/integrations/alexa.smart_home/)
