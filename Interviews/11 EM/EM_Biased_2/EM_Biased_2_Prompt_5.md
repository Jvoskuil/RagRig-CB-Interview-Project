You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{**Interviewer:** Thanks for making time for this. Just to confirm — this is a voluntary debrief for our after-action learning file, not a performance review. I'll ask you to walk me through the Riverside facility fire from your role as PIO, and I may pause to dig into specific moments. Sound okay?

**Participant:** Sure, happy to do it. It's still pretty fresh — that was a long shift.

**Interviewer:** Good. Before we get into detail, can you give me a quick overview of the incident and what you were trying to accomplish?

**Participant:** Basically, we had a fire break out at the solvent recycling facility on the east side, maybe three hundred meters from a residential block and not far from the elementary school. My job was to get accurate public messaging out fast — warn people if they needed to shelter, keep the media from running ahead of us, and coordinate with the school and health officer so nobody's getting conflicting instructions. Objective was simple to state, hard to execute: protect people without causing panic, and don't say anything we'd have to walk back.

**Interviewer:** Walk me through how it started.

**Participant:** Dispatch got the call a little after 1pm. Within ten minutes we had confirmation of a working fire, heavy smoke, and wind carrying it toward the neighborhood. 911 was lighting up with people reporting a chemical smell. Problem was, we didn't have the facility's chemical manifest yet — that takes time to pull and verify with the fire marshal. So I'm standing in the JIC with a wind direction, an odor complaint pattern, and no confirmed hazard identity. I recommended we go out with a precautionary shelter-in-place advisory rather than wait, because closing windows and staying put costs us very little if it turns out to be nothing, but waiting costs a lot if it's not nothing.

**Interviewer:** What information came in after that first call?

**Participant:** Within about forty minutes the manifest came back — mostly low-toxicity solvents, not the worst-case chemical we'd feared. Wind also shifted slightly, pushing the plume a bit more over open ground. So the initial risk picture actually eased some, which was a relief, but by then we'd already committed to the advisory, which I think was still the right call given what we knew at the time.

**Interviewer:** Let's reconstruct the next couple hours. What happened after that initial advisory went out?

**Participant:** We had about a ninety-minute window where the air monitoring wasn't fully stood up yet, so we were operating a little blind on the contaminant side. Meanwhile the Incident Commander is focused on suppression, the health officer wants to weigh in on any health guidance, and our elected officials are asking me for updates every twenty minutes. Then social media started moving faster than we could — somebody posted early speculation that it was a "chemical explosion," which wasn't accurate, and we had to spend cycles knocking that down instead of just informing.

**Interviewer:** That's around when you had to choose how to actually push out that first advisory — which system to use. Tell me about that decision.

**Participant:** Right, so our comms team had two options. There's the reverse-911 system, which got upgraded last year — it can geotarget down to the block level, so you're only alerting people actually in the plume path. Then there's our Community Alert Network, the CAN system, which is the one we've used in every drill and every real incident for at least five years. I know that script cold, I know how the spokesperson delivery works with it, I know what it sounds like when it goes out.

**Interviewer:** And you went with CAN.

**Participant:** I did. It's just the one that's always worked for us. Somebody on the comms desk mentioned reverse-911 had a couple of successful tests on the books, but I didn't pull the test log or ask the on-call tech what the fallback would be if it hiccupped mid-broadcast — I just had this sense that a system I hadn't personally run live could have bugs, and that was enough to steer me back to what I already knew. I was aware CAN would blast countywide instead of just the plume area, which isn't really a great fit for a localized smoke event, but that didn't weigh very heavily against just going with the familiar option.

**Interviewer:** Did you weigh the two options against each other on any specific criteria — reach accuracy, message length, anything like that?

**Participant:** Not in a formal sense, no. It was more that CAN is the one I trust because I've been using it for years. In hindsight the countywide reach did cause some issues — we got a bunch of calls from people way outside the plume who got scared for no reason — but at the time it felt like the safer choice just because it was the tool I knew.

**Interviewer:** Let's move to the third decision point — the escalation discussion. What was happening then?

**Participant:** About two hours in, the health officer's sensor readings were coming through — text table, updated every fifteen minutes — and contaminant levels were sitting in the advisory range, not danger range. But right around the same time, a resident's photo of this huge black smoke plume went viral locally, just an incredibly dramatic shot, rooftops with this black column behind them. Media started calling, asking if we were about to order an evacuation.

**Interviewer:** How did that shape your thinking?

**Participant:** Honestly, looking at that photo, my gut said this looks bad, we should be moving toward evacuation language. I actually had a draft evacuation recommendation half-written. The sensor table was open right there on my second monitor the whole time, showing levels weren't at that threshold, but the image was what I kept coming back to when I was talking through it with the team — how thick and dark that smoke looked. We ended up holding at shelter-in-place because the health officer pushed back hard on the data, not because I'd fully talked myself out of the escalation.

**Interviewer:** What did you learn afterward?

**Participant:** The follow-up readings thirty minutes later confirmed levels had stayed stable the whole time. And it turned out that black smoke was mostly from a stockpile of packaging material catching fire, not the solvents themselves. So visually it looked like the worst-case scenario, but the actual air data never supported that story.

**Interviewer:** Last decision point — the all-clear.

**Participant:** By hour five, suppression's basically done, Incident Commander says fire's under control. But we've got parents showing up at the school reunification point, some residents still smelling residual smoke, and the health officer recommends lifting shelter-in-place but keeping a window-closure advisory for two more hours as a buffer. I went with that phased approach instead of a full all-clear right away.

**Interviewer:** Any pushback on that?

**Participant:** A handful of residents said the phased message was confusing — they wanted a clean yes-or-no. But given we still had some odor reports, I felt the cautious, staged approach was more defensible than an immediate blanket all-clear, even if it wasn't as tidy a message.

**Interviewer:** If the reverse-911 system had already been used successfully in a live incident before this one, do you think you'd have made a different channel choice?

**Participant:** Probably, yeah. If I'd seen it perform live even once, I think I'd have trusted it enough to use it instead of CAN, especially given the geotargeting benefit.

**Interviewer:** And if that photo had never circulated — does the escalation conversation go differently?

**Participant:** I think it's calmer, honestly. The sensor data alone was pretty steady the whole time. Without that image driving the room's mood, we probably stay at shelter-in-place without ever drafting the evacuation language.

**Interviewer:** Anything you'd evaluate differently with the same information again?

**Participant:** Maybe build in a habit of stating the data source out loud before reacting to whatever's most visually striking in the moment. And for channel choice, I'd want someone to actually pull the reverse-911 test record and talk to the on-call tech before I default to the tool I already know, so familiarity isn't doing all the deciding. Otherwise, given what we knew at each point, I think the calls were reasonable.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{EM_Biased_2}}",
  "occupational_domain": "{{Emergency management and Civil Protection}}",
  "role": "{{Public Information Officer (Emergency/Crisis Communications)}}"
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
