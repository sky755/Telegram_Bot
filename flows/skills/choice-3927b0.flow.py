{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "85iuw6c9pn",
    "contentId": "builtin_single-choice-vkS-4A",
    "invalidContentId": "",
    "keywords": {
      "025": [
        "025",
        "Все ще не допомагає"
      ],
      "toStart": [
        "toStart",
        "Мені стало легше"
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
        "say #!builtin_single-choice-vkS-4A {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "386022"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"85iuw6c9pn\",\"contentId\":\"builtin_single-choice-vkS-4A\",\"invalidContentId\":\"\",\"keywords\":{\"025\":[\"025\",\"Все ще не допомагає\"],\"toStart\":[\"toStart\",\"Мені стало легше\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-85iuw6c9pn'] === true",
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
      "id": "242637"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"85iuw6c9pn\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-85iuw6c9pn']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "373968"
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
      "id": "285198"
    }
  ]
}