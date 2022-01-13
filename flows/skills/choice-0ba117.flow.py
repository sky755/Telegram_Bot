{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "t8dt08vnlr",
    "contentId": "builtin_single-choice-1I8MEj",
    "invalidContentId": "",
    "keywords": {
      "eventPartisipant": [
        "eventPartisipant",
        "Так, я був учасником/цею"
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
        "say #!builtin_single-choice-1I8MEj {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "414703"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"t8dt08vnlr\",\"contentId\":\"builtin_single-choice-1I8MEj\",\"invalidContentId\":\"\",\"keywords\":{\"eventPartisipant\":[\"eventPartisipant\",\"Так, я був учасником/цею\"],\"witness\":[\"witness\",\"Мені довелося бути свідком\"],\"aboutProblem\":[\"aboutProblem\",\"Я хочу дізнатися про суть цієї проблеми\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-t8dt08vnlr'] === true",
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
      "id": "190986"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"t8dt08vnlr\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-t8dt08vnlr']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "257788"
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
      "id": "686279"
    }
  ]
}