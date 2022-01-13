{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "8wnthdk9um",
    "contentId": "builtin_single-choice-JPr09W",
    "invalidContentId": "",
    "keywords": {
      "whatIsNext": [
        "whatIsNext",
        "Що далі?"
      ],
      "imDone": [
        "imDone",
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
        "say #!builtin_single-choice-JPr09W {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "025627"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"8wnthdk9um\",\"contentId\":\"builtin_single-choice-JPr09W\",\"invalidContentId\":\"\",\"keywords\":{\"whatIsNext\":[\"whatIsNext\",\"Що далі?\"],\"imDone\":[\"imDone\",\"Мені стало легше\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-8wnthdk9um'] === true",
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
      "id": "972396"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"8wnthdk9um\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-8wnthdk9um']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "608711"
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
      "id": "744528"
    }
  ]
}