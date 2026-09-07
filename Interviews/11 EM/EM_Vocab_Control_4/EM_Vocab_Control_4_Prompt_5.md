You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. This is a routine debrief on your reasoning process during the Copper Creek event, not a performance review — nothing here affects your evaluation. Okay to proceed on that basis?

Participant: Sure, that's fine.

Interviewer: Can you start by describing your role on the desk that shift?

Participant: I'm the meteorological hazard forecaster for the ESF-2/ESF-5 desk at the state EOC. I translate NWS and SPC guidance into activation-level recommendations, warning products, and messaging calls for the counties in our basin. I coordinate with the WFO, the county EMs, and on multi-state events, with neighboring forecast desks.

Interviewer: Walk me through this particular incident from the start.

Participant: It started overnight with SPC flagging a marginal severe risk for the basin, low confidence, mostly because guidance was still sparse. By the 06Z cycle we only had four members of the convection-allowing ensemble finished — the rest were still running. Three of those four showed the cluster intensifying fast over the basin within about three hours. Given that we only had four members in, I didn't want to treat that as the full picture, so instead of a basin-wide upgrade I issued a limited advisory just for the highest-confidence sub-area and flagged that the guidance sample was still thin. A couple hours later, radar showed a hook-shaped reflectivity signature that looked a lot like an event I'd forecasted successfully a couple seasons back — similar CAPE and shear profile. It was tempting to just run with that track, but the motion vector still supported two plausible paths, so I got the WFO desk on the line before committing to anything. They confirmed the dual-track concern was legitimate and we kept both options open a while longer. Then flash flood guidance started climbing in two of our sub-watersheds, and I wanted to escalate the EOC activation level and get swift-water teams moving, since they need about 45 minutes lead time. The regional director called and asked us to hold, citing a pending downstream reservoir-release update that could shift the hydrologic picture within the hour. On the interstate coordination call after that, three of four neighboring jurisdictions said they were holding, citing rainfall totals below their local thresholds. Our own numbers were still worsening, so I issued a locally scaled escalation while keeping shared language for the parts of the basin that matched their situation. Flooding started in one of our towns about fifty minutes after that call ended.

Interviewer: Let's reconstruct the sequence more precisely. What did you have at each stage, and what were you still waiting on?

Participant: At the start, just the partial ensemble and the SPC discussion — no radar-observed rotation or guidance exceedance yet. Then the radar signature came in as a qualitative cue layered on the model data. After that, the guidance numbers gave us the first hard hydrologic evidence. And the coordination call added a comparison point — what the specific data behind each jurisdiction's position looked like, not just their stance.

Interviewer: Let's go through the four moments where you had to make a call. First: the early guidance decision. What alternatives did you weigh?

Participant: Upgrade basin-wide, hold entirely for the 09Z cycle, or scale it — advisory for the sub-area with the strongest signal while noting the limited sample. I went with the scaled option.

Interviewer: What tipped it?

Participant: Honestly, the fact that it was only four members mattered a lot. Three agreeing is worth something, but with that few total runs in, I didn't think it justified a full upgrade. Splitting the difference let us respond to the signal without overstating how solid it was.

Interviewer: Did the SPC's own confidence language factor in?

Participant: Yes — they were explicit that confidence was low given how sparse guidance still was, and that lined up with my instinct not to lean too hard on just four members.

Interviewer: Second decision — the radar signature and the track call. What made you loop in the WFO before settling on one track?

Participant: The signature really did remind me of that prior event, and part of me wanted to just call it. But recognizing a shape isn't the same as confirming a track, and the motion vector still supported two paths. I didn't have hard evidence to rule either one out, so getting an independent read felt like the responsible move before committing publicly.

Interviewer: How confident were you in the moment?

Participant: Moderately — maybe six or seven out of ten on the pattern match itself, but I held the actual forecast at "two plausible tracks" until the WFO's read came back and we converged.

Interviewer: Third decision point — the activation-level call after the director's instruction. What was your read going in?

Participant: Guidance exceedance was climbing, and my inclination was to escalate and get swift-water teams moving given the lead time. When the director called for a hold, I asked him what was driving it rather than just taking the instruction at face value.

Interviewer: What did he tell you?

Participant: He said there was a downstream reservoir-release update expected within the hour that could change the exceedance timing. That's a real variable I hadn't factored in yet, so I agreed to hold — but only with a defined recheck time, given how tight the swift-water lead time already was.

Interviewer: Was there a technical case for holding, independent of his instruction?

Participant: Once he explained the reservoir piece, yes — that's genuinely relevant hydrology I didn't have. It wasn't just deferring to him; it was incorporating information I was missing.

Interviewer: Fourth decision — the coordination call and public messaging.

Participant: My numbers favored escalating messaging and issuing a WEA locally. Three of four neighboring desks said they were holding, but they backed that up with their own rainfall totals, which were genuinely lower than ours. So I compared our specific numbers against theirs rather than just matching their stance, concluded our situation was different, and issued a scaled local escalation while keeping shared language for the overlapping parts of the basin.

Interviewer: What happened afterward?

Participant: Flooding started in one of our towns about fifty minutes later. The neighboring jurisdictions' hold positions turned out to be consistent with their own lower totals, so their call made sense for their situation.

Interviewer: If the fuller ensemble had been available from the start, would the early decision have gone differently?

Participant: Maybe — if more members had agreed, I might have gone straight to a basin-wide upgrade instead of scaling it. The small sample was really the reason I hedged.

Interviewer: If the director's call hadn't included the reservoir rationale, what would you have done?

Participant: I'd have pushed back harder or escalated anyway. The hold only made sense to me once I understood what new variable was behind it.

Interviewer: Looking back, with the same information available at each point, would you change anything?

Participant: Not fundamentally. I might have pinged the WFO even earlier on the track call, just to shorten how long we sat with two options. But splitting the difference on the early advisory and separating our data from the neighboring jurisdictions' data both felt like the right calls given what we actually had.

Interviewer: That's really helpful. Thanks for walking through it in this much detail.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{EM_Vocab_Control_4}}",
  "occupational_domain": "{{Emergency management and Civil Protection}}",
  "role": "{{Meteorological Hazard Forecaster (Emergency Support Function)}}"
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
