You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about a specific inspection you handled, purely for understanding how you approached the decisions — not an audit of your conclusions. That okay with you?

Participant: Sure, no problem. I've got the file pulled up if I need to check dates.

Interviewer: Great. Can you give me your role and a bit of background first?

Participant: I'm a fire inspector, been doing building code compliance for about nine years now, mostly commercial and mixed-use properties. This particular case was an annual re-inspection tied to a certificate of occupancy renewal for a three-story building — retail on the ground floor, offices above. They'd just finished a tenant fit-out renovation, so the stakes were a little higher than a routine annual check.

Interviewer: Walk me through what happened, from arrival to wrap-up.

Participant: I got there in the morning, met the building manager — I've worked with him for probably four years across different properties he's managed. Good guy, very responsive, easy to deal with. The building was operating normally, tenants open, so I had to work around foot traffic in a few spots. First thing I did was the egress corridors. Near the loading dock there's a secondary egress path, and I found it partially narrowed by stacked delivery pallets. He told me it was just for that morning's delivery. I measured it anyway — clear width was under the code minimum with the pallets there. I wrote that up as a formal minor violation with a short correction window, regardless of what he said about the timing. Later, actually, one of the retail staff mentioned in passing that the pallets had been sitting there off and on for a couple weeks, not just that morning. Didn't change my classification, but it stuck with me.

Then we went up to check the secondary stairwell door. That's when I found the self-closing device disconnected — the arm was just hanging loose. That's a meaningful finding; a fire door that won't close on its own defeats the whole point of the assembly during smoke or fire conditions. He was pretty apologetic about it, said maintenance had already been told about it the week before, and he offered to have someone reattach it right then while I was standing there.

Interviewer: And the alarm system?

Participant: Right, that was next. I pulled the monthly test log and there was a gap — one month with nothing recorded. He said the test had definitely happened, it just hadn't been logged properly. I didn't take that at face value. I asked for the monitoring company's records instead of just accepting the verbal explanation, and I flagged the gap as an open documentation item pending that verification rather than closing it out.

Interviewer: Let's go through each of those decisions in a bit more detail, starting with the pallets. What made you decide to formally cite that instead of just noting it informally?

Participant: The corridor width is objective — I measured it, it was under the minimum, full stop. Doesn't matter what the explanation is for why it's narrow. That one felt straightforward to me; the measurement does the talking.

Interviewer: And the door closer — how did you land on an advisory note instead of a formal citation, given you just described it as a meaningful life-safety item?

Participant: Yeah, that one I went back and forth on a bit. Technically, sure, it's a significant deficiency — no-questions-asked at the code level. But he was really upfront about it, apologized a couple times, said his team already knew and it just hadn't been actioned yet, and he wanted to fix it right there in front of me. After four years of him being straight with me on other properties, going in hard with a formal citation over something he was already fixing on the spot felt like more friction than the moment called for. So I logged it as an advisory note instead — get it corrected, follow up next visit, no formal paperwork trail.

Interviewer: Did you check the maintenance ticket he referenced, or look at whether this had come up before at that building?

Participant: Not in the moment, no. I didn't pull the ticket timestamp, and I didn't cross-check last year's report right there. In hindsight I probably should have — turned out the ticket was only logged that morning, not the week before like he said, and there'd actually been a near-identical closer issue flagged and marked corrected in last year's inspection. So it wasn't new, it was a repeat. I didn't know that at the time I made the call, though.

Interviewer: What was going through your mind that made the apology and the offer to fix it feel like enough?

Participant: Honestly, it just felt like the reasonable, low-friction way to handle it with someone who's generally cooperative. I wasn't thinking about whether it had happened before — I was thinking about the guy standing in front of me being embarrassed about it and already moving to fix it. Writing him up formally in that moment felt like it would've been an unnecessarily hard line to take.

Interviewer: Third decision — the alarm log gap. Why request outside verification there but not for the door closer?

Participant: Different kind of claim, I think. "The test happened but wasn't logged" is something I can actually check against a third party — the monitoring company has their own records independent of him. There's no equivalent independent record for a closer that's already been reattached; once it's fixed, the evidence is gone. So partly it was about what was still verifiable versus what wasn't.

Interviewer: Fourth decision — writing the final recommendation. How did you weigh the three findings together?

Participant: I recommended conditional renewal — correct the pallet obstruction, get the alarm verification resolved, and monitor the door closer as an open advisory item. My supervisor actually pushed back a little, asked why the closer wasn't a formal citation given the classification. I explained the on-site correction and the manager's responsiveness. He wasn't fully satisfied but didn't override it. The manager also messaged me afterward thanking me for being reasonable during the visit.

Interviewer: What information, if you'd had it at the time, would have changed your call on the door closer?

Participant: Knowing it was a repeat finding from last year would have changed things for sure — that's a pattern, not a one-off. If I'd pulled that file before finalizing the note instead of after, I think I'd have citied it formally.

Interviewer: If the manager had reacted differently — say, defensively or dismissively instead of apologetically — do you think your classification would have been different?

Participant: Probably, yeah. If he'd pushed back or acted like it wasn't a big deal, I think I'd have gone straight to a formal citation without much hesitation. The fact that he was already owning it and fixing it changed how I approached writing it up.

Interviewer: Looking back, is there a point where you'd want more information before deciding again?

Participant: The closer, for sure. I'd want the maintenance ticket pulled and last year's report checked before I finalize any classification, not after.

Interviewer: Anything you'd tell a newer inspector handling a similar situation with a cooperative, familiar contact?

Participant: Probably to separate the paperwork from the personal read on the guy. The relationship can tell you how a conversation's going to go, but it shouldn't really be what decides the classification — the classification should hold up the same whether the person in front of you is anxious about it or not.
}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{HE_Biased_1}}",
  "occupational_domain": "{{High-risk Engineering and Fire Engineering}}",
  "role": "{{Fire Inspector (Building Code Compliance)}}"
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
