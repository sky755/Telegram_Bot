{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "k8xm34ld9p",
    "contentId": "builtin_single-choice-BKW_XI",
    "invalidContentId": "",
    "keywords": {
      "toStart": [
        "toStart",
        "Повернемось на початок розмови?"
      ],
      "feedbackNode": [
        "feedbackNode",
        "Написати повідомлення або залишити свої контакти"
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
        "say #!builtin_single-choice-BKW_XI {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "796802"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"k8xm34ld9p\",\"contentId\":\"builtin_single-choice-BKW_XI\",\"invalidContentId\":\"\",\"keywords\":{\"toStart\":[\"toStart\",\"Повернемось на початок розмови?\"],\"feedbackNode\":[\"feedbackNode\",\"Написати повідомлення або залишити свої контакти\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-k8xm34ld9p'] === true",
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
      "id": "737327"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"k8xm34ld9p\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-k8xm34ld9p']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "807473"
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
      "id": "819034"
    }
  ]
}