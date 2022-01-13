{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "0w25zlir01",
    "contentId": "builtin_single-choice-JUQXHC",
    "invalidContentId": "",
    "keywords": {
      "manTest": [
        "manTest",
        "Чол"
      ],
      "womenTest": [
        "womenTest",
        "Жін"
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
        "say #!builtin_single-choice-JUQXHC {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "728714"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"0w25zlir01\",\"contentId\":\"builtin_single-choice-JUQXHC\",\"invalidContentId\":\"\",\"keywords\":{\"manTest\":[\"manTest\",\"Чол\"],\"womenTest\":[\"womenTest\",\"Жін\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-0w25zlir01'] === true",
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
      "id": "677781"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"0w25zlir01\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-0w25zlir01']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "318320"
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
      "id": "227243"
    }
  ]
}