{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "a9aovwtdff",
    "contentId": "builtin_single-choice-0ELvNj",
    "invalidContentId": "",
    "keywords": {
      "exercise6": [
        "exercise6",
        "Давай до наступної врпави"
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
        "say #!builtin_single-choice-0ELvNj {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "149351"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"a9aovwtdff\",\"contentId\":\"builtin_single-choice-0ELvNj\",\"invalidContentId\":\"\",\"keywords\":{\"exercise6\":[\"exercise6\",\"Давай до наступної врпави\"],\"imDone\":[\"imDone\",\"Мені стало легше\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-a9aovwtdff'] === true",
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
      "id": "491156"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"a9aovwtdff\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-a9aovwtdff']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "105341"
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
      "id": "270637"
    }
  ]
}