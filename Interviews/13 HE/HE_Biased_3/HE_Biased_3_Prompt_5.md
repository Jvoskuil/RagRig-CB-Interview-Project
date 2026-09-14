You are an independent occupational-task analyst. Classify the tasks actually described in the interview below using only the taxonomy and definitions supplied in this prompt.

Do not classify the occupation in general. Classify the work activity and decision episode represented in this interview. Do not infer categories solely from the job title, industry, prestige, assumed education, or stereotypes. Use the interview text as the primary evidence.

Do not assess cognitive biases. Do not use any hidden bias-generation specification. Do not use any prior validator output. This is an independent task-taxonomy annotation.

Return valid JSON only. Do not return prose outside the JSON object.

INTERVIEW
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a research review of design decision-making, nothing you say will be tied to your name in any report, and you can skip anything you're not comfortable discussing. Sound okay?

Participant: Yeah, that's fine. I've done these before for our internal lessons-learned process, so I'm used to it.

Interviewer: Great. Can you start by telling me what your role was on this project and what the assignment involved?

Participant: Sure. I'm the lead design engineer on a sprinkler retrofit for a distribution warehouse, about 140,000 square feet, tilt-up concrete. The building owner was bringing in a new third-party logistics tenant who needed part of the floor converted to high-piled rack storage, double-row selective rack up to 32 feet. My job was to take the existing system, which was designed for a much lighter occupancy, and redesign it to handle the new storage configuration, get it through plan review, and get it installed before the tenant's lease start.

Interviewer: What made this one more complicated than a typical retrofit?

Participant: Mainly the schedule. We had about three weeks from kickoff to permit submission because the tenant's stocking schedule was locked in and the owner didn't want to renegotiate the lease start. On top of that, the existing water supply and riser sizing were set up for the old, lower-hazard use, so I was working within infrastructure that wasn't originally built for this.

Interviewer: Walk me through the incident from the beginning, in your own words.

Participant: We got the go-ahead and I needed to nail down the commodity classification pretty fast, because that drives everything else, the density, the rack sprinkler requirements, all of it. I hadn't gotten a finalized SKU or packaging list from the tenant yet, they were still finalizing their own inventory plans, but the owner wanted the classification locked so he could set the retrofit budget. I'd done two other jobs for similar 3PL operators in the past couple of years, so I had a sense of what that kind of tenant typically stores. Based on that, I classified it as Class III commodity and moved forward with design. From there I pulled the NFPA design density and area curves for that classification at 32 feet of rack height, picked a density/area point that cleared the code minimum, and built out the hydraulic calculations. That went to the owner for a value engineering pass, since the number came in over his budget, and we had a conversation about trimming the in-rack sprinkler allowance to bring the cost down. After the system was installed, we got to commissioning, and even with the schedule tight, I made sure we did the full witnessed flow test before sign-off, which the AHJ requires.

Interviewer: Let's reconstruct that chronologically. What came first?

Participant: Classification first, in the first few days. Then the hydraulic calc and density selection, maybe a week and a half in, right before permit submission. The value-engineering conversation with the owner happened after plan review comments came back, so maybe two and a half weeks in. Commissioning was right at the end, days before the tenant's move-in date.

Interviewer: What did you learn after the classification that you didn't know at the time you made it?

Participant: A partial inventory list came through a bit later, and it showed a decent chunk of exposed unexpanded plastics mixed in with the cartoned goods, more than I'd assumed. That pushed the actual profile closer to a plastics classification than straight Class III.

Interviewer: Let's go back to that classification decision specifically. What information did you actually have in hand at that point?

Participant: I had the tenant's general business type, third-party logistics handling retail goods, and I had my own history with two comparable clients. I didn't have their SKU list yet.

Interviewer: What other approaches did you consider before settling on Class III?

Participant: I could have asked for a preliminary packaging sample list before finalizing anything, or gone conservative and designed to a worst-case plastics assumption until the data came in.

Interviewer: Why didn't you go with either of those?

Participant: Honestly, this type of tenant, in my experience, usually runs cartoned retail goods, maybe some mixed packaging, but nothing that changes the classification much. The two prior jobs I'd done for similar operators both landed at Class III, so I went with that pattern rather than waiting on the tenant's list, especially with the owner pushing to lock the budget.

Interviewer: What would have made you wait for the SKU data instead?

Participant: If something about this particular tenant's business model had stood out as different, like if they'd mentioned handling electronics or aerosols specifically. Nothing in the early conversations flagged that, so I didn't press for the list before moving forward.

Interviewer: Let's move to the density selection. What alternatives were actually on the table?

Participant: There were several density/area points that would satisfy the code minimum for Class III at that rack height, some requiring more in-rack sprinklers, some less. I could have compared those against the specific rack configuration and aisle widths, or checked the manufacturer's design guide for something tailored to that layout.

Interviewer: What did you actually do?

Participant: I took the first density/area point that cleared the minimum for the assumed classification and built the calc package around it. We were up against the submission deadline, and that point technically satisfied the requirement, so I ran with it rather than working through the other combinations.

Interviewer: Did the plan reviewer have any comments on that later?

Participant: Yeah, the AHJ reviewer flagged that the point I'd chosen was pretty close to the edge of the applicable curve for the actual rack configuration. Not a rejection, just a note.

Interviewer: What was going through your mind when the owner asked for value engineering?

Participant: He wanted the number under budget, and the in-rack sprinkler allowance was the biggest line item I could trim. Retaining it would've kept more margin against the classification uncertainty, since I knew the plastics content wasn't fully confirmed yet. But we've got two more retrofit jobs pending with this same owner, and I didn't want that relationship to get strained over this one line item, so I recommended pulling the in-rack allowance to hit his number.

Interviewer: Did you lay out the classification uncertainty as part of that recommendation?

Participant: Not in as much detail as I probably could have. I mentioned it in passing but framed the removal as a reasonable trade-off rather than walking him through how much margin we'd be giving up.

Interviewer: Last decision point, commissioning. What determined how much testing you pursued?

Participant: The AHJ requires a witnessed flow test regardless, so that wasn't really optional. With the move-in date bearing down, I could have leaned on the contractor's certification paperwork and expedited sign-off, or done a partial test on just the modified risers. I decided to do the full witnessed test anyway.

Interviewer: How did that turn out?

Participant: It passed, but the value came in close to the required minimum, close enough that I flagged it for monitoring going forward.

Interviewer: If you'd had the tenant's full SKU list before classifying the commodity, would you have done anything differently?

Participant: Probably, yeah. If I'd seen the plastics percentage upfront, I'd have leaned toward a more conservative classification from the start rather than defaulting to what I'd seen on similar jobs.

Interviewer: If there'd been no ongoing relationship with the building owner, do you think the value-engineering conversation would have gone differently?

Participant: Maybe. I'd like to think I'd have pushed harder on keeping the in-rack allowance, but I can't say for certain the outcome would've changed.

Interviewer: Looking back, is there a point where you'd make a different call given the same information you had at the time?

Participant: The classification, probably. Everything downstream followed from that first call, and I had the means to ask for more data before locking it in.}}

OPTIONAL METADATA
The following metadata may help identify the setting but must not determine the classification:
{
  "interview_id": "{{HE_Biased_3}}",
  "occupational_domain": "{{High-risk Engineering and Fire Engineering}}",
  "role": "{{Fire Protection System Designer (Sprinkler/Suppression Design Engineer)}}"
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
