{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "osn8x8i3cq",
    "contentId": "builtin_single-choice-llJsDJ",
    "invalidContentId": "",
    "keywords": {
      "825": [
        "825",
        "Тут все зрозуміло, давай повернемось до початку розмови"
      ],
      "feedback": [
        "feedback",
        "Так, я хочу, щоб зі мною зв'язалися"
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
        "say #!builtin_single-choice-llJsDJ {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "493678"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"osn8x8i3cq\",\"contentId\":\"builtin_single-choice-llJsDJ\",\"invalidContentId\":\"\",\"keywords\":{\"825\":[\"825\",\"Тут все зрозуміло, давай повернемось до початку розмови\"],\"feedback\":[\"feedback\",\"Так, я хочу, щоб зі мною зв'язалися\"],\"contacts\":[\"contacts\",\"Мені терміново! покажи Горячі лінії\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-osn8x8i3cq'] === true",
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
      "id": "619987"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"osn8x8i3cq\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-osn8x8i3cq']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "414148"
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
      "id": "941183"
    }
  ]
}