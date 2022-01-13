{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "fbozlbprfp",
    "contentId": "builtin_single-choice-WUNvj7",
    "invalidContentId": "",
    "keywords": {
      "A6": [
        "A6",
        "Мені потрібно отримати консультацію"
      ],
      "A7": [
        "A7",
        "Чому я маю вважати це проблемою?"
      ],
      "A8": [
        "A8",
        "В мене все в порядку!"
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
        "say #!builtin_single-choice-WUNvj7 {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "002104"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"fbozlbprfp\",\"contentId\":\"builtin_single-choice-WUNvj7\",\"invalidContentId\":\"\",\"keywords\":{\"A6\":[\"A6\",\"Мені потрібно отримати консультацію\"],\"A7\":[\"A7\",\"Чому я маю вважати це проблемою?\"],\"A8\":[\"A8\",\"В мене все в порядку!\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-fbozlbprfp'] === true",
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
      "id": "735143"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"fbozlbprfp\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-fbozlbprfp']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "380002"
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
      "id": "722983"
    }
  ]
}