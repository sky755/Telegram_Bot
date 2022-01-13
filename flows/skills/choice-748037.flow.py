{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "m43vfxs2g0",
    "contentId": "builtin_single-choice-lzCAZN",
    "invalidContentId": "",
    "keywords": {
      "029": [
        "029",
        "Я хочу звернутися до Open Doors"
      ],
      "startExercise": [
        "startExercise",
        "Давай ще раз вправи на самозаспокоєння"
      ],
      "toStart": [
        "toStart",
        "Краще повернемось до початку розмови"
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
        "say #!builtin_single-choice-lzCAZN {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "052806"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"m43vfxs2g0\",\"contentId\":\"builtin_single-choice-lzCAZN\",\"invalidContentId\":\"\",\"keywords\":{\"029\":[\"029\",\"Я хочу звернутися до Open Doors\"],\"startExercise\":[\"startExercise\",\"Давай ще раз вправи на самозаспокоєння\"],\"toStart\":[\"toStart\",\"Краще повернемось до початку розмови\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-m43vfxs2g0'] === true",
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
      "id": "019962"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"m43vfxs2g0\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-m43vfxs2g0']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "649595"
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
      "id": "914791"
    }
  ]
}