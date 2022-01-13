{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "dqyvss0l77",
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
      "id": "426253"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"dqyvss0l77\",\"contentId\":\"builtin_single-choice-Tbnqs6\",\"invalidContentId\":\"\",\"keywords\":{\"contacts\":[\"contacts\",\"Покажи інші Горячі лінії\"],\"toStart\":[\"toStart\",\"Повернемося до початку нашої бесіди\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-dqyvss0l77'] === true",
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
      "id": "983751"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"dqyvss0l77\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-dqyvss0l77']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "666557"
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
      "id": "816013"
    }
  ]
}