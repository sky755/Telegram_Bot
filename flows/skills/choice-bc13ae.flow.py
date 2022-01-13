{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "xn4hms3uqd",
    "contentId": "builtin_single-choice-aV0p_e",
    "invalidContentId": "",
    "keywords": {
      "A9-3": [
        "A9-3",
        "То як мені звернутись до психолога?"
      ],
      "toStart": [
        "toStart",
        "Повернемося до початку розмови"
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
        "say #!builtin_single-choice-aV0p_e {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "439842"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"xn4hms3uqd\",\"contentId\":\"builtin_single-choice-aV0p_e\",\"invalidContentId\":\"\",\"keywords\":{\"A9-3\":[\"A9-3\",\"То як мені звернутись до психолога?\"],\"toStart\":[\"toStart\",\"Повернемося до початку розмови\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-xn4hms3uqd'] === true",
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
      "id": "519260"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"xn4hms3uqd\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-xn4hms3uqd']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "133254"
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
      "id": "522489"
    }
  ]
}