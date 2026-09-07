You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm—this is a confidential debrief about how you handled a specific stretch of the trial, not an audit. I'll ask you to walk me through what happened and how you made a few key calls. Sound okay?

Participant: Sure, that's fine. I've talked through the quarter with the monitor already, so I don't mind going over it again.

Interviewer: Great. Can you give me a sense of your role and what this trial looked like during that period?

Participant: I'm the lead coordinator on a Phase III oncology study at our site, one of about fourteen sites nationally. I was also splitting time across two other trials, so hours were tight. We were roughly three weeks from the end of a quarterly enrollment window and about four patients behind target, which matters because the sponsor ties site continuation funding to pace.

Interviewer: What was the main thing you were trying to protect during that stretch?

Participant: Mainly staying compliant while not losing the site's enrollment allocation. Those two goals don't always pull in the same direction.

Interviewer: Walk me through the incident from the start.

Participant: It kicked off with a screening visit. We'd just gotten an amended protocol that changed the organ-function language to something looser—"adequate organ function"—without giving us a lab cutoff table like the old version had. A patient came in who fit almost everything except that his labs were borderline under the old thresholds. Our PI was traveling and only reachable by short messages, not a real conversation. Given where we stood on enrollment, I read the new wording as intentionally more permissive and enrolled him without flagging the ambiguity to anyone first. A few weeks later the sponsor sent a clarifying memo with explicit cutoffs, and his labs didn't clearly meet them. The monitor flagged it for query at the next visit.

Around the same time, I was still trying to get a referral pipeline going with a partner clinic—training their staff, building scheduling templates, that kind of thing. I'd put in something like forty hours on it, but after six weeks it had only produced one enrollee. There was an untried option—reviewing our own oncology charts for candidates—that a colleague thought could move faster. I kept most of my hours on the partner-clinic pipeline anyway. Part of it was that I'd already built the infrastructure and didn't want to abandon it prematurely. Separately, a coordinator newsletter came out saying a couple of peer sites were ahead of pace using a similar clinic-referral approach, and that made me more comfortable sticking with it rather than testing the chart-review idea.

Then we had an adverse event: a newly enrolled patient developed a grade 2 rash and some fatigue about nine days after his first infusion. It looked a lot like the classic hypersensitivity vignette in the investigator brochure. He'd also just finished an antibiotic course and has a history of seasonal allergies, both in his chart already. The day before I drafted my assessment, a peer-site coordinator had described an almost identical rash on a call, attributed to the study drug. My draft leaned toward drug-related, mostly because the case matched the brochure picture so well, and that recent peer case reinforced it for me.

Last piece: the eligibility ambiguity resurfaced as a monitor query, and I had to summarize it in writing for the sponsor's trial manager. The PI floated two ways to describe it—"minor administrative eligibility clarification" or "protocol deviation requiring corrective action." Both were defensible given how the language had been written. I went with the milder version, partly because it came up first and just sounded less serious.

Interviewer: Let's slow down and go through each of those in order. Starting with the screening decision—what did you actually have in front of you right then?

Participant: The new protocol text, the patient's lab values, and the fact that our PI wasn't reachable for a real discussion. I also had the enrollment count in the back of my mind.

Interviewer: What alternatives did you consider?

Participant: I could have held the screening and pushed the ambiguity up to the PI or the sponsor's medical monitor before deciding anything, or just declined him outright until the wording was clarified. I didn't do either—I made the call myself and moved forward.

Interviewer: What made you settle on your own interpretation instead of escalating?

Participant: Honestly, escalating would have meant losing him as a candidate for that window, and we needed the number. I told myself the new language was probably meant to be more flexible, so I read it that way and enrolled him.

Interviewer: Moving to the referral pathway—what alternatives did you weigh?

Participant: Keep pushing the partner-clinic pipeline, redirect hours to chart review, or split time between both. I stayed with the partner-clinic route.

Interviewer: What tipped the balance?

Participant: Two things, really. I'd already sunk forty hours into setting it up, so switching felt like throwing that away. And then seeing that other sites were reportedly doing well with a similar setup made it easier to justify staying the course rather than testing something untried.

Interviewer: On the adverse event—how did you arrive at your causality read?

Participant: The presentation matched the brochure's example almost point for point, so that was my anchor. And having just heard about that near-identical case on the peer call the day before made it feel confirmed, so I leaned toward drug-related in my draft.

Interviewer: Did the antibiotic course or allergy history factor into that draft?

Participant: They were in the chart, but I didn't weigh them heavily going in—I mentioned them but treated the pattern match and the peer case as the stronger signal.

Interviewer: And the sponsor note—how did you land on that specific wording?

Participant: The PI mentioned the "minor clarification" phrasing first when we talked it through, and it just felt like the lower-friction option, so that's what I used.

Interviewer: Was there anything at that point pulling you toward the other description?

Participant: Not really pulling me—I knew "protocol deviation" was equally accurate, but by the time I sat down to write the note, the milder framing was already the one in my head.

Interviewer: How much uncertainty did you feel at each of these moments?

Participant: Screening felt rushed more than uncertain. The pathway decision felt more like frustration than doubt. The AE read, I was fairly confident at the time, less so after the allergy testing came back. The note-writing, I didn't feel uncertain at all in the moment, which looking back maybe I should have.

Interviewer: If the sponsor's clarifying memo had landed a day before that screening visit, would things have gone differently?

Participant: Probably—I'd have had the actual cutoffs and wouldn't have needed to guess.

Interviewer: And if you hadn't seen the peer newsletter or heard about that rash case beforehand?

Participant: The pathway decision might have gone to chart review sooner. The AE draft, I'm less sure—the pattern match alone might have gotten me there anyway, just maybe with less confidence.

Interviewer: If the PI had suggested "protocol deviation" first instead of the milder phrase?

Participant: I think I'd have gone with that one instead, honestly.

Interviewer: Looking back, is there a point where you'd want clearer guidance before deciding?

Participant: The eligibility language, definitely—a real threshold table instead of open wording would have saved me from guessing under pressure.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{HC_Biased_6}}",
  "occupational_domain": "{{Healthcare}}",
  "role": "{{Clinical Research Coordinator}}"
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
