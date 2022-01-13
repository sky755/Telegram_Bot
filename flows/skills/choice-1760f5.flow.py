{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "va36x2d77i",
    "contentId": "builtin_single-choice-xSQ6Ov",
    "invalidContentId": "",
    "keywords": {
      "eventPartisipant": [
        "eventPartisipant",
        "Так, я був учасником"
      ],
      "witness": [
        "witness",
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
        "say #!builtin_single-choice-xSQ6Ov {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "755270"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"va36x2d77i\",\"contentId\":\"builtin_single-choice-xSQ6Ov\",\"invalidContentId\":\"\",\"keywords\":{\"eventPartisipant\":[\"eventPartisipant\",\"Так, я був учасником\"],\"witness\":[\"witness\",\"Мені довелося бути свідком\"],\"aboutProblem\":[\"aboutProblem\",\"Я хочу дізнатися про суть цієї проблеми\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-va36x2d77i'] === true",
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
      "id": "463774"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"va36x2d77i\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-va36x2d77i']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "040970"
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
      "id": "236644"
    }
  ]
}