{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "y8jbmm3gfw",
    "contentId": "builtin_single-choice-M52ZN4",
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
        "Не визначився"
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
        "say #!builtin_single-choice-M52ZN4 {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "339882"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"y8jbmm3gfw\",\"contentId\":\"builtin_single-choice-M52ZN4\",\"invalidContentId\":\"\",\"keywords\":{\"88\":[\"88\",\"Впродовж 24 годин\"],\"89\":[\"89\",\"Впродовж наступного тижня\"],\"810\":[\"810\",\"Не визначився\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-y8jbmm3gfw'] === true",
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
      "id": "014569"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"y8jbmm3gfw\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-y8jbmm3gfw']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "100057"
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
      "id": "646101"
    }
  ]
}