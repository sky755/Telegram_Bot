{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "4tjjjro3di",
    "contentId": "builtin_single-choice-MIJOQs",
    "invalidContentId": "",
    "keywords": {
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
        "say #!builtin_single-choice-MIJOQs {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "188419"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"4tjjjro3di\",\"contentId\":\"builtin_single-choice-MIJOQs\",\"invalidContentId\":\"\",\"keywords\":{\"contacts\":[\"contacts\",\"Покажи інші Горячі лінії\"],\"toStart\":[\"toStart\",\"Повернемося на початок нашої бесіди\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-4tjjjro3di'] === true",
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
      "id": "904842"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"4tjjjro3di\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-4tjjjro3di']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "099762"
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
      "id": "806441"
    }
  ]
}