{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "txwt8rcidu",
    "contentId": "builtin_single-choice-Tbnqs6",
    "invalidContentId": "",
    "keywords": {
      "contacts": [
        "contacts",
        "Покажи інші Горячі лінії"
      ],
      "toStart": [
        "toStart",
        "Повернемось до початку розмови"
      ]
    },
    "config": {
      "nbMaxRetries": 3,
      "repeatChoicesOnInvalid": false,
      "variableName": ""
    }
  },
  "nodes": [
    {
      "name": "entry",
      "onEnter": [
        "say #!builtin_single-choice-Tbnqs6 {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "826732"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"txwt8rcidu\",\"contentId\":\"builtin_single-choice-Tbnqs6\",\"invalidContentId\":\"\",\"keywords\":{\"contacts\":[\"contacts\",\"Покажи інші Горячі лінії\"],\"toStart\":[\"toStart\",\"Повернемось до початку розмови\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-txwt8rcidu'] === true",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "invalid"
        }
      ],
      "triggers": [
        {
          "conditions": [
            {
              "id": "always"
            }
          ]
        }
      ],
      "onEnter": [],
      "id": "005389"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"txwt8rcidu\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-txwt8rcidu']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "739483"
    },
    {
      "name": "sorry",
      "onEnter": [],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "145035"
    }
  ]
}