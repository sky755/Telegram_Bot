{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "awqg30wfuo",
    "contentId": "builtin_single-choice-B08OOR",
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
        "say #!builtin_single-choice-B08OOR {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "139058"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"awqg30wfuo\",\"contentId\":\"builtin_single-choice-B08OOR\",\"invalidContentId\":\"\",\"keywords\":{\"A6\":[\"A6\",\"Мені потрібно отримати консультацію\"],\"A7\":[\"A7\",\"Чому я маю вважати це проблемою?\"],\"A8\":[\"A8\",\"В мене все в порядку!\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-awqg30wfuo'] === true",
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
      "id": "683838"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"awqg30wfuo\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-awqg30wfuo']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "203962"
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
      "id": "814557"
    }
  ]
}