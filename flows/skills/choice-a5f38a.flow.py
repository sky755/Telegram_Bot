{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "mw3peg919g",
    "contentId": "builtin_single-choice-O7ujl5",
    "invalidContentId": "",
    "keywords": {
      "toStart": [
        "toStart",
        "На початок"
      ],
      "sendMail": [
        "sendMail",
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
        "say #!builtin_single-choice-O7ujl5 {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "697660"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"mw3peg919g\",\"contentId\":\"builtin_single-choice-O7ujl5\",\"invalidContentId\":\"\",\"keywords\":{\"toStart\":[\"toStart\",\"На початок\"],\"sendMail\":[\"sendMail\",\"Так я хочу написати листа\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-mw3peg919g'] === true",
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
      "id": "107842"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"mw3peg919g\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-mw3peg919g']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "366452"
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
      "id": "471912"
    }
  ]
}