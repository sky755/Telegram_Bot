{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "sl3mc31yzy",
    "contentId": "builtin_single-choice-nBG4qC",
    "invalidContentId": "",
    "keywords": {
      "toStart": [
        "toStart",
        "На початок"
      ],
      "fk-4": [
        "fk-4",
        "Так, хочу ще щось додати"
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
        "say #!builtin_single-choice-nBG4qC {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "115342"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"sl3mc31yzy\",\"contentId\":\"builtin_single-choice-nBG4qC\",\"invalidContentId\":\"\",\"keywords\":{\"toStart\":[\"toStart\",\"На початок\"],\"fk-4\":[\"fk-4\",\"Так, хочу ще щось додати\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-sl3mc31yzy'] === true",
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
      "id": "168277"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"sl3mc31yzy\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-sl3mc31yzy']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "899647"
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
      "id": "466929"
    }
  ]
}