{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "htolzhhho1",
    "contentId": "builtin_single-choice-iedXRX",
    "invalidContentId": "",
    "keywords": {
      "feedback": [
        "feedback",
        "Я хочу написати листа"
      ],
      "aboutProblem": [
        "aboutProblem",
        "А юридичні аспекти цього питання?"
      ],
      "toStart": [
        "toStart",
        "Повернемось на початок розмови"
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
        "say #!builtin_single-choice-iedXRX {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "942623"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"htolzhhho1\",\"contentId\":\"builtin_single-choice-iedXRX\",\"invalidContentId\":\"\",\"keywords\":{\"feedback\":[\"feedback\",\"Я хочу написати листа\"],\"aboutProblem\":[\"aboutProblem\",\"А юридичні аспекти цього питання?\"],\"toStart\":[\"toStart\",\"Повернемось на початок розмови\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-htolzhhho1'] === true",
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
      "id": "679017"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"htolzhhho1\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-htolzhhho1']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "980560"
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
      "id": "477863"
    }
  ]
}