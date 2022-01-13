{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "djeb60yr80",
    "contentId": "builtin_single-choice-ysryVH",
    "invalidContentId": "",
    "keywords": {
      "prometeus": [
        "prometeus",
        "Де про це можна дізнатись у більш широкому форматі?"
      ],
      "aboutProblem": [
        "aboutProblem",
        "Підкажи, а як юридично правильно оформити факт дискримінації чи насильства?"
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
        "say #!builtin_single-choice-ysryVH {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "224427"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"djeb60yr80\",\"contentId\":\"builtin_single-choice-ysryVH\",\"invalidContentId\":\"\",\"keywords\":{\"prometeus\":[\"prometeus\",\"Де про це можна дізнатись у більш широкому форматі?\"],\"aboutProblem\":[\"aboutProblem\",\"Підкажи, а як юридично правильно оформити факт дискримінації чи насильства?\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-djeb60yr80'] === true",
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
      "id": "417278"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"djeb60yr80\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-djeb60yr80']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "887675"
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
      "id": "571266"
    }
  ]
}