{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "gdr3ccmgcp",
    "contentId": "builtin_single-choice-n0m4fN",
    "invalidContentId": "",
    "keywords": {
      "feedback": [
        "feedback",
        "Проблему не вирішено... Як написати до Невидимого батальйону?"
      ],
      "contacts": [
        "contacts",
        "Покажи інші Горячі лінії"
      ],
      "toStart": [
        "toStart",
        "Повернемося на початок нашої бесіди"
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
        "say #!builtin_single-choice-n0m4fN {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "797115"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"gdr3ccmgcp\",\"contentId\":\"builtin_single-choice-n0m4fN\",\"invalidContentId\":\"\",\"keywords\":{\"feedback\":[\"feedback\",\"Проблему не вирішено... Як написати до Невидимого батальйону?\"],\"contacts\":[\"contacts\",\"Покажи інші Горячі лінії\"],\"toStart\":[\"toStart\",\"Повернемося на початок нашої бесіди\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-gdr3ccmgcp'] === true",
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
      "id": "471518"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"gdr3ccmgcp\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-gdr3ccmgcp']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "797053"
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
      "id": "452539"
    }
  ]
}