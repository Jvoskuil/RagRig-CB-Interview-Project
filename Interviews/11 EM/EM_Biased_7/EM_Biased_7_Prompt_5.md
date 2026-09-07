You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this conversation being recorded and used for after-action training purposes, not for any personnel evaluation.

Participant: Yeah, that's fine. I've done these debriefs before.

Interviewer: Can you tell me your role and what you were responsible for when this incident started?

Participant: I'm the Situation Unit Analyst for the county EOC. My job during an activation is to build and maintain the Common Operating Picture — pulling in field reports, sensor data, weather, whatever's coming in — and turning that into something the Branch Directors and the EOC Director can actually make calls from. That night I was covering both the flood side and keeping an eye on the fire branch, since Ridge Fire was still active and eating into our smoke-camera and aerial coverage.

Interviewer: Walk me through how the incident began.

Participant: It started with a notice from the Twin Forks Reservoir Authority around 9 PM. They said they were doing a controlled precautionary release ahead of the storm cell that was coming in — basically getting ahead of it so the reservoir wouldn't be over capacity when the rain hit. Our downstream gauges at that point were showing a gradual rise, nothing dramatic. The duty hydrologist was tied up on another call and wasn't going to be free for at least ninety minutes, so I didn't have anyone to sanity-check the numbers against. Our flood Branch Director, who's been doing this about twenty years, looked at the same notice and said this was a routine pattern, that he'd seen the reservoir do exactly this kind of release two or three times before.

Interviewer: What did you decide to do with that information?

Participant: I recommended we go with a monitor-and-prepare advisory rather than jump straight to a warning for Sector 7. The operator's language was pretty clearly framed as precautionary — they used the word "controlled" a couple times — and combined with the Director's read that this looked routine, it felt like the proportionate response. I remember thinking, if this were really an emergency release they wouldn't be calling it precautionary.

Interviewer: Did you consider verifying that independently before finalizing the advisory?

Participant: I thought about it, but with the hydrologist unavailable and the Director being pretty confident, it seemed like it would just slow things down without adding much. He's the one who signs off on tier decisions normally, and I trusted his read given how long he's been doing this.

Interviewer: What happened next?

Participant: About ninety minutes later the gauges spiked hard — much faster than the operator's language had implied. The release turned out to be a lot bigger than "controlled precautionary" suggested. That's when things started moving fast.

Interviewer: Let's talk about the resource request that followed. What was happening at that point?

Participant: Our field liaison started getting scattered water-rescue calls, but only in two sub-neighborhoods — small numbers, really consistent with a standard tier-1 response. At the same time I was hearing fire dispatch chatter using radio codes that sounded almost identical to what we used during the 2018 flash flood two counties over, the one with multiple fatalities. I'd helped coordinate the tier-3 mobilization on that one.

Interviewer: How did that connection affect your recommendation?

Participant: Honestly, it hit me pretty hard. I remember thinking, this feels like 2018 again, and I didn't want to be caught understaffed like we almost were back then. So I recommended a full tier-3 mobilization — extra swift-water teams, extra staging — even though the actual call volume we had in front of us was only tier-1 level.

Interviewer: Did the current data support tier-3 on its own?

Participant: Not really, no. If you just looked at the confirmed calls, tier-1 would've covered it. But that memory was loud in my head.

Interviewer: What ended up happening with those resources?

Participant: The rescue calls plateaued at basically tier-1 volume. So we had tier-3 assets sitting partly idle for a few hours, which the fire branch wasn't thrilled about since they needed some of that same equipment.

Interviewer: Let's move to the evacuation zone decision. What information did you have at that stage?

Participant: This was the rough part. Six of our eight stream gauges were down — the repeater got knocked out by Ridge Fire smoke interference — so I only had two gauges reporting, and both were showing a sharp rise over about twenty minutes. Around the same time, videos of flooding at one intersection started circulating on social media and a regional news account picked it up and ran with it. That clip kept popping up everywhere — I must've seen it shared four or five times through different channels — and after a while it started feeling like the flooding was happening all over, even though it was really just the one intersection.

Interviewer: How did you put that together into a recommendation?

Participant: I built out a flood-extent map using the two gauges plus that footage, and honestly, it all fit together really cleanly — the trend line, the video, the timing. It told a clear, coherent story, and I felt confident recommending we expand the evacuation to the whole multi-sector watershed area rather than just the sub-zones next to those two gauges.

Interviewer: Did you weigh how much of the watershed those two gauges actually represented?

Participant: I mean, two out of eight isn't the full picture, but they were both moving in the same direction, so I took that as a strong enough signal for the whole area. Getting people out ahead of a flood is better than being late, so I leaned toward the wider expansion.

Interviewer: What came out of that afterward?

Participant: Once the backup gauges came back online later that night, it turned out two of the newly evacuated sub-zones never actually exceeded minor flood stage. So the expansion was broader than what materialized, though obviously nobody could've known that for certain in the moment.

Interviewer: Let's go to the hot-wash review. What was discussed there?

Participant: We went back over the original advisory decision — the one from the start of the night — now that we knew how bad it actually got. Reading the operator's notice again, with everything we now know, it seemed like the signs were pretty clearly there. The scale of what happened felt like it should have been obvious from that notice alone.

Interviewer: When you say "obvious," obvious based on what was known that night, or knowing how it turned out?

Participant: Looking back at it now, it just reads differently. Knowing what happened after, the wording in that notice looks like it was underselling things pretty clearly.

Interviewer: If the operator's notice had used different language that night — less "controlled," more urgent — do you think your initial recommendation would have changed?

Participant: Probably, yeah. If it had said something like "emergency release" instead of "precautionary," I think I'd have pushed harder for a warning tier instead of an advisory, regardless of what the Director's initial read was.

Interviewer: And if all eight gauges had stayed online through the evacuation decision, would that have changed things?

Participant: I'd like to think I'd have waited for a fuller picture instead of leaning as hard on those two data points and the footage. With full coverage I probably wouldn't have needed the video to fill in the gaps at all.

Interviewer: Looking back across the whole night, how do you separate what you actually knew in the moment from what became clear afterward?

Participant: It's harder than it sounds. In the moment you're working with partial data and you're making the best call you can with what's in front of you. It's only once you have the full outcome that certain things start looking like they should have been flagged earlier — but I try to remind myself that clarity came from hindsight, not from anything I necessarily missed in real time.

Interviewer: That's a good place to stop. Thanks for walking through this in detail.

Participant: Sure, happy to help however this gets used.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{EM_Biased_7}}",
  "occupational_domain": "{{Emergency management and Civil Protection}}",
  "role": "{{Emergency Operations Center (EOC) Situation Unit Analyst}}"
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
