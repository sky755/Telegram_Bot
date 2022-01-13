{
  "version": "0.0.1",
  "catchAll": {},
  "startNode": "choice-law_1",
  "description": "",
  "nodes": [
    {
      "id": "skill-d497a3",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-law_1",
      "flow": "skills/choice-d497a3.flow.json",
      "next": [
        {
          "caption": "User picked [70]",
          "condition": "temp['skill-choice-ret-sumqrhm45v'] == \"70\"",
          "node": "choice-law_2"
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
      "id": "skill-9c94bf",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-law_2",
      "flow": "skills/choice-9c94bf.flow.json",
      "next": [
        {
          "caption": "User picked [71]",
          "condition": "temp['skill-choice-ret-he49t0kppf'] == \"71\"",
          "node": "choice-law_3"
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
      "id": "skill-2a8ae0",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-law_3",
      "flow": "skills/choice-2a8ae0.flow.json",
      "next": [
        {
          "caption": "User picked [72]",
          "condition": "temp['skill-choice-ret-s92w8ne9s9'] == \"72\"",
          "node": "choice-law_4"
        },
        {
          "caption": "User picked [73]",
          "condition": "temp['skill-choice-ret-s92w8ne9s9'] == \"73\"",
          "node": "choice-ab3364"
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
      "id": "skill-8f9c9d",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-law_4",
      "flow": "skills/choice-8f9c9d.flow.json",
      "next": [
        {
          "caption": "User picked [74]",
          "condition": "temp['skill-choice-ret-ofl9xrdsmm'] == \"74\"",
          "node": "choice-law_5"
        },
        {
          "caption": "User picked [75]",
          "condition": "temp['skill-choice-ret-ofl9xrdsmm'] == \"75\"",
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
      "id": "51878b2f6d",
      "name": "node-sotnia",
      "next": [
        {
          "condition": "true",
          "node": "main.flow.json#secondStart"
        }
      ],
      "onEnter": [
        "say #!builtin_text-KMXYT6"
      ],
      "onReceive": null,
      "type": "standard"
    },
    {
      "id": "skill-4533c2",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-law_5",
      "flow": "skills/choice-4533c2.flow.json",
      "next": [
        {
          "caption": "User picked [76]",
          "condition": "temp['skill-choice-ret-r0y8cd9edr'] == \"76\"",
          "node": "choice-law_5-1"
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
      "id": "skill-cf9ba3",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-law_6",
      "flow": "skills/choice-cf9ba3.flow.json",
      "next": [
        {
          "caption": "User picked [77]",
          "condition": "temp['skill-choice-ret-2xk8y8suyo'] == \"77\"",
          "node": "choice-law_7"
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
      "id": "skill-e53055",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-law_7",
      "flow": "skills/choice-e53055.flow.json",
      "next": [
        {
          "caption": "User picked [78]",
          "condition": "temp['skill-choice-ret-3m54mgdxsp'] == \"78\"",
          "node": "choice-law_7-2"
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
      "id": "skill-05b897",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-law_8",
      "flow": "skills/choice-05b897.flow.json",
      "next": [
        {
          "caption": "User picked [79]",
          "condition": "temp['skill-choice-ret-2w7wtal1te'] == \"79\"",
          "node": "choice-law_9"
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
      "id": "skill-784426",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-law_9",
      "flow": "skills/choice-784426.flow.json",
      "next": [
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-jhj8l1a9wg'] == \"toStart\"",
          "node": "choice-a765a1"
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
      "id": "skill-a765a1",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-a765a1",
      "flow": "skills/choice-a765a1.flow.json",
      "next": [
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-k8xm34ld9p'] == \"toStart\"",
          "node": "main.flow.json#secondStart"
        },
        {
          "caption": "User picked [feedbac...]",
          "condition": "temp['skill-choice-ret-k8xm34ld9p'] == \"feedbackNode\"",
          "node": "main.flow.json#feedbackNode"
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
      "id": "skill-ab3364",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-ab3364",
      "flow": "skills/choice-ab3364.flow.json",
      "next": [
        {
          "caption": "User picked [feedback]",
          "condition": "temp['skill-choice-ret-3bmpl365zn'] == \"feedback\"",
          "node": "main.flow.json#feedbackNode"
        },
        {
          "caption": "User picked [contacts]",
          "condition": "temp['skill-choice-ret-3bmpl365zn'] == \"contacts\"",
          "node": "main.flow.json#choice-yes"
        },
        {
          "caption": "User picked [toStart]",
          "condition": "temp['skill-choice-ret-3bmpl365zn'] == \"toStart\"",
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
      "id": "skill-fce1c8",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-law_7-2",
      "flow": "skills/choice-fce1c8.flow.json",
      "next": [
        {
          "caption": "User picked [78-1]",
          "condition": "temp['skill-choice-ret-i27gyvtve0'] == \"78-1\"",
          "node": "choice-law_8"
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
      "id": "skill-a71f39",
      "type": "skill-call",
      "skill": "choice",
      "name": "choice-law_5-1",
      "flow": "skills/choice-a71f39.flow.json",
      "next": [
        {
          "caption": "User picked [76-1]",
          "condition": "temp['skill-choice-ret-309z38gk1u'] == \"76-1\"",
          "node": "choice-law_6"
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