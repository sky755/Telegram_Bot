{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "hcv0lxqblr",
    "contentId": "builtin_single-choice-GF1-C1",
    "invalidContentId": "",
    "keywords": {
      "contacts": [
        "contacts",
        "Контакти"
      ],
      "conversation": [
        "conversation",
        "Поспілкуємось"
      ],
      "test": [
        "test",
        "Я хочу пройти самотестування"
      ],
      "alternative": [
        "alternative",
        "Зараз я дуже нервую і не можу адекватно сприймати інформацію"
      ],
      "api": [
        "api",
        "API Call"
      ]
    },
    "config": {
      "nbMaxRetries": 3,
      "repeatChoicesOnInvalid": false,
      "variableName": "Starter node"
    }
  },
  "nodes": [
    {
      "name": "entry",
      "onEnter": [
        "say #!builtin_single-choice-GF1-C1 {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "401613"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"Starter node\",\"contentId\":\"builtin_single-choice-GF1-C1\",\"invalidContentId\":\"\",\"keywords\":{\"contacts\":[\"contacts\",\"Контакти\"],\"conversation\":[\"conversation\",\"Поспілкуємось\"],\"test\":[\"test\",\"Я хочу пройти самотестування\"],\"alternative\":[\"alternative\",\"Зараз я дуже нервую і не можу адекватно сприймати інформацію\"],\"api\":[\"api\",\"API Call\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"Starter node\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-Starter node'] === true",
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
      "id": "566969"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"Starter node\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-Starter node']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "698104"
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
      "id": "765105"
    }
  ]
}