{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "70dm0g9vxl",
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
      "id": "181188"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"70dm0g9vxl\",\"contentId\":\"builtin_single-choice-kIQGT-\",\"invalidContentId\":\"\",\"keywords\":{\"A4\":[\"A4\",\"Мені потрібно отримати консультацію\"],\"A5\":[\"A5\",\"Давай далі\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-70dm0g9vxl'] === true",
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
      "id": "530459"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"70dm0g9vxl\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-70dm0g9vxl']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "646729"
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
      "id": "018868"
    }
  ]
}