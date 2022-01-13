{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "2x4fmhu4gm",
    "contentId": "builtin_single-choice-UPoS52",
    "invalidContentId": "",
    "keywords": {
      "823-1": [
        "823-1",
        "А чи є до кого звернутися за порадою, якщо я не впевнений у своїх діях як свідок?"
      ],
      "823-2": [
        "823-2",
        "Надай мені краще контакти психологів"
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
        "say #!builtin_single-choice-UPoS52 {\"skill\":\"choice\"}"
      ],
      "next": [
        {
          "condition": "true",
          "node": "parse"
        }
      ],
      "id": "004790"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"2x4fmhu4gm\",\"contentId\":\"builtin_single-choice-UPoS52\",\"invalidContentId\":\"\",\"keywords\":{\"823-1\":[\"823-1\",\"А чи є до кого звернутися за порадою, якщо я не впевнений у своїх діях як свідок?\"],\"823-2\":[\"823-2\",\"Надай мені краще контакти психологів\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-2x4fmhu4gm'] === true",
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
      "id": "628082"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"2x4fmhu4gm\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-2x4fmhu4gm']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "612312"
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
      "id": "905725"
    }
  ]
}