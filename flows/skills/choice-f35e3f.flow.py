{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "lxjriiqurb",
    "contentId": "builtin_single-choice-NBbyI8",
    "invalidContentId": "",
    "keywords": {
      "88": [
        "88",
        "Впродовж 24 годин"
      ],
      "89": [
        "89",
        "Впродовж наступного тижня"
      ],
      "810": [
        "810",
        "Не визначилася"
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
        "say #!builtin_single-choice-NBbyI8 {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "893748"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"lxjriiqurb\",\"contentId\":\"builtin_single-choice-NBbyI8\",\"invalidContentId\":\"\",\"keywords\":{\"88\":[\"88\",\"Впродовж 24 годин\"],\"89\":[\"89\",\"Впродовж наступного тижня\"],\"810\":[\"810\",\"Не визначилася\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-lxjriiqurb'] === true",
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
      "id": "035717"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"lxjriiqurb\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-lxjriiqurb']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "554838"
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
      "id": "187171"
    }
  ]
}