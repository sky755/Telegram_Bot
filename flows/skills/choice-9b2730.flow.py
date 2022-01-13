{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "a5m6vjk1lk",
    "contentId": "builtin_single-choice-iziwvV",
    "invalidContentId": "",
    "keywords": {
      "man": [
        "man",
        "Чоловіча"
      ],
      "woman": [
        "woman",
        "Жіноча"
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
        "say #!builtin_single-choice-iziwvV {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "612226"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"a5m6vjk1lk\",\"contentId\":\"builtin_single-choice-iziwvV\",\"invalidContentId\":\"\",\"keywords\":{\"man\":[\"man\",\"Чоловіча\"],\"woman\":[\"woman\",\"Жіноча\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-a5m6vjk1lk'] === true",
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
      "id": "962124"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"a5m6vjk1lk\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-a5m6vjk1lk']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "996138"
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
      "id": "704693"
    }
  ]
}