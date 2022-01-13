{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "9tmmhvbe0y",
    "contentId": "builtin_single-choice-ERAXFB",
    "invalidContentId": "",
    "keywords": {
      "023": [
        "023",
        "Давай до наступної врпави"
      ],
      "toStart": [
        "toStart",
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
        "say #!builtin_single-choice-ERAXFB {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "636920"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"9tmmhvbe0y\",\"contentId\":\"builtin_single-choice-ERAXFB\",\"invalidContentId\":\"\",\"keywords\":{\"023\":[\"023\",\"Давай до наступної врпави\"],\"toStart\":[\"toStart\",\"Мені стало легше\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-9tmmhvbe0y'] === true",
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
      "id": "358716"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"9tmmhvbe0y\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-9tmmhvbe0y']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "775713"
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
      "id": "695562"
    }
  ]
}