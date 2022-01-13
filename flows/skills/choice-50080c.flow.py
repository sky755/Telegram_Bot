{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "3e0z0n5mgc",
    "contentId": "builtin_single-choice-nkmTc6",
    "invalidContentId": "",
    "keywords": {
      "A2": [
        "A2",
        "Мені потрібно отримати консультацію"
      ],
      "A3": [
        "A3",
        "Продовжимо"
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
        "say #!builtin_single-choice-nkmTc6 {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "255604"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"3e0z0n5mgc\",\"contentId\":\"builtin_single-choice-nkmTc6\",\"invalidContentId\":\"\",\"keywords\":{\"A2\":[\"A2\",\"Мені потрібно отримати консультацію\"],\"A3\":[\"A3\",\"Продовжимо\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-3e0z0n5mgc'] === true",
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
      "id": "883503"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"3e0z0n5mgc\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-3e0z0n5mgc']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "212628"
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
      "id": "220741"
    }
  ]
}