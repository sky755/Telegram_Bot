{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "0nrl54fslg",
    "contentId": "builtin_single-choice-qvmcTR",
    "invalidContentId": "",
    "keywords": {
      "823": [
        "823",
        "Чи є до кого звертатися за поразкою, якщо я не впевнений у своїх діях як свідок?"
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
        "say #!builtin_single-choice-qvmcTR {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "428189"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"0nrl54fslg\",\"contentId\":\"builtin_single-choice-qvmcTR\",\"invalidContentId\":\"\",\"keywords\":{\"823\":[\"823\",\"Чи є до кого звертатися за поразкою, якщо я не впевнений у своїх діях як свідок?\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-0nrl54fslg'] === true",
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
      "id": "117732"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"0nrl54fslg\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-0nrl54fslg']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "386509"
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
      "id": "823351"
    }
  ]
}