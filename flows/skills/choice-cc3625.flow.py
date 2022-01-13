{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "pb2zssjv3j",
    "contentId": "builtin_single-choice-Tbnqs6",
    "invalidContentId": "",
    "keywords": {
      "contacts": [
        "contacts",
        "Покажи інші Горячі лінії"
      ],
      "toStart": [
        "toStart",
        "Повернемося до початку нашої бесіди"
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
      "id": "735656"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"pb2zssjv3j\",\"contentId\":\"builtin_single-choice-Tbnqs6\",\"invalidContentId\":\"\",\"keywords\":{\"contacts\":[\"contacts\",\"Покажи інші Горячі лінії\"],\"toStart\":[\"toStart\",\"Повернемося до початку нашої бесіди\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-pb2zssjv3j'] === true",
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
      "id": "024208"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"pb2zssjv3j\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-pb2zssjv3j']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "165303"
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
      "id": "262673"
    }
  ]
}