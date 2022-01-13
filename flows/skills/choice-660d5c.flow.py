{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "fsxn6zlpon",
    "contentId": "builtin_single-choice-R-8EKo",
    "invalidContentId": "",
    "keywords": {
      "1": [
        "1",
        "дати контакти"
      ],
      "2": [
        "2",
        "поспілкуємось"
      ],
      "3": [
        "3",
        "пройти тест"
      ],
      "4": [
        "4",
        "зараз не готовай"
      ],
      "5": [
        "5",
        "описати історію"
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
        "say #!builtin_single-choice-R-8EKo {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "792294"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"fsxn6zlpon\",\"contentId\":\"builtin_single-choice-R-8EKo\",\"invalidContentId\":\"\",\"keywords\":{\"1\":[\"1\",\"дати контакти\"],\"2\":[\"2\",\"поспілкуємось\"],\"3\":[\"3\",\"пройти тест\"],\"4\":[\"4\",\"зараз не готовай\"],\"5\":[\"5\",\"описати історію\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-fsxn6zlpon'] === true",
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
      "id": "579539"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"fsxn6zlpon\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-fsxn6zlpon']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "231551"
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
      "id": "745655"
    }
  ]
}