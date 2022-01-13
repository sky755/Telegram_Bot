{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "l6tdj2xr9l",
    "contentId": "builtin_single-choice-Sq-Tps",
    "invalidContentId": "",
    "keywords": {
      "nextExample": [
        "nextExample",
        "Видно, що це доволі важка тема, можна і тут на прикладах?"
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
        "say #!builtin_single-choice-Sq-Tps {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "915785"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"l6tdj2xr9l\",\"contentId\":\"builtin_single-choice-Sq-Tps\",\"invalidContentId\":\"\",\"keywords\":{\"nextExample\":[\"nextExample\",\"Видно, що це доволі важка тема, можна і тут на прикладах?\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-l6tdj2xr9l'] === true",
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
      "id": "641824"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"l6tdj2xr9l\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-l6tdj2xr9l']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "157817"
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
      "id": "519545"
    }
  ]
}