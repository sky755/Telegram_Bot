{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "5g6c0yrgka",
    "contentId": "builtin_single-choice-FmHbwa",
    "invalidContentId": "",
    "keywords": {
      "81": [
        "81",
        "Так, я була учасником"
      ],
      "82": [
        "82",
        "Мені довелося бути свідком"
      ],
      "aboutProblem": [
        "aboutProblem",
        "Я хочу дізнатися про суть цієї проблеми"
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
        "say #!builtin_single-choice-FmHbwa {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "225983"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"5g6c0yrgka\",\"contentId\":\"builtin_single-choice-FmHbwa\",\"invalidContentId\":\"\",\"keywords\":{\"81\":[\"81\",\"Так, я була учасником\"],\"82\":[\"82\",\"Мені довелося бути свідком\"],\"aboutProblem\":[\"aboutProblem\",\"Я хочу дізнатися про суть цієї проблеми\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-5g6c0yrgka'] === true",
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
      "id": "967916"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"5g6c0yrgka\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-5g6c0yrgka']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "410030"
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
      "id": "363682"
    }
  ]
}