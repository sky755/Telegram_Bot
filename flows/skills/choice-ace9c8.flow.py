{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "s6aagbdtlz",
    "contentId": "builtin_single-choice-zgjQlD",
    "invalidContentId": "",
    "keywords": {
      "nextExample-2": [
        "nextExample-2",
        "Видно, що це доволі важка тема... Можна і тут на прикладах?"
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
        "say #!builtin_single-choice-zgjQlD {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "270073"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"s6aagbdtlz\",\"contentId\":\"builtin_single-choice-zgjQlD\",\"invalidContentId\":\"\",\"keywords\":{\"nextExample-2\":[\"nextExample-2\",\"Видно, що це доволі важка тема... Можна і тут на прикладах?\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-s6aagbdtlz'] === true",
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
      "id": "876667"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"s6aagbdtlz\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-s6aagbdtlz']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "555909"
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
      "id": "758798"
    }
  ]
}