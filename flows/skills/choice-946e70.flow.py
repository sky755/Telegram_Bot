{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "w3k1uu30xl",
    "contentId": "builtin_single-choice-WqLY_1",
    "invalidContentId": "",
    "keywords": {
      "A4": [
        "A4",
        "Мені потрібно отримати консультацію"
      ],
      "A5": [
        "A5",
        "Давай далі"
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
        "say #!builtin_single-choice-WqLY_1 {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "718776"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"w3k1uu30xl\",\"contentId\":\"builtin_single-choice-WqLY_1\",\"invalidContentId\":\"\",\"keywords\":{\"A4\":[\"A4\",\"Мені потрібно отримати консультацію\"],\"A5\":[\"A5\",\"Давай далі\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-w3k1uu30xl'] === true",
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
      "id": "524449"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"w3k1uu30xl\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-w3k1uu30xl']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "527769"
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
      "id": "292480"
    }
  ]
}