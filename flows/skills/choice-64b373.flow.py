{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "1yxb4taevs",
    "contentId": "builtin_single-choice-WSsWPD",
    "invalidContentId": "",
    "keywords": {
      "015": [
        "015",
        "Давай наступне"
      ],
      "016": [
        "016",
        "Мені стало легше"
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
        "say #!builtin_single-choice-WSsWPD {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "817837"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"1yxb4taevs\",\"contentId\":\"builtin_single-choice-WSsWPD\",\"invalidContentId\":\"\",\"keywords\":{\"015\":[\"015\",\"Давай наступне\"],\"016\":[\"016\",\"Мені стало легше\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-1yxb4taevs'] === true",
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
      "id": "433908"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"1yxb4taevs\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-1yxb4taevs']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "304649"
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
      "id": "291166"
    }
  ]
}