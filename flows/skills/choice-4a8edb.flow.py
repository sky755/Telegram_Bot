{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "vb6aolw264",
    "contentId": "builtin_single-choice-EUKfTa",
    "invalidContentId": "",
    "keywords": {
      "feedbackNode": [
        "feedbackNode",
        "Написати. Я хочу щоб зі мною зв'язались"
      ],
      "toStart": [
        "toStart",
        "Давай повернемось до початку нашої розмови"
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
        "say #!builtin_single-choice-EUKfTa {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "329714"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"vb6aolw264\",\"contentId\":\"builtin_single-choice-EUKfTa\",\"invalidContentId\":\"\",\"keywords\":{\"feedbackNode\":[\"feedbackNode\",\"Написати. Я хочу щоб зі мною зв'язались\"],\"toStart\":[\"toStart\",\"Давай повернемось до початку нашої розмови\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-vb6aolw264'] === true",
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
      "id": "103207"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"vb6aolw264\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-vb6aolw264']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "370628"
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
      "id": "132829"
    }
  ]
}