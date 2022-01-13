{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "7h2wk4hex6",
    "contentId": "builtin_single-choice-_iJvgg",
    "invalidContentId": "",
    "keywords": {
      "825": [
        "825",
        "Тут все зрозуміло, давай повернемось до початку розмови"
      ],
      "feedback": [
        "feedback",
        " Так, я хочу, щоб зі мною зв'язалися"
      ],
      "contacts": [
        "contacts",
        "Мені терміново! покажи Горячі лінії"
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
        "say #!builtin_single-choice-_iJvgg {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "952961"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"7h2wk4hex6\",\"contentId\":\"builtin_single-choice-_iJvgg\",\"invalidContentId\":\"\",\"keywords\":{\"825\":[\"825\",\"Тут все зрозуміло, давай повернемось до початку розмови\"],\"feedback\":[\"feedback\",\" Так, я хочу, щоб зі мною зв'язалися\"],\"contacts\":[\"contacts\",\"Мені терміново! покажи Горячі лінії\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-7h2wk4hex6'] === true",
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
      "id": "796607"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"7h2wk4hex6\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-7h2wk4hex6']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "325332"
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
      "id": "240026"
    }
  ]
}