{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "xs3wnkmaag",
    "contentId": "builtin_single-choice-WCHsDI",
    "invalidContentId": "",
    "keywords": {
      "thx": [
        "thx",
        "Дякую"
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
        "say #!builtin_single-choice-WCHsDI {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "757210"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"xs3wnkmaag\",\"contentId\":\"builtin_single-choice-WCHsDI\",\"invalidContentId\":\"\",\"keywords\":{\"thx\":[\"thx\",\"Дякую\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-xs3wnkmaag'] === true",
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
      "id": "017705"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"xs3wnkmaag\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-xs3wnkmaag']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "225715"
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
      "id": "631648"
    }
  ]
}