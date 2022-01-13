{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "k59r3efydw",
    "contentId": "builtin_single-choice-l_APOu",
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
        "say #!builtin_single-choice-l_APOu {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "477816"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"k59r3efydw\",\"contentId\":\"builtin_single-choice-l_APOu\",\"invalidContentId\":\"\",\"keywords\":{\"eventPartisipant\":[\"eventPartisipant\",\"Так, я був учасником\"],\"witness\":[\"witness\",\"Мені довелося бути свідком\"],\"aboutProblem\":[\"aboutProblem\",\"Я хочу дізнатися про суть цієї проблеми\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-k59r3efydw'] === true",
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
      "id": "294021"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"k59r3efydw\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-k59r3efydw']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "375941"
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
      "id": "522601"
    }
  ]
}