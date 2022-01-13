{
  "version": "0.0.1",
  "catchAll": {},
  "startNode": "choice-entry",
  "description": "",
  "nodes": [
    {
      "id": "764c6464be",
      "type": "skill-call",
      "skill": "choice",
      "name": "S1",
      "flow": "skills/choice-50080c.flow.json",
      "next": [
        {
          "caption": "User picked [A2]",
          "condition": "temp['skill-choice-ret-3e0z0n5mgc'] == \"A2\"",
          "node": "choice-ff39ae-copy"
        },
        {
          "caption": "User picked [A3]",
          "condition": "temp['skill-choice-ret-3e0z0n5mgc'] == \"A3\"",
          "node": "S2"
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
      "id": "94c767cc78",
      "type": "skill-call",
      "skill": "choice",
      "name": "S2",
      "flow": "skills/choice-7dc9d7.flow.json",
      "next": [
        {
          "caption": "User picked [A4]",
          "condition": "temp['skill-choice-ret-rjb4frqpf7'] == \"A4\"",
          "node": "choice-ff39ae-copy"
        },
        {
          "caption": "User picked [A5]",
          "condition": "temp['skill-choice-ret-rjb4frqpf7'] == \"A5\"",
          "node": "S3"
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
      "id": "68fc2e5548",
      "type": "skill-call",
      "skill": "choice",
      "name": "S3",
      "flow": "skills/choice-1b132f.flow.json",
      "next": [
        {
          "caption": "User picked [A6]",
          "condition": "temp['skill-choice-ret-awqg30wfuo'] == \"A6\"",
          "node": "choice-ff39ae-copy"
        },
        {
          "caption": "User picked [A7]",
          "condition": "temp['skill-choice-ret-awqg30wfuo'] == \"A7\"",
          "node": "S4-drugs"
        },
        {
          "caption": "User picked [A8]",
          "condition": "temp['skill-choice-ret-awqg30wfuo'] == \"A8\"",
          "node": "S_Exit1"
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
      "id": "561044a0fb",
      "name": "S_Exit1",
      "next": [
        {
          "condition": "true",
          "node": "main.flow.json#secondStart"
        }
      ],
      "onEnter": [
        "say #!builtin_text-BVJveT"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "fb598cbf96",
      "type": "skill-call",
      "skill": "choice",
      "name": "S4-drugs",
      "flow": "skills/choice-5715f6.flow.json",
      "next": [
        {
          "caption": "User picked [A9]",
          "condition": "temp['skill-choice-ret-r9qxamlm32'] == \"A9\"",
          "node": "S4-drugs-1"
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
      "id": "85310d8ff0",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-S0",
      "flow": "skills/choice-c8e017.flow.json",
      "next": [
        {
          "caption": "User picked [a1]",
          "condition": "temp['skill-choice-ret-ni8b6igxxs'] == \"a1\"",
          "node": ""
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
      "id": "skill-fb6528",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-entry",
      "flow": "skills/choice-fb6528.flow.json",
      "next": [
        {
          "caption": "User picked [nextTest]",
          "condition": "temp['skill-choice-ret-82u8b2a9sw'] == \"nextTest\"",
          "node": "S1"
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
      "id": "0849c7f645",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-ff39ae-copy",
      "flow": "skills/choice-ff39ae.flow.json",
      "next": [
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-jzezjki293'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-jzezjki293'] == \"toStart\"",
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
      "id": "skill-4639ba",
      "type": "skill-call",
      "skill": "choice",
      "name": "S4-drugs-1",
      "flow": "skills/choice-4639ba.flow.json",
      "next": [
        {
          "caption": "User picked [A9-2]",
          "condition": "temp['skill-choice-ret-d54y6hk4p1'] == \"A9-2\"",
          "node": "S4-drugs-2"
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
      "id": "skill-bc13ae",
      "type": "skill-call",
      "skill": "choice",
      "name": "S4-drugs-2",
      "flow": "skills/choice-bc13ae.flow.json",
      "next": [
        {
          "caption": "User picked [A9-3]",
          "condition": "temp['skill-choice-ret-xn4hms3uqd'] == \"A9-3\"",
          "node": "choice-ff39ae-copy"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-xn4hms3uqd'] == \"toStart\"",
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
    }
  ]
}