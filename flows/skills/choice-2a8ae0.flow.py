{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "s92w8ne9s9",
    "contentId": "builtin_single-choice-axCiXW",
    "invalidContentId": "",
    "keywords": {
      "72": [
        "72",
        "Ні я краще зроблю це самостійно"
      ],
      "73": [
        "73",
        "Надайте мені їх контакти"
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
        "say #!builtin_single-choice-axCiXW {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "896762"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"s92w8ne9s9\",\"contentId\":\"builtin_single-choice-axCiXW\",\"invalidContentId\":\"\",\"keywords\":{\"72\":[\"72\",\"Ні я краще зроблю це самостійно\"],\"73\":[\"73\",\"Надайте мені їх контакти\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-s92w8ne9s9'] === true",
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
      "id": "512574"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"s92w8ne9s9\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-s92w8ne9s9']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "097146"
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
      "id": "846211"
    }
  ]
}