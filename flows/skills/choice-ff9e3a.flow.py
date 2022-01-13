{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "rgyt9p9hft",
    "contentId": "builtin_single-choice-LHlyid",
    "invalidContentId": "",
    "keywords": {
      "019": [
        "019",
        "Ще вправу, будь ласка"
      ],
      "020": [
        "020",
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
        "say #!builtin_single-choice-LHlyid {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "090764"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"rgyt9p9hft\",\"contentId\":\"builtin_single-choice-LHlyid\",\"invalidContentId\":\"\",\"keywords\":{\"019\":[\"019\",\"Ще вправу, будь ласка\"],\"020\":[\"020\",\"Мені стало легше\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-rgyt9p9hft'] === true",
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
      "id": "648104"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"rgyt9p9hft\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-rgyt9p9hft']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "887183"
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
      "id": "321492"
    }
  ]
}