{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "5sjmc5dsq2",
    "contentId": "builtin_single-choice-0GG4Ns",
    "invalidContentId": "",
    "keywords": {
      "startExercise": [
        "startExercise",
        "Давай спробуємо вправи"
      ],
      "test-new-0": [
        "test-new-0",
        "Я хочу пройти самотестування"
      ],
      "toStart": [
        "toStart",
        "Двай повернемось до початку розмови"
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
        "say #!builtin_single-choice-0GG4Ns {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "892605"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"5sjmc5dsq2\",\"contentId\":\"builtin_single-choice-0GG4Ns\",\"invalidContentId\":\"\",\"keywords\":{\"startExercise\":[\"startExercise\",\"Давай спробуємо вправи\"],\"test-new-0\":[\"test-new-0\",\"Я хочу пройти самотестування\"],\"toStart\":[\"toStart\",\"Двай повернемось до початку розмови\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-5sjmc5dsq2'] === true",
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
      "id": "113330"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"5sjmc5dsq2\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-5sjmc5dsq2']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "449657"
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
      "id": "157745"
    }
  ]
}