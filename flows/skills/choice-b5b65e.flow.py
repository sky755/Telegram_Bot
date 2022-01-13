{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "l2glg0bkrv",
    "contentId": "builtin_single-choice-wm6vjv",
    "invalidContentId": "",
    "keywords": {
      "generalNext-01": [
        "generalNext-01",
        "Наче зрозуміло, а які приклади такого поводження?"
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
        "say #!builtin_single-choice-wm6vjv {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "904611"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"l2glg0bkrv\",\"contentId\":\"builtin_single-choice-wm6vjv\",\"invalidContentId\":\"\",\"keywords\":{\"generalNext-01\":[\"generalNext-01\",\"Наче зрозуміло, а які приклади такого поводження?\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-l2glg0bkrv'] === true",
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
      "id": "501924"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"l2glg0bkrv\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-l2glg0bkrv']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "467090"
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
      "id": "843705"
    }
  ]
}