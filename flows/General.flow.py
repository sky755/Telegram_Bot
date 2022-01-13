{
  "version": "0.0.1",
  "catchAll": {},
  "startNode": "choice-General0",
  "description": "",
  "nodes": [
    {
      "id": "skill-652d3b",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-General1",
      "flow": "skills/choice-652d3b.flow.json",
      "next": [
        {
          "caption": "User picked [general...]",
          "condition": "temp['skill-choice-ret-hc7gxtqyfu'] == \"generalNext\"",
          "node": "choice-General2"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-8bd044",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-General2",
      "flow": "skills/choice-8bd044.flow.json",
      "next": [
        {
          "caption": "User picked [nextExa...]",
          "condition": "temp['skill-choice-ret-l6tdj2xr9l'] == \"nextExample\"",
          "node": "choice-General2-01"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "629f7615a1",
      "name": "General3",
      "next": [
        {
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": [
        "say #!builtin_text-0wHR1S"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "skill-839c22",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-General4",
      "flow": "skills/choice-839c22.flow.json",
      "next": [
        {
          "caption": "User picked [15]",
          "condition": "temp['skill-choice-ret-qk9ove8c1f'] == \"15\"",
          "node": "choice-General5"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-fbeeb2",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-General0",
      "flow": "skills/choice-fbeeb2.flow.json",
      "next": [
        {
          "caption": "User picked [examples]",
          "condition": "temp['skill-choice-ret-25fhmqpaqz'] == \"examples\"",
          "node": "choice-General-01"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-90c4db",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-General5",
      "flow": "skills/choice-90c4db.flow.json",
      "next": [
        {
          "caption": "User picked [feedback]",
          "condition": "temp['skill-choice-ret-htolzhhho1'] == \"feedback\"",
          "node": "main.flow.json#feedbackNode"
        },
        {
          "caption": "User picked [aboutPr...]",
          "condition": "temp['skill-choice-ret-htolzhhho1'] == \"aboutProblem\"",
          "node": "Lawyer.flow.json"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-htolzhhho1'] == \"toStart\"",
          "node": "main.flow.json#secondStart"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-b5b65e",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-General-01",
      "flow": "skills/choice-b5b65e.flow.json",
      "next": [
        {
          "caption": "User picked [general...]",
          "condition": "temp['skill-choice-ret-l2glg0bkrv'] == \"generalNext-01\"",
          "node": "choice-General1"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-ace9c8",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-General2-1",
      "flow": "skills/choice-ace9c8.flow.json",
      "next": [
        {
          "caption": "User picked [nextExa...]",
          "condition": "temp['skill-choice-ret-s6aagbdtlz'] == \"nextExample-2\"",
          "node": "General3-1"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-583764",
      "type": "skill-call",
      "skill": "choice",
      "name": "General3-1",
      "flow": "skills/choice-583764.flow.json",
      "next": [
        {
          "caption": "User picked [promete...]",
          "condition": "temp['skill-choice-ret-djeb60yr80'] == \"prometeus\"",
          "node": "choice-General4"
        },
        {
          "caption": "User picked [aboutPr...]",
          "condition": "temp['skill-choice-ret-djeb60yr80'] == \"aboutProblem\"",
          "node": "Lawyer.flow.json"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "skill-defbca",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-General2-01",
      "flow": "skills/choice-defbca.flow.json",
      "next": [
        {
          "caption": "User picked [nextExa...]",
          "condition": "temp['skill-choice-ret-61x4mugqr3'] == \"nextExample-1\"",
          "node": "choice-General2-1"
        },
        {
          "caption": "On failure",
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": null,
      "onReceive": null
    }
  ]
}