{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "ofl9xrdsmm",
    "contentId": "builtin_single-choice-3DN9Cu",
    "invalidContentId": "",
    "keywords": {
      "74": [
        "74",
        "Надай"
      ],
      "75": [
        "75",
        "Давай повернемось до початку розмови"
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
        "say #!builtin_single-choice-3DN9Cu {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "539006"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"ofl9xrdsmm\",\"contentId\":\"builtin_single-choice-3DN9Cu\",\"invalidContentId\":\"\",\"keywords\":{\"74\":[\"74\",\"Надай\"],\"75\":[\"75\",\"Давай повернемось до початку розмови\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-ofl9xrdsmm'] === true",
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
      "id": "825697"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"ofl9xrdsmm\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-ofl9xrdsmm']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "868399"
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
      "id": "051153"
    }
  ]
}