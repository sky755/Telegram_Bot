{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "rjb4frqpf7",
    "contentId": "builtin_single-choice-kIQGT-",
    "invalidContentId": "",
    "keywords": {
      "A4": [
        "A4",
        "Мені потрібно отримати консультацію"
      ],
      "A5": [
        "A5",
        "Давай далі"
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
        "say #!builtin_single-choice-kIQGT- {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "241965"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"rjb4frqpf7\",\"contentId\":\"builtin_single-choice-kIQGT-\",\"invalidContentId\":\"\",\"keywords\":{\"A4\":[\"A4\",\"Мені потрібно отримати консультацію\"],\"A5\":[\"A5\",\"Давай далі\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-rjb4frqpf7'] === true",
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
      "id": "091021"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"rjb4frqpf7\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-rjb4frqpf7']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "205822"
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
      "id": "414689"
    }
  ]
}