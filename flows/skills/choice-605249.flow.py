{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "pmp2pvbems",
    "contentId": "builtin_single-choice-Wt1bV6",
    "invalidContentId": "",
    "keywords": {
      "A9": [
        "A9",
        "То як мені звернутись до психолога?"
      ],
      "A10": [
        "A10",
        "Повернемось до початку розмови"
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
        "say #!builtin_single-choice-Wt1bV6 {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "079276"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"pmp2pvbems\",\"contentId\":\"builtin_single-choice-Wt1bV6\",\"invalidContentId\":\"\",\"keywords\":{\"A9\":[\"A9\",\"То як мені звернутись до психолога?\"],\"A10\":[\"A10\",\"Повернемось до початку розмови\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-pmp2pvbems'] === true",
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
      "id": "895215"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"pmp2pvbems\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-pmp2pvbems']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "834805"
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
      "id": "183168"
    }
  ]
}