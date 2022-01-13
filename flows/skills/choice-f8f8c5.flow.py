{
  "version": "0.0.1",
  "catchAll": {
    "next": []
  },
  "startNode": "entry",
  "skillData": {
    "randomId": "actvnvwfkq",
    "contentId": "builtin_single-choice-UPoS52",
    "invalidContentId": "",
    "keywords": {
      "823-1": [
        "823-1",
        "А до кого тоді мені звернутися за порадою, якщо я не впевнений у своїх діях як свідок?"
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
      "id": "759997"
    },
    {
      "name": "parse",
      "onReceive": [
        "basic-skills/choice_parse_answer {\"randomId\":\"actvnvwfkq\",\"contentId\":\"builtin_single-choice-UPoS52\",\"invalidContentId\":\"\",\"keywords\":{\"823-1\":[\"823-1\",\"А до кого тоді мені звернутися за порадою, якщо я не впевнений у своїх діях як свідок?\"],\"823-2\":[\"823-2\",\"Надай мені краще контакти психологів\"]},\"config\":{\"nbMaxRetries\":3,\"repeatChoicesOnInvalid\":false,\"variableName\":\"\"}}"
      ],
      "next": [
        {
          "condition": "temp['skill-choice-valid-actvnvwfkq'] === true",
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
      "id": "522835"
    },
    {
      "name": "invalid",
      "onEnter": [
        "basic-skills/choice_invalid_answer {\"randomId\":\"actvnvwfkq\"}"
      ],
      "next": [
        {
          "condition": "Number(temp['skill-choice-invalid-count-actvnvwfkq']) > Number(3)",
          "node": "#"
        },
        {
          "condition": "true",
          "node": "sorry"
        }
      ],
      "id": "698296"
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
      "id": "404351"
    }
  ]
}