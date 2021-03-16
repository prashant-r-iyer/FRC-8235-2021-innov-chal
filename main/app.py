import db


name_athlete = ''
outdoors_athlete = False
bodypart_athlete = 'U' # U for upper, L for lower, C for core
budget_athlete = 1
time_athlete = '' # M for morning, A for afternoon, E for evening

# Format: Sublists containing [Name, Outdoors, Bodypart, Cost, Timing]
events = {
    1: ['Mum', False , 'L', 69, 'E'],
    2: ['Dad', True, 'L', 420, 'E'],
    69: ['Dad', True, 'C', 1, 'M'],
    21: ['L', True, 'U', 420, 'M'],
    0: ['Dad', True, 'C', 4200, 'A'],
}

bias = {}

for event_key in events:
    current_bias = 0
    if events[event_key][1] == outdoors_athlete:
        current_bias += 1
    if events[event_key][2] == bodypart_athlete:
        current_bias += 1
    if events[event_key][4] == time_athlete:
        current_bias += 1
    weightage = (budget_athlete - events[event_key][3]) / budget_athlete
    bias_add = 1 + (weightage * 1)
    if budget_athlete == 0:
        if events[event_key][4] == budget_athlete:
            bias_add = 1
    if bias_add < 0:
        bias_add = 0
    current_bias += bias_add
    bias[event_key] = current_bias

bias = dict(sorted(bias.items(), key=lambda item: item[1], reverse=True))

top_3_keys = []
count = 0
for bias_item in bias:
    top_3_keys.append(bias_item)
    count += 1
    if count == 3:
        break

top_3_events = []
for top_3_key in top_3_keys:
    top_3_events.append(events[top_3_key])

print(top_3_events)

id = db.previous_id() + 1
name_trainer = ''
outdoors_trainer = False
bodypart_trainer = ''
cost_trainer = 0


details = db.database_entry([id, name_trainer, outdoors_trainer, bodypart_trainer, cost_trainer])

db.input_event(details)
