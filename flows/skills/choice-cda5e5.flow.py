{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "5z3gyifk7a",
    "contentId": "builtin_single-choice-MIJOQs",
    "invalidContentId": "",
    "keywords": {
      "contacts": [
        "contacts",
        "Покажи інші Горячі лінії"
      ],
      "toStart": [
        "toStart",
        "Повернемося на початок нашої бесіди"
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
        "say #!builtin_single-choice-MIJOQs {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "663932"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"5z3gyifk7a\",\"contentId\":\"builtin_single-choice-MIJOQs\",\"invalidContentId\":\"\",\"keywords\":{\"contacts\":[\"contacts\",\"Покажи інші Горячі лінії\"],\"toStart\":[\"toStart\",\"Повернемося на початок нашої бесіди\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-5z3gyifk7a'] === true",
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
      "id": "594398"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"5z3gyifk7a\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-5z3gyifk7a']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "358871"
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
      "id": "479311"
    }
  ]
}