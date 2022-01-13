{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "mqmwlku0kz",
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
      "id": "169513"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"mqmwlku0kz\",\"contentId\":\"builtin_single-choice-dHdWV4\",\"invalidContentId\":\"\",\"keywords\":{\"815\":[\"815\",\"Давай спробуємо\"],\"816\":[\"816\",\"Ні. Мені це точно не потрібно\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-mqmwlku0kz'] === true",
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
      "id": "484527"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"mqmwlku0kz\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-mqmwlku0kz']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "690383"
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
      "id": "127000"
    }
  ]
}