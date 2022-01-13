{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "d8istasych",
    "contentId": "builtin_single-choice-nC3XTo",
    "invalidContentId": "",
    "keywords": {
      "conversation": [
        "conversation",
        "Поспілкуємось"
      ],
      "contacts": [
        "contacts",
        "Надай всі наявні у тебе контакти гарячих ліній та спеціалістів"
      ],
      "General-new-0": [
        "General-new-0",
        "Я хочу дізнатися про суть цієї проблеми"
      ],
      "recomendations": [
        "recomendations",
        "Зараз я дуже нервую і не можу адекватно сприймати інформацію"
      ],
      "feedback": [
        "feedback",
        "Надіслати відгук про мою роботу"
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
        "say #!builtin_single-choice-nC3XTo {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "619311"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"d8istasych\",\"contentId\":\"builtin_single-choice-nC3XTo\",\"invalidContentId\":\"\",\"keywords\":{\"conversation\":[\"conversation\",\"Поспілкуємось\"],\"contacts\":[\"contacts\",\"Надай всі наявні у тебе контакти гарячих ліній та спеціалістів\"],\"General-new-0\":[\"General-new-0\",\"Я хочу дізнатися про суть цієї проблеми\"],\"recomendations\":[\"recomendations\",\"Зараз я дуже нервую і не можу адекватно сприймати інформацію\"],\"feedback\":[\"feedback\",\"Надіслати відгук про мою роботу\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-d8istasych'] === true",
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
      "id": "004634"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"d8istasych\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-d8istasych']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "314379"
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
      "id": "101823"
    }
  ]
}