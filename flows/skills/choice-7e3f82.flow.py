{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "4zv6a8b6nl",
    "contentId": "builtin_single-choice-dHdWV4",
    "invalidContentId": "",
    "keywords": {
      "815": [
        "815",
        "Давай спробуємо"
      ],
      "816": [
        "816",
        "Ні. Мені це точно не потрібно"
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
        "say #!builtin_single-choice-dHdWV4 {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "999995"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"4zv6a8b6nl\",\"contentId\":\"builtin_single-choice-dHdWV4\",\"invalidContentId\":\"\",\"keywords\":{\"815\":[\"815\",\"Давай спробуємо\"],\"816\":[\"816\",\"Ні. Мені це точно не потрібно\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-4zv6a8b6nl'] === true",
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
      "id": "855083"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"4zv6a8b6nl\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-4zv6a8b6nl']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "832725"
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
      "id": "244845"
    }
  ]
}