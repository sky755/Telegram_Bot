{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "szmed57u5n",
    "contentId": "builtin_single-choice-AsDb70",
    "invalidContentId": "",
    "keywords": {
      "021": [
        "021",
        "Що далі?"
      ],
      "022": [
        "022",
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
        "say #!builtin_single-choice-AsDb70 {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "591033"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"szmed57u5n\",\"contentId\":\"builtin_single-choice-AsDb70\",\"invalidContentId\":\"\",\"keywords\":{\"021\":[\"021\",\"Що далі?\"],\"022\":[\"022\",\"Мені стало легше\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-szmed57u5n'] === true",
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
      "id": "847483"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"szmed57u5n\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-szmed57u5n']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "372925"
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
      "id": "537958"
    }
  ]
}