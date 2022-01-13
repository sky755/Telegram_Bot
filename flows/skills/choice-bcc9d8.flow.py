{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "hgf9c57g48",
    "contentId": "builtin_single-choice-lBjydW",
    "invalidContentId": "",
    "keywords": {
      "contacts": [
        "contacts",
        "Надай всі наявні у тебе контакти гарячих ліній та спеціалістів"
      ],
      "conversation": [
        "conversation",
        "Поспілкуємось"
      ],
      "selfTest": [
        "selfTest",
        "Я хочу пройти самотестування"
      ],
      "recomendations": [
        "recomendations",
        "Зараз я дуже нервую і не можу адекватно сприймати інформацію"
      ],
      "feedback": [
        "feedback",
        "Надіслати відгук про мою роботу або Описати свою історію "
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
        "say #!builtin_single-choice-lBjydW {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "447334"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"hgf9c57g48\",\"contentId\":\"builtin_single-choice-lBjydW\",\"invalidContentId\":\"\",\"keywords\":{\"contacts\":[\"contacts\",\"Надай всі наявні у тебе контакти гарячих ліній та спеціалістів\"],\"conversation\":[\"conversation\",\"Поспілкуємось\"],\"selfTest\":[\"selfTest\",\"Я хочу пройти самотестування\"],\"recomendations\":[\"recomendations\",\"Зараз я дуже нервую і не можу адекватно сприймати інформацію\"],\"feedback\":[\"feedback\",\"Надіслати відгук про мою роботу або Описати свою історію \"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-hgf9c57g48'] === true",
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
      "id": "228984"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"hgf9c57g48\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-hgf9c57g48']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "776983"
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
      "id": "896976"
    }
  ]
}