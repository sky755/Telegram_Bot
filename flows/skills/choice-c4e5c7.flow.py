{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "p9h7l24hkk",
    "contentId": "builtin_single-choice-3VoRD2",
    "invalidContentId": "",
    "keywords": {
      "toStart": [
        "toStart",
        "На початок"
      ],
      "feedback": [
        "feedback",
        "Так я хочу написати листа"
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
        "say #!builtin_single-choice-3VoRD2 {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "121893"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"p9h7l24hkk\",\"contentId\":\"builtin_single-choice-3VoRD2\",\"invalidContentId\":\"\",\"keywords\":{\"toStart\":[\"toStart\",\"На початок\"],\"feedback\":[\"feedback\",\"Так я хочу написати листа\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-p9h7l24hkk'] === true",
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
      "id": "227143"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"p9h7l24hkk\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-p9h7l24hkk']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "905981"
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
      "id": "781335"
    }
  ]
}