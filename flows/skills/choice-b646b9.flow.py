{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "9aj1gzvblj",
    "contentId": "builtin_single-choice-hG0EIA",
    "invalidContentId": "",
    "keywords": {
      "812": [
        "812",
        "Так"
      ],
      "813": [
        "813",
        "Ні"
      ],
      "814": [
        "814",
        "Чесно кажучи, не впевнений"
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
        "say #!builtin_single-choice-hG0EIA {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "246924"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"9aj1gzvblj\",\"contentId\":\"builtin_single-choice-hG0EIA\",\"invalidContentId\":\"\",\"keywords\":{\"812\":[\"812\",\"Так\"],\"813\":[\"813\",\"Ні\"],\"814\":[\"814\",\"Чесно кажучи, не впевнений\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-9aj1gzvblj'] === true",
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
      "id": "225475"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"9aj1gzvblj\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-9aj1gzvblj']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "448106"
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
      "id": "321347"
    }
  ]
}