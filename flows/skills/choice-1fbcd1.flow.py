{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "c9i2f0hqcz",
    "contentId": "builtin_single-choice-Lam0XF",
    "invalidContentId": "",
    "keywords": {
      "exercise7": [
        "exercise7",
        "Все ще не допомагає"
      ],
      "imDone": [
        "imDone",
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
        "say #!builtin_single-choice-Lam0XF {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "057796"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"c9i2f0hqcz\",\"contentId\":\"builtin_single-choice-Lam0XF\",\"invalidContentId\":\"\",\"keywords\":{\"exercise7\":[\"exercise7\",\"Все ще не допомагає\"],\"imDone\":[\"imDone\",\"Мені стало легше\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-c9i2f0hqcz'] === true",
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
      "id": "502871"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"c9i2f0hqcz\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-c9i2f0hqcz']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "178854"
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
      "id": "582570"
    }
  ]
}