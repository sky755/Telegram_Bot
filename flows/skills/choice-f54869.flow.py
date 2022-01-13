{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "3t681eqxuj",
    "contentId": "builtin_single-choice-XLKK6Z",
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
        "say #!builtin_single-choice-XLKK6Z {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "589772"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"3t681eqxuj\",\"contentId\":\"builtin_single-choice-XLKK6Z\",\"invalidContentId\":\"\",\"keywords\":{\"toStart\":[\"toStart\",\"На початок\"],\"feedback\":[\"feedback\",\"Так я хочу написати листа\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-3t681eqxuj'] === true",
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
      "id": "375798"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"3t681eqxuj\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-3t681eqxuj']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "057258"
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
      "id": "130167"
    }
  ]
}