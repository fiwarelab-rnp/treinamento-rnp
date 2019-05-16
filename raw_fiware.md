
# Treinamento FIWARE Lab @ RNP

## Desenvolvimento de aplicações com FIWARE com requisições puras

### Criação do serviço

`POST` http://fiwarelab.rnp.br:8007/iot/services

**Headers**
```javascript
'Content-Type': 'application/json'
'Fiware-Service': 'UFRN'
'Fiware-ServicePath': '/dimap'
```

**Body**
```javascript
{
  "services": [
    {
      "protocol": ["IoTA-UL"],
      "apikey": "1a2b3c4d5e6f7h",
      "token": "token2",
      "cbroker": "http://fiwarelab.rnp.br:8004",
      "entity_type": "thing",
      "resource": "/iot/d"
    }
  ]
}
```

### Criação de entidade

`POST` http://fiwarelab.rnp.br:8004/v2/entities

**Headers**
```javascript
'Content-Type': 'application/json'
'Fiware-Service': 'UFRN'
'Fiware-ServicePath': '/dimap'
```

**Body**
```javascript
{
  "id": "Room001",
  "type": "Room",
  "temperature": {
    "value": 23,
    "type": "Float"
  },
  "pressure": {
    "value": 720,
    "type": "Integer"
  }
}
```

### Listar entidades

`GET` http://fiwarelab.rnp.br:8004/v2/entities

**Headers**
```javascript
'Fiware-Service': 'UFRN'
'Fiware-ServicePath': '/dimap'
```

### Listar entidades

`GET` http://fiwarelab.rnp.br:8004/v2/entities

**Headers**
```javascript
'Fiware-Service': 'UFRN'
'Fiware-ServicePath': '/dimap'
```

### Filtrar entidades

Por tipo

`GET` http://fiwarelab.rnp.br:8004/v2/entities?type=Room

Por id

`GET` http://fiwarelab.rnp.br:8004/v2/entities/Room001

**Headers**
```javascript
'Fiware-Service': 'UFRN'
'Fiware-ServicePath': '/dimap'
```

### Registro de dispositivo

`POST` http://fiwarelab.rnp.br:8007/iot/devices

**Headers**
```javascript
'Content-Type': 'application/json'
'Fiware-Service': 'UFRN'
'Fiware-ServicePath': '/dimap'
```

**Body**
```javascript
{
  "devices": [
  	{
  	  "device_id": "SPLACE001",
      "entity_name": "RoomSPLACE",
      "entity_type": "thing",
      "timezone": "America/Fortaleza",
      "transport": "MQTT",
      "protocol": "IoTA-UL",
      "attributes": [
        {
          "object_id": "t",
          "name": "temperature",
          "type": "float"
        },
        {
          "object_id": "h",
          "name": "humidity",
          "type": "float"
        },
        {
          "object_id": "p",
          "name": "presence",
          "type": "bool"
        },
        {
          "object_id": "np",
          "name": "num_people",
          "type": "int"
        },
        {
          "object_id": "sac",
          "name": "state_ac",
          "type": "bool"
        },
        {
          "object_id": "tac",
          "name": "temperature_ac",
          "type": "int"
        }
      ],
      "commands": [
        {
          "name": "change_state_ac",
          "type": "command",
          "value": "SPLACE001@change_state_ac|%s"
        },
        {
          "name": "change_temperature_ac",
          "type": "command",
          "value": "SPLACE001@change_temperature_ac|%d"
        }
      ],
      "static_attributes": [
        {
          "name": "device_id",
          "type": "string",
          "value": "SPLACE001"
        },
        {
          "name": "id_sala",
          "type": "string",
          "value": ""
        }
      ]
    }
  ]
}
```

### Listar dispositivos

`GET` http://fiwarelab.rnp.br:8007/iot/devices

**Headers**
```javascript
'Content-Type': 'application/json'
'Fiware-Service': 'UFRN'
'Fiware-ServicePath': '/dimap'
```

### Envio de dados

Usando UL-HTTP

`POST` http://fiwarelab.rnp.br:8006/iot/d?k=1a2b3c4d5e6f7h&i=SPLACE001

**Headers**
```javascript
'Content-Type': 'text/plain'
'Fiware-Service': 'UFRN'
'Fiware-ServicePath': '/dimap'
```

**Body**
```javascript
t|35|h|100|p|1
```

### Execução de comandos

`POST` http://fiwarelab.rnp.br:8004/v2/entities

**Headers**
```javascript
'Content-Type': 'application/json'
'Fiware-Service': 'UFRN'
'Fiware-ServicePath': '/dimap'
'Accept': 'application/json'
```

**Body**
```javascript
{
  "contextElements": [
    {
      "type": "thing",
      "isPattern": "false",
      "id": "RoomSPLACE",
      "attributes": [
        {
          "name": "change_state_ac",
          "type": "command",
          "value": "ON"
        }
      ]
    }
  ],
  "updateAction": "UPDATE"
}
```

### Armazenamento de dados históricos de leituras

`POST` http://fiwarelab.rnp.br:8004/v1/subscribeContext

**Headers**
```javascript
'Content-Type': 'application/json'
'Fiware-Service': 'UFRN'
'Fiware-ServicePath': '/dimap'
'Accept': 'application/json'
```

**Body**
```javascript
{
  "entities": [
    {
      "type": "thing",
      "isPattern": "false",
      "id": "SPLACE001"
    }
  ],
  "attributes": [ "temperature", "humidity", "presence" ],
  "notifyConditions": [
    {
      "type": "ONCHANGE",
      "condValues": [ "temperature", "humidity", "presence" ]
    }
  ],
  "reference": "http://fiwarelab.rnp.br:8010/notify",
  "duration": "P1Y",
  "throttling": "PT1S"
}
```
