{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "4ykhf2iuiq",
    "contentId": "builtin_single-choice-kCjGd5",
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
        "Чесно кажучи, не впевнена"
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
        "say #!builtin_single-choice-kCjGd5 {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "967707"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"4ykhf2iuiq\",\"contentId\":\"builtin_single-choice-kCjGd5\",\"invalidContentId\":\"\",\"keywords\":{\"812\":[\"812\",\"Так\"],\"813\":[\"813\",\"Ні\"],\"814\":[\"814\",\"Чесно кажучи, не впевнена\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-4ykhf2iuiq'] === true",
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
      "id": "100921"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"4ykhf2iuiq\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-4ykhf2iuiq']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "376606"
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
      "id": "483247"
    }
  ]
}