You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal research-practice review, and I'll be asking you to walk me through a specific project in detail. You can skip anything you're not comfortable discussing. Can you start by telling me your role and how long you've been doing UX research here?

Participant: Sure. I'm a UX researcher on the productivity tools team, been here about four years. Most of my work is usability testing and discovery research feeding into our quarterly release cycles.

Interviewer: Great. I want to focus on the Smart Suggestions study. Can you walk me through how that project came about?

Participant: So Smart Suggestions is a recommendation feature — it watches what you're doing in the app and surfaces contextual actions. It came to me already pretty far along. Our VP had seen a competitor demo and decided we were building it. My brief wasn't "should we ship this," it was "help us ship it right." That framing came directly from him, almost word for word, in the kickoff.

Interviewer: How did that framing affect how you approached the study?

Participant: Honestly, it put me in a slightly defensive posture. The original plan I'd sketched was pretty lean — five moderated sessions, look at task completion and basic usability heuristics, done in a week. But hearing "this is happening regardless" made me not want to just rubber-stamp something. So before I even looked at the budget, I decided to add an unmoderated diary study on top of the moderated sessions, specifically to give people more room to surface friction over time, not just in a single session.

Interviewer: What did you know at that point that made you confident the expansion was the right call?

Participant: I had some prior data — a similar recommendation pattern we shipped in another product line got mixed reactions, so I knew these features aren't automatically loved. That backed up the diary study idea. But if I'm being fully honest, part of it was wanting to make sure the study had enough teeth that it couldn't just be waved through.

Interviewer: Did anyone push back on the expanded scope?

Participant: Research ops flagged that moderated sessions plus a diary cohort would eat most of our remaining budget. And engineering said the diary study would push the readout back a week. I considered just keeping the original five-session plan, and I also thought about pausing to renegotiate the study's purpose with the VP directly. In the end I went with the expanded version anyway.

Interviewer: Let's move to the discussion guide. What happened there?

Participant: Our PM shared a transcript from an earlier internal demo — a stakeholder said something like "this feels like it reads my mind." She sent it to me before I'd finalized the guide and said, "make sure the guide can capture moments like this." At that point my draft was pretty neutral — open prompts about task completion, satisfaction, that kind of thing.

Interviewer: What did you do with that transcript?

Participant: I went back through the guide and revised a couple of probes to more closely echo that framing — things like asking participants to describe moments where the suggestion "anticipated" what they needed. I thought I was just sharpening vague questions with a concrete example. Screener criteria were still being locked down around the same time, so there was a lot happening at once.

Interviewer: Did you consider leaving the original wording as-is?

Participant: Yeah, that was one option. Another was asking her to hold off sharing examples until after I'd locked the guide. I didn't do either. I finalized the revised version.

Interviewer: What happened once sessions started?

Participant: Two of the pilot participants used almost identical language to that transcript — "it's like it knows what I want." Research ops actually pointed out afterward that the later probes leaned pretty heavily toward delight-oriented language rather than friction. I hadn't really clocked that until she said it.

Interviewer: Let's talk about synthesis. What did the fuller pilot data look like?

Participant: Once we had ten moderated sessions plus the diary entries, it was mixed. Four sessions had real frustration — suggestions popping up mid-task, interrupting flow. Three were clearly positive. The diary entries kept circling back to timing as an issue.

Interviewer: How did you approach coding that?

Participant: This is where it got complicated. I'd given the steering committee an informal update about two weeks earlier — after just the first couple of sessions — saying early signs looked promising. So when the frustration cluster showed up, I coded it separately, as edge cases tied to atypical workflows, rather than merging it with the positive theme into one "mixed reception" finding.

Interviewer: What made atypical workflows the right explanation, in your view at the time?

Participant: Some of those users did have unusual task patterns — multi-window setups, non-standard shortcuts. So there was a real basis for it. But when a second researcher sat in on the affinity mapping and asked why we weren't just calling it "mixed reception" outright, I remember thinking that would be a harder story to tell after already saying things looked promising. That consideration was in my head when I made the call.

Interviewer: Was pausing for more sessions ever on the table?

Participant: Briefly. Engineering was also asking whether the timing complaints were serious enough to change the rollout configuration, and we didn't have time to run more sessions before the readout, so I moved forward with the edge-case framing.

Interviewer: Walk me through the final recommendation.

Participant: The synthesis doc described the feature as largely positive with a small caveat about timing. Engineering wanted one of three things: ship as-is, ship with a timing adjustment, or delay for redesign. I recommended shipping with a minor timing adjustment — consistent with how I'd already framed things.

Interviewer: How did the readout go?

Participant: The steering committee approved it, asked for a follow-up study post-launch. The VP thanked me for "confirming the direction was right all along." That phrase stuck with me a bit.

Interviewer: What information, if you'd had it earlier, might have changed any of these decisions?

Participant: If I'd had the full ten-session data set before I ever spoke informally to the committee, I might have described the early signal more cautiously. Not giving that update at all would have removed a constraint I was working around later.

Interviewer: If the product manager hadn't shared that transcript before you finalized the guide, do you think the probes would have looked different?

Participant: Probably. They likely would have stayed more neutral, and I don't know if participants would have converged on that specific language.

Interviewer: Looking back, is there anything about the process you'd reconsider?

Participant: I think I'd separate the informal updates from the analysis phase more strictly — maybe not report anything upward until coding was finalized. And I'd want a second pass on the guide before sharing any example transcripts, just to keep those inputs from bleeding into the wording. The frustration data was real; I just wonder now whether "edge case" was the cleanest read of it or the most convenient one at the time.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{IS_Biased_3}}",
  "occupational_domain": "{{Information Systems, human-computer interaction, and interaction design}}",
  "role": "{{UX Researcher}}"
}

TAXONOMY

This taxonomy distinguishes three aspects of work:

1. Task content: what the worker does.
2. Work methods: how the work is organised.
3. Tools: what machinery or technology is used.

Classify only categories supported by observable evidence. Multiple categories may be present. Select one primary content category and any defensible secondary categories. Do not force a category when evidence is insufficient.

A. TASK CONTENT — WHAT THE WORKER DOES

A1. PHYSICAL TASKS

A1.1 Strength
The worker exerts physical force or effort, handles loads, pushes, pulls, lifts, carries, restrains, or uses bodily strength as a meaningful part of the task.

A1.2 Dexterity
The worker performs precise, coordinated, or fine-grained physical movements, manipulates objects or instruments, assembles, repairs, operates controls manually, or uses hand-eye coordination as a meaningful part of the task.

A1.3 Navigation
The worker physically moves through or around an environment, routes people or objects, or maintains orientation and position in a spatial setting as a meaningful part of the task.

A2. INTELLECTUAL TASKS

A2.1 Uncodified visual or auditory information processing
The worker interprets visual, auditory, or other perceptual information that is difficult to reduce to a fully explicit rule, including recognizing patterns, anomalies, conditions, or signals.

A2.2 Literacy
The worker reads, writes, composes, edits, interprets, or communicates using written language as a meaningful part of the task.

A2.3 Numeracy
The worker calculates, quantifies, estimates, compares numerical values, interprets numerical information, or reasons about proportions, probabilities, measurements, or financial quantities.

A2.4 Information search, retrieval, gathering, and evaluation
The worker seeks, retrieves, gathers, compares, verifies, filters, or evaluates information from records, people, systems, documents, observations, or other sources.

A2.5 Conceptualisation, learning, and abstraction
The worker forms concepts, learns from experience, generalises, diagnoses, explains relationships, builds mental models, applies abstract principles, or understands a system beyond the immediate facts.

A2.6 Creativity, planning, and resolution
The worker generates, designs, or adapts solutions to a problem; develops and compares possible courses of action; plans their implementation; anticipates dependencies or consequences; or resolves a novel, non-routine situation by combining information in an original or context-sensitive way. Planning counts when it involves organising a sequence of actions, timing, resources, contingencies, or dependencies toward a goal—not merely selecting or carrying out a routine next step.

A3. SOCIAL TASKS

A3.1 Serving and attending
The worker responds to another person's immediate needs, provides a service, receives requests, attends to a customer, patient, client, user, colleague, or member of the public, or manages an interaction aimed at assistance.

A3.2 Teaching, training, and coaching
The worker explains, instructs, demonstrates, trains, develops, mentors, or coaches another person.

A3.3 Selling and influencing
The worker persuades, negotiates, recommends, markets, advocates, manages expectations, seeks agreement, or attempts to influence another person's decision or behaviour.

A3.4 Managing and coordinating
The worker allocates work, coordinates people or activities, manages dependencies, sets priorities, resolves organisational conflicts, supervises, or aligns multiple stakeholders.

A3.5 Caring
The worker provides emotional, personal, health-related, protective, or welfare-oriented support in which attention to another person's condition or well-being is central.

B. WORK METHODS — HOW THE WORK IS ORGANISED

B1. AUTONOMY

B1.1 Latitude
The worker has discretion over objectives, priorities, timing, sequence, methods, or decisions. Classify low, moderate, or high only when the interview provides evidence about the worker's discretion.

B1.2 Control and monitoring
The worker's work is supervised, measured, audited, monitored, reviewed, or constrained by another person, policy, procedure, system, target, or formal approval process. Classify low, moderate, or high based on the strength and frequency of such control.

B2. TEAMWORK

Direct collaboration with co-workers or other actors to accomplish a shared task, exchange information, coordinate actions, hand off work, or reach a joint decision. Classify low, moderate, or high based on the worker's dependence on collaboration in the described episode.

B3. ROUTINE

B3.1 Repetitiveness
The same or highly similar actions, inputs, decisions, or outputs recur frequently.

B3.2 Standardisation
The task follows prescribed procedures, scripts, checklists, templates, rules, or consistent sequences.

B3.3 Certainty and response to unforeseen situations
Certainty refers to how predictable the relevant inputs, conditions, and consequences are. Response to unforeseen situations refers to how much the worker must handle exceptions, novelty, ambiguity, disruptions, or unexpected developments.

For this dimension, report both:
- certainty: low, moderate, high, or not_observable;
- unforeseen_response_requirement: low, moderate, high, or not_observable.

C. TOOLS — MACHINERY AND TECHNOLOGY USED

C1. Non-digital machinery
Analog or mechanical devices and machinery without meaningful digital control, sensing, computing, or networked information processing.

C2. Digitally enabled machinery
Machinery or equipment using digital control, sensors, software, automation, robotics, or networked digital systems. Classify the most specific supported subtype:

C2.1 Autonomous machinery or robots
The equipment performs meaningful operations with limited direct human control after initiation.

C2.2 Non-autonomous digitally enabled machinery
The worker directly operates or controls digitally enabled physical equipment.

C2.3 Basic ICT
Routine use of computers, smartphones, email, office software, standard databases, or basic digital communication and information systems.

C2.4 Advanced ICT or programming
Programming, data analysis, modelling, system configuration, advanced computational tools, or complex software-based information processing.

C2.5 Specialised ICT
Special-purpose professional software or digital systems used for a particular occupation or work process, where the system is more specialised than ordinary office or communication software.

C2.6 Other digitally enabled tools
Digital tools that clearly matter to the work but do not fit the preceding subcategories.

CLASSIFICATION RULES

1. Classify the described episode, not the entire occupation.
2. A category must have textual evidence. Do not infer it from the role title.
3. Assign one primary task-content category: the category most central to the operational objective and decision episode.
4. Assign secondary content categories only when they are substantively involved, not merely mentioned.
5. Content categories may come from different families. For example, an interview may contain intellectual information evaluation as primary content and social influencing as secondary content.
6. Methods and tools are separate from content. Do not label a task intellectual merely because it uses a computer, or social merely because other people are mentioned.
7. Distinguish information search/evaluation from conceptualisation: the former concerns obtaining and assessing information; the latter concerns forming models, diagnoses, abstractions, or generalisations.
8. Distinguish creativity/resolution from ordinary choice: creativity requires adaptation, novel solution generation, or non-routine problem resolution.
9. Distinguish serving/attending from selling/influencing: assistance and responsiveness are not necessarily persuasion or negotiation.
10. Distinguish managing/coordinating from teamwork: teamwork is collaboration; managing/coordinating involves organising dependencies, priorities, people, or activities.
11. Do not infer strength, dexterity, navigation, or caring without direct evidence.
12. For autonomy, monitoring, teamwork, repetitiveness, standardisation, and certainty, use `not_observable` when the interview does not support a reliable level.
13. Multiple tools may be present. Record only tools that play a meaningful role in the episode.
14. If a classification is ambiguous, record the competing categories and explain the ambiguity.
15. Do not treat the participant's cognitive bias, if any, as a task category.
16. Do not use external web research. The supplied taxonomy is the authority for this annotation.

EVIDENCE REQUIREMENTS

For every assigned content category, method level, and tool category, provide:
- a short quotation or faithful text span;
- the location, such as opening, timeline, decision point, or participant turn;
- an explanation of why the evidence supports the category;
- confidence from 0 to 100.

For categories not observed but potentially plausible, do not list them as present. Place them in `not_observed_or_insufficient` only if doing so helps explain a material ambiguity.

COVERAGE STATUS

Set `coverage_status` as follows:
- `complete`: the interview contains enough evidence to classify content, methods, and tools;
- `partial`: at least one major dimension is not observable;
- `ambiguous`: competing categories cannot be resolved from the text;
- `insufficient`: the interview does not contain a sufficiently identifiable work episode.

OUTPUT SCHEMA

{
  "taxonomy_version": "Fernandez-Macias_Bisello_2021",
  "interview_id": "...",
  "occupational_domain": "...",
  "role": "...",
  "classification_confidence": 0,
  "coverage_status": "complete|partial|ambiguous|insufficient",
  "content": {
    "primary_category": {
      "family": "physical|intellectual|social|unknown",
      "subcategory": "...",
      "confidence": 0,
      "evidence": [
        {
          "location": "...",
          "quote": "...",
          "explanation": "..."
        }
      ]
    },
    "secondary_categories": [
      {
        "family": "physical|intellectual|social",
        "subcategory": "...",
        "confidence": 0,
        "evidence": [
          {
            "location": "...",
            "quote": "...",
            "explanation": "..."
          }
        ]
      }
    ],
    "all_observed_categories": [],
    "not_observed_or_insufficient": [],
    "ambiguities": []
  },
  "methods": {
    "autonomy": {
      "latitude": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      },
      "control_monitoring": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      }
    },
    "teamwork": {
      "level": "low|moderate|high|not_observable",
      "confidence": 0,
      "evidence": []
    },
    "routine": {
      "repetitiveness": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      },
      "standardisation": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      },
      "certainty": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      },
      "unforeseen_response_requirement": {
        "level": "low|moderate|high|not_observable",
        "confidence": 0,
        "evidence": []
      }
    }
  },
  "tools": [
    {
      "category": "non_digital_machinery|autonomous_machinery_or_robot|non_autonomous_digitally_enabled_machinery|basic_ict|advanced_ict_or_programming|specialised_ict|other_digitally_enabled_tool",
      "role_in_task": "...",
      "confidence": 0,
      "evidence": [
        {
          "location": "...",
          "quote": "...",
          "explanation": "..."
        }
      ]
    }
  ],
  "task_anchors": [
    {
      "location": "...",
      "task_description": "...",
      "taxonomy_labels": [],
      "confidence": 0
    }
  ],
  "decision_point_task_map": [
    {
      "decision_point": 1,
      "dominant_task_categories": [],
      "methods_relevant": [],
      "tools_relevant": [],
      "evidence": []
    }
  ],
  "classification_quality": {
    "occupation_inference_risk": "low|moderate|high",
    "stereotype_risk": "low|moderate|high",
    "taxonomy_ambiguity": "low|moderate|high",
    "missing_evidence": [],
    "manual_review_recommended": false
  },
  "coverage_flags": {
    "physical_content_observed": false,
    "intellectual_content_observed": false,
    "social_content_observed": false,
    "methods_observed": false,
    "tools_observed": false,
    "all_major_dimensions_observable": false
  },
  "recommended_dataset_action": "retain|retain_with_low_confidence|sample_more|manual_review|exclude"
}

FINAL CHECK

Before returning JSON, verify that:
- Every present category has textual evidence.
- The primary category is central to the episode, not merely the most frequently mentioned word.
- Secondary categories are substantively involved.
- Method and tool labels are supported independently from content labels.
- `not_observable` is used where appropriate.
- Confidence reflects evidence quality, not certainty from the occupation or role.
- No cognitive-bias labels appear as task categories.
- No external sources or unstated occupational assumptions were used.
- The result is valid JSON and contains no prose outside the JSON object.
