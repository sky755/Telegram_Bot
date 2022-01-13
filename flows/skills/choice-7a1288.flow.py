{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "5ktfibmrsy",
    "contentId": "builtin_single-choice-sna1-T",
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
        "say #!builtin_single-choice-sna1-T {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "090935"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"5ktfibmrsy\",\"contentId\":\"builtin_single-choice-sna1-T\",\"invalidContentId\":\"\",\"keywords\":{\"conversation\":[\"conversation\",\"Поспілкуємось\"],\"contacts\":[\"contacts\",\"Надай всі наявні у тебе контакти гарячих ліній та спеціалістів\"],\"General-new-0\":[\"General-new-0\",\"Я хочу дізнатися про суть цієї проблеми\"],\"recomendations\":[\"recomendations\",\"Зараз я дуже нервую і не можу адекватно сприймати інформацію\"],\"feedback\":[\"feedback\",\"Надіслати відгук про мою роботу або Описати свою історію \"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-5ktfibmrsy'] === true",
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
      "id": "643501"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"5ktfibmrsy\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-5ktfibmrsy']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "716596"
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
      "id": "369309"
    }
  ]
}