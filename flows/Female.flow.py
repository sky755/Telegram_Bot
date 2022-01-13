{
  "version": "0.0.1",
  "catchAll": {},
  "startNode": "choice-Female1",
  "description": "",
  "nodes": [
    {
      "id": "9afa89ec8b",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-participant_1",
      "flow": "skills/choice-e4adb7.flow.json",
      "next": [
        {
          "caption": "User picked [84]",
          "condition": "temp['skill-choice-ret-xxmk751qsc'] == \"84\"",
          "node": "choice-participant_2"
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
      "id": "bedbf78ba8",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-participant_2",
      "flow": "skills/choice-354e6b.flow.json",
      "next": [
        {
          "caption": "User picked [84]",
          "condition": "temp['skill-choice-ret-wvexpnacxb'] == \"84\"",
          "node": "node-la_strada_1-02"
        },
        {
          "caption": "User picked [85]",
          "condition": "temp['skill-choice-ret-wvexpnacxb'] == \"85\"",
          "node": "choice-suicide_1"
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
      "id": "653dbf5f80",
      "name": "node-la_strada_1",
      "next": [
        {
          "condition": "true",
          "node": "main.flow.json#secondStart"
        }
      ],
      "onEnter": [
        "say #!builtin_text-CzDk7X"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "071d90fcd2",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-suicide_1",
      "flow": "skills/choice-2829e6.flow.json",
      "next": [
        {
          "caption": "User picked [86]",
          "condition": "temp['skill-choice-ret-56g0a9eykt'] == \"86\"",
          "node": "choice-suicide_2"
        },
        {
          "caption": "User picked [87]",
          "condition": "temp['skill-choice-ret-56g0a9eykt'] == \"87\"",
          "node": "choice-participant_3"
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "5b43d0ae64",
      "name": "node-life_line",
      "next": [
        {
          "condition": "true",
          "node": "main.flow.json#secondStart"
        }
      ],
      "onEnter": [
        "say #!builtin_text-t9M7BH"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "3a8b09a0be",
      "name": "node-open_doors_1",
      "next": [
        {
          "condition": "true",
          "node": "main.flow.json#secondStart"
        }
      ],
      "onEnter": [
        "say #!builtin_text-QHcr0i"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "ca5931dbca",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-participant_3",
      "flow": "skills/choice-42415d.flow.json",
      "next": [
        {
          "caption": "User picked [811]",
          "condition": "temp['skill-choice-ret-g4fa3t9gbm'] == \"811\"",
          "node": "choice-psy_1"
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "7f61a9434b",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-psy_1",
      "flow": "skills/choice-22534a.flow.json",
      "next": [
        {
          "caption": "User picked [812]",
          "condition": "temp['skill-choice-ret-4ykhf2iuiq'] == \"812\"",
          "node": "node-open_doors_1-02"
        },
        {
          "caption": "User picked [813]",
          "condition": "temp['skill-choice-ret-4ykhf2iuiq'] == \"813\"",
          "node": "choice-rest"
        },
        {
          "caption": "User picked [814]",
          "condition": "temp['skill-choice-ret-4ykhf2iuiq'] == \"814\"",
          "node": "choice-test"
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "a03cf5584f",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-test",
      "flow": "skills/choice-7e3f82.flow.json",
      "next": [
        {
          "caption": "User picked [815]",
          "condition": "temp['skill-choice-ret-4zv6a8b6nl'] == \"815\"",
          "node": "Selftest_Female.flow.json"
        },
        {
          "caption": "User picked [816]",
          "condition": "temp['skill-choice-ret-4zv6a8b6nl'] == \"816\"",
          "node": "choice-rest"
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
      "id": "d32acf9ede",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-rest",
      "flow": "skills/choice-f6e64f.flow.json",
      "next": [
        {
          "caption": "User picked [toLawyer]",
          "condition": "temp['skill-choice-ret-c6j8a7nd2t'] == \"toLawyer\"",
          "node": "Lawyer.flow.json"
        },
        {
          "caption": "User picked [contact...]",
          "condition": "temp['skill-choice-ret-c6j8a7nd2t'] == \"contactJurSotnya\"",
          "node": "choice-feedback-2"
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
      "id": "4097376a8e",
      "name": "node-sotnia",
      "next": [
        {
          "condition": "true",
          "node": ""
        }
      ],
      "onEnter": [
        "say #!builtin_text-KMXYT6"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "a8904e84ab",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-fidback",
      "flow": "skills/choice-4a8edb.flow.json",
      "next": [
        {
          "caption": "User picked [feedback]",
          "condition": "temp['skill-choice-ret-vb6aolw264'] == \"feedback\"",
          "node": "main.flow.json#feedback"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-vb6aolw264'] == \"toStart\"",
          "node": "main.flow.json#secondStart"
        }
      ],
      "onEnter": null,
      "onReceive": null
    },
    {
      "id": "34e8737073",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-witness_1",
      "flow": "skills/choice-5bc467.flow.json",
      "next": [
        {
          "caption": "User picked [821]",
          "condition": "temp['skill-choice-ret-40l23rk2ta'] == \"821\"",
          "node": "choice-witness_2"
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
      "id": "4f1a842262",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-witness_2",
      "flow": "skills/choice-a8bf61.flow.json",
      "next": [
        {
          "caption": "User picked [822]",
          "condition": "temp['skill-choice-ret-zq0lwvqinw'] == \"822\"",
          "node": "choice-witness_3-1"
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
      "id": "18da37549b",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-witness_4",
      "flow": "skills/choice-868b4f.flow.json",
      "next": [
        {
          "caption": "User picked [825]",
          "condition": "temp['skill-choice-ret-7h2wk4hex6'] == \"825\"",
          "node": "main.flow.json#secondStart"
        },
        {
          "caption": "User picked [feedback]",
          "condition": "temp['skill-choice-ret-7h2wk4hex6'] == \"feedback\"",
          "node": "main.flow.json#feedbackNode"
        },
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-7h2wk4hex6'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
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
      "id": "skill-f35e3f",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-suicide_2",
      "flow": "skills/choice-f35e3f.flow.json",
      "next": [
        {
          "caption": "User picked [88]",
          "condition": "temp['skill-choice-ret-lxjriiqurb'] == \"88\"",
          "node": "node-life_line-2"
        },
        {
          "caption": "User picked [89]",
          "condition": "temp['skill-choice-ret-lxjriiqurb'] == \"89\"",
          "node": "node-open_doors_1-02"
        },
        {
          "caption": "User picked [810]",
          "condition": "temp['skill-choice-ret-lxjriiqurb'] == \"810\"",
          "node": "node-open_doors_1-02"
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
      "id": "skill-007a8d",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-Female1",
      "flow": "skills/choice-007a8d.flow.json",
      "next": [
        {
          "caption": "User picked [81]",
          "condition": "temp['skill-choice-ret-5g6c0yrgka'] == \"81\"",
          "node": "choice-participant_1"
        },
        {
          "caption": "User picked [82]",
          "condition": "temp['skill-choice-ret-5g6c0yrgka'] == \"82\"",
          "node": "choice-witness_1"
        },
        {
          "caption": "User picked [aboutPr...]",
          "condition": "temp['skill-choice-ret-5g6c0yrgka'] == \"aboutProblem\"",
          "node": "General.flow.json"
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
      "id": "skill-95615b",
      "type": "skill-call",
      "skill": "choice",
      "name": "node-la_strada_1-02",
      "flow": "skills/choice-95615b.flow.json",
      "next": [
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-qy4vxlspox'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-qy4vxlspox'] == \"toStart\"",
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
      "id": "skill-aadf57",
      "type": "skill-call",
      "skill": "choice",
      "name": "node-life_line-2",
      "flow": "skills/choice-aadf57.flow.json",
      "next": [
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-4tjjjro3di'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-4tjjjro3di'] == \"toStart\"",
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
      "id": "skill-be33b3",
      "type": "skill-call",
      "skill": "choice",
      "name": "node-open_doors_1-02",
      "flow": "skills/choice-be33b3.flow.json",
      "next": [
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-txwt8rcidu'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-txwt8rcidu'] == \"toStart\"",
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
      "id": "skill-0c3c21",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-feedback-2",
      "flow": "skills/choice-0c3c21.flow.json",
      "next": [
        {
          "caption": "User picked [feedback]",
          "condition": "temp['skill-choice-ret-452idm2wc5'] == \"feedback\"",
          "node": "main.flow.json#feedbackNode"
        },
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-452idm2wc5'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-452idm2wc5'] == \"toStart\"",
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
      "id": "skill-f848a2",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-witness_3-1",
      "flow": "skills/choice-f848a2.flow.json",
      "next": [
        {
          "caption": "User picked [823]",
          "condition": "temp['skill-choice-ret-7y25ti3vdu'] == \"823\"",
          "node": "choice-2fd0cf"
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
      "id": "skill-cc3625",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-cc3625",
      "flow": "skills/choice-cc3625.flow.json",
      "next": [
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-pb2zssjv3j'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-pb2zssjv3j'] == \"toStart\"",
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
      "id": "skill-2fd0cf",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-2fd0cf",
      "flow": "skills/choice-2fd0cf.flow.json",
      "next": [
        {
          "caption": "User picked [823-1]",
          "condition": "temp['skill-choice-ret-2x4fmhu4gm'] == \"823-1\"",
          "node": "choice-witness_4"
        },
        {
          "caption": "User picked [823-2]",
          "condition": "temp['skill-choice-ret-2x4fmhu4gm'] == \"823-2\"",
          "node": "choice-cc3625"
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